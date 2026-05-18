import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, roc_auc_score, confusion_matrix, 
                             classification_report, roc_curve, auc)
import joblib
import json
import os
from datetime import datetime


class ChurnModelTrainer:
    """Trains and evaluates multiple churn prediction models"""
    
    def __init__(self):
        self.models = {}
        self.results = {}
        self.best_model = None
        self.best_model_name = None
        
    def train_logistic_regression(self, X_train, y_train):
        """Train Logistic Regression model"""
        print("\n" + "="*50)
        print("Training Logistic Regression...")
        print("="*50)
        
        lr = LogisticRegression(max_iter=1000, random_state=42, n_jobs=-1)
        lr.fit(X_train, y_train)
        self.models['Logistic Regression'] = lr
        
        print("[OK] Logistic Regression trained")
        return lr
    
    def train_random_forest(self, X_train, y_train):
        """Train Random Forest model"""
        print("\n" + "="*50)
        print("Training Random Forest...")
        print("="*50)
        
        rf = RandomForestClassifier(
            n_estimators=100,
            max_depth=15,
            min_samples_split=10,
            min_samples_leaf=5,
            random_state=42,
            n_jobs=-1,
            class_weight='balanced'
        )
        rf.fit(X_train, y_train)
        self.models['Random Forest'] = rf
        
        print("[OK] Random Forest trained")
        return rf
    
    def train_gradient_boosting(self, X_train, y_train):
        """Train Gradient Boosting model"""
        print("\n" + "="*50)
        print("Training Gradient Boosting...")
        print("="*50)
        
        gb = GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            min_samples_split=10,
            min_samples_leaf=5,
            random_state=42,
            subsample=0.8
        )
        gb.fit(X_train, y_train)
        self.models['Gradient Boosting'] = gb
        
        print("[OK] Gradient Boosting trained")
        return gb
    
    def evaluate_model(self, model_name, model, X_test, y_test):
        """Evaluate a single model"""
        # Make predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        # Calculate metrics
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred),
            'roc_auc': roc_auc_score(y_test, y_pred_proba),
            'confusion_matrix': confusion_matrix(y_test, y_pred).tolist()
        }
        
        self.results[model_name] = metrics
        
        # Print results
        print(f"\n{'='*50}")
        print(f"Results for {model_name}")
        print(f"{'='*50}")
        print(f"Accuracy:  {metrics['accuracy']:.4f}")
        print(f"Precision: {metrics['precision']:.4f}")
        print(f"Recall:    {metrics['recall']:.4f}")
        print(f"F1-Score:  {metrics['f1_score']:.4f}")
        print(f"ROC-AUC:   {metrics['roc_auc']:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))
        
        return metrics, y_pred, y_pred_proba
    
    def train_and_evaluate(self, X_train, X_test, y_train, y_test):
        """Train all models and evaluate"""
        print("\n\n" + "#"*50)
        print("# STARTING MODEL TRAINING AND EVALUATION")
        print("#"*50)
        
        # Train all models
        self.train_logistic_regression(X_train, y_train)
        self.train_random_forest(X_train, y_train)
        self.train_gradient_boosting(X_train, y_train)
        
        # Evaluate all models
        print("\n\n" + "#"*50)
        print("# MODEL EVALUATION ON TEST SET")
        print("#"*50)
        
        predictions = {}
        for model_name, model in self.models.items():
            metrics, y_pred, y_pred_proba = self.evaluate_model(model_name, model, X_test, y_test)
            predictions[model_name] = {
                'predictions': y_pred.tolist(),
                'probabilities': y_pred_proba.tolist()
            }
        
        # Select best model
        best_model_name = max(self.results, key=lambda x: self.results[x]['roc_auc'])
        self.best_model_name = best_model_name
        self.best_model = self.models[best_model_name]
        
        print("\n\n" + "#"*50)
        print(f"# BEST MODEL: {best_model_name}")
        print(f"# ROC-AUC Score: {self.results[best_model_name]['roc_auc']:.4f}")
        print("#"*50)
        
        return self.best_model, self.results
    
    def save_model(self, filepath):
        """Save best model"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self.best_model, filepath)
        print(f"\n[OK] Best model ({self.best_model_name}) saved to {filepath}")
    
    def save_results(self, filepath):
        """Save training results as JSON"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Convert numpy types to native Python types for JSON serialization
        results_json = {}
        for model_name, metrics in self.results.items():
            results_json[model_name] = {
                'accuracy': float(metrics['accuracy']),
                'precision': float(metrics['precision']),
                'recall': float(metrics['recall']),
                'f1_score': float(metrics['f1_score']),
                'roc_auc': float(metrics['roc_auc']),
                'confusion_matrix': metrics['confusion_matrix']
            }
        
        with open(filepath, 'w') as f:
            json.dump(results_json, f, indent=4)
        
        print(f"[OK] Results saved to {filepath}")
    
    def get_model_info(self):
        """Get information about all trained models"""
        info = {
            'timestamp': datetime.now().isoformat(),
            'models_trained': list(self.models.keys()),
            'best_model': self.best_model_name,
            'best_model_score': self.results[self.best_model_name]['roc_auc']
        }
        return info


if __name__ == "__main__":
    # Load preprocessed data
    X_train = pd.read_csv('../data/X_train.csv')
    X_test = pd.read_csv('../data/X_test.csv')
    y_train = pd.read_csv('../data/y_train.csv').squeeze()
    y_test = pd.read_csv('../data/y_test.csv').squeeze()
    
    # Train and evaluate models
    trainer = ChurnModelTrainer()
    best_model, results = trainer.train_and_evaluate(X_train, X_test, y_train, y_test)
    
    # Save model and results
    trainer.save_model('../models/churn_model.pkl')
    trainer.save_results('../models/model_results.json')
    
    print("\n[OK] Model training completed successfully!")
