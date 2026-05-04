import requests
import json

BASE_URL = 'http://localhost:5000'

def test_health():
    """Test health check endpoint"""
    print("\n" + "="*50)
    print("Testing Health Check Endpoint")
    print("="*50)
    
    response = requests.get(f'{BASE_URL}/health')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_single_prediction():
    """Test single prediction endpoint"""
    print("\n" + "="*50)
    print("Testing Single Prediction Endpoint")
    print("="*50)
    
    customer_data = {
        "tenure_months": 12,
        "monthly_charges": 65.5,
        "total_charges": 786,
        "contract_length": 12,
        "internet_service": 1,
        "phone_service": 1,
        "streaming_tv": 0,
        "streaming_movies": 0,
        "device_protection": 0,
        "tech_support": 1,
        "online_security": 1,
        "backup_service": 0,
        "satisfaction_score": 4,
        "support_tickets": 2,
        "payment_delay": 0
    }
    
    response = requests.post(f'{BASE_URL}/predict', json=customer_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_batch_prediction():
    """Test batch prediction endpoint"""
    print("\n" + "="*50)
    print("Testing Batch Prediction Endpoint")
    print("="*50)
    
    customers_data = {
        "customers": [
            {
                "customer_id": "CUST001",
                "tenure_months": 12,
                "monthly_charges": 65.5,
                "total_charges": 786,
                "contract_length": 12,
                "internet_service": 1,
                "phone_service": 1,
                "streaming_tv": 0,
                "streaming_movies": 0,
                "device_protection": 0,
                "tech_support": 1,
                "online_security": 1,
                "backup_service": 0,
                "satisfaction_score": 4,
                "support_tickets": 2,
                "payment_delay": 0
            },
            {
                "customer_id": "CUST002",
                "tenure_months": 3,
                "monthly_charges": 85.0,
                "total_charges": 255,
                "contract_length": 6,
                "internet_service": 1,
                "phone_service": 1,
                "streaming_tv": 1,
                "streaming_movies": 1,
                "device_protection": 1,
                "tech_support": 0,
                "online_security": 0,
                "backup_service": 0,
                "satisfaction_score": 2,
                "support_tickets": 5,
                "payment_delay": 2
            }
        ]
    }
    
    response = requests.post(f'{BASE_URL}/batch-predict', json=customers_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_model_info():
    """Test model info endpoint"""
    print("\n" + "="*50)
    print("Testing Model Info Endpoint")
    print("="*50)
    
    response = requests.get(f'{BASE_URL}/model-info')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_model_results():
    """Test model results endpoint"""
    print("\n" + "="*50)
    print("Testing Model Results Endpoint")
    print("="*50)
    
    response = requests.get(f'{BASE_URL}/model-results')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == '__main__':
    print("\n" + "#"*50)
    print("# TESTING FLASK API ENDPOINTS")
    print("#"*50)
    
    try:
        test_health()
        test_model_info()
        test_model_results()
        test_single_prediction()
        test_batch_prediction()
        
        print("\n" + "#"*50)
        print("# ALL TESTS COMPLETED")
        print("#"*50)
    
    except requests.exceptions.ConnectionError:
        print("\n✗ Error: Could not connect to API")
        print("Make sure the Flask app is running with: python app.py")
    except Exception as e:
        print(f"\n✗ Error: {e}")
