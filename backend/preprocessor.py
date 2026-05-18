import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import os

class DataPreprocessor:
    """Handles data loading, cleaning, and feature engineering"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.encoders = {}
        self.feature_names = None
        
    def load_data(self, filepath):
        """Load customer churn dataset"""
        df = pd.read_csv(filepath)
        print(f"[OK] Data loaded: {df.shape}")
        return df
    
    def feature_engineering(self, df):
        """Create new features from existing ones"""
        df = df.copy()
        
        # Create tenure buckets
        df['tenure_category'] = pd.cut(df['tenure_months'], 
                                       bins=[0, 6, 12, 24, 100], 
                                       labels=['0-6 months', '6-12 months', '12-24 months', '24+ months'])
        
        # Create charge level buckets
        df['charge_category'] = pd.cut(df['monthly_charges'],
                                       bins=[0, 50, 75, 100, 200],
                                       labels=['Low', 'Medium', 'High', 'Premium'])
        
        # Customer lifetime value proxy
        df['customer_value'] = df['tenure_months'] * df['monthly_charges']
        
        # Support engagement ratio
        df['support_engagement'] = df['support_tickets'] / (df['tenure_months'] + 1)
        
        # Service adoption rate (how many services they use)
        service_cols = ['internet_service', 'phone_service', 'streaming_tv', 
                       'streaming_movies', 'device_protection', 'tech_support', 
                       'online_security', 'backup_service']
        df['service_count'] = df[service_cols].sum(axis=1)
        
        # Payment delay indicator
        df['has_payment_delay'] = (df['payment_delay'] > 0).astype(int)
        
        print("[OK] Feature engineering completed")
        return df
    
    def encode_categorical(self, df, fit=True):
        """Encode categorical features"""
        df = df.copy()
        
        categorical_cols = ['tenure_category', 'charge_category']
        
        for col in categorical_cols:
            if fit:
                self.encoders[col] = LabelEncoder()
                df[col] = self.encoders[col].fit_transform(df[col].astype(str))
            else:
                df[col] = self.encoders[col].transform(df[col].astype(str))
        
        print(f"[OK] Categorical encoding completed for {len(categorical_cols)} features")
        return df
    
    def drop_unnecessary_columns(self, df):
        """Drop columns not needed for modeling"""
        cols_to_drop = ['customer_id', 'tenure_months', 'monthly_charges', 'total_charges']
        
        # Only drop if they exist
        cols_to_drop = [col for col in cols_to_drop if col in df.columns]
        df = df.drop(columns=cols_to_drop)
        
        print(f"[OK] Dropped {len(cols_to_drop)} unnecessary columns")
        return df
    
    def scale_features(self, X, fit=True):
        """Scale numerical features"""
        if fit:
            X_scaled = self.scaler.fit_transform(X)
        else:
            X_scaled = self.scaler.transform(X)
        
        X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
        print("[OK] Feature scaling completed")
        return X_scaled
    
    def preprocess(self, df, test_size=0.2, random_state=42, fit=True):
        """Complete preprocessing pipeline"""
        
        # Feature engineering
        df = self.feature_engineering(df)
        
        # Separate features and target
        X = df.drop('churn', axis=1)
        y = df['churn']
        
        # Encode categorical features
        X = self.encode_categorical(X, fit=fit)
        
        # Drop unnecessary columns
        X = self.drop_unnecessary_columns(X)
        
        # Store feature names
        if fit:
            self.feature_names = X.columns.tolist()
        
        # Scale features
        X = self.scale_features(X, fit=fit)
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
        
        print(f"[OK] Train-test split: Train {X_train.shape} | Test {X_test.shape}")
        print(f"[OK] Class distribution - Train: {y_train.value_counts().to_dict()} | Test: {y_test.value_counts().to_dict()}")
        
        return X_train, X_test, y_train, y_test
    
    def save_preprocessor(self, filepath):
        """Save preprocessor for later use"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self, filepath)
        print(f"[OK] Preprocessor saved to {filepath}")
    
    @staticmethod
    def load_preprocessor(filepath):
        """Load preprocessor"""
        preprocessor = joblib.load(filepath)
        print(f"[OK] Preprocessor loaded from {filepath}")
        return preprocessor


if __name__ == "__main__":
    # Initialize preprocessor
    preprocessor = DataPreprocessor()
    
    # Load data
    df = preprocessor.load_data('../data/customer_churn.csv')
    
    # Preprocess
    X_train, X_test, y_train, y_test = preprocessor.preprocess(df)
    
    # Save preprocessor
    preprocessor.save_preprocessor('../models/preprocessor.pkl')
    
    # Save processed data
    X_train.to_csv('../data/X_train.csv', index=False)
    X_test.to_csv('../data/X_test.csv', index=False)
    y_train.to_csv('../data/y_train.csv', index=False)
    y_test.to_csv('../data/y_test.csv', index=False)
    
    print("\n[OK] All preprocessing completed successfully!")
