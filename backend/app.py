from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Load model and preprocessor
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models/churn_model.pkl')
PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), '../models/preprocessor.pkl')
RESULTS_PATH = os.path.join(os.path.dirname(__file__), '../models/model_results.json')

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    with open(RESULTS_PATH, 'r') as f:
        model_results = json.load(f)
    print("✓ Model and preprocessor loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    preprocessor = None
    model_results = {}


@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Customer Churn Prediction API',
        'version': '1.0.0',
        'endpoints': {
            '/health': 'Health check',
            '/predict': 'Make predictions',
            '/batch-predict': 'Batch predictions',
            '/model-info': 'Get model information',
            '/model-results': 'Get model results'
        }
    }), 200


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    if model is None:
        return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500
    
    return jsonify({
        'status': 'success',
        'model_loaded': model is not None,
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/predict', methods=['POST'])
def predict():
    """Make a single prediction"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Convert to DataFrame for preprocessing
        df = pd.DataFrame([data])
        
        # Apply preprocessing
        df_processed = preprocessor.feature_engineering(df)
        X = preprocessor.encode_categorical(df_processed, fit=False)
        X = preprocessor.drop_unnecessary_columns(X)
        X = preprocessor.scale_features(X, fit=False)
        
        # Make prediction
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0]
        
        return jsonify({
            'status': 'success',
            'prediction': int(prediction),
            'churn_probability': float(probability[1]),
            'no_churn_probability': float(probability[0]),
            'risk_level': 'HIGH' if probability[1] > 0.7 else 'MEDIUM' if probability[1] > 0.4 else 'LOW'
        }), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/batch-predict', methods=['POST'])
def batch_predict():
    """Make batch predictions"""
    try:
        data = request.get_json()
        
        if not data or 'customers' not in data:
            return jsonify({'error': 'No customer data provided'}), 400
        
        customers = data['customers']
        results = []
        
        for customer in customers:
            try:
                # Convert to DataFrame for preprocessing
                df = pd.DataFrame([customer])
                
                # Apply preprocessing
                df_processed = preprocessor.feature_engineering(df)
                X = preprocessor.encode_categorical(df_processed, fit=False)
                X = preprocessor.drop_unnecessary_columns(X)
                X = preprocessor.scale_features(X, fit=False)
                
                # Make prediction
                prediction = model.predict(X)[0]
                probability = model.predict_proba(X)[0]
                
                results.append({
                    'customer_id': customer.get('customer_id', 'unknown'),
                    'prediction': int(prediction),
                    'churn_probability': float(probability[1]),
                    'risk_level': 'HIGH' if probability[1] > 0.7 else 'MEDIUM' if probability[1] > 0.4 else 'LOW'
                })
            except Exception as e:
                results.append({
                    'customer_id': customer.get('customer_id', 'unknown'),
                    'error': str(e)
                })
        
        return jsonify({
            'status': 'success',
            'total_predictions': len(results),
            'predictions': results
        }), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/model-info', methods=['GET'])
def model_info():
    """Get model information"""
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        info = {
            'model_type': str(type(model).__name__),
            'features': preprocessor.feature_names if preprocessor else [],
            'n_features': len(preprocessor.feature_names) if preprocessor else 0,
            'timestamp_created': datetime.now().isoformat()
        }
        
        return jsonify({'status': 'success', 'model_info': info}), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/model-results', methods=['GET'])
def get_model_results():
    """Get model evaluation results"""
    try:
        if not model_results:
            return jsonify({'error': 'Model results not available'}), 500
        
        return jsonify({
            'status': 'success',
            'model_results': model_results
        }), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("Starting Customer Churn Prediction API...")
    app.run(debug=True, host='0.0.0.0', port=5000)
