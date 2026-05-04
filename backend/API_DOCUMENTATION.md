# Flask API Documentation

## Endpoints

### 1. Health Check
- **URL**: `/`
- **Method**: GET
- **Response**: Returns API status and available endpoints

**Example**:
```bash
curl http://localhost:5000/
```

### 2. API Health Status
- **URL**: `/health`
- **Method**: GET
- **Response**: Confirms model is loaded and API is ready

**Example**:
```bash
curl http://localhost:5000/health
```

### 3. Single Prediction
- **URL**: `/predict`
- **Method**: POST
- **Body**: JSON object with customer features
- **Response**: Churn prediction and probability

**Example**:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

**Response**:
```json
{
  "status": "success",
  "prediction": 0,
  "churn_probability": 0.25,
  "no_churn_probability": 0.75,
  "risk_level": "LOW"
}
```

### 4. Batch Predictions
- **URL**: `/batch-predict`
- **Method**: POST
- **Body**: JSON object with array of customer objects
- **Response**: Array of predictions

**Example**:
```bash
curl -X POST http://localhost:5000/batch-predict \
  -H "Content-Type: application/json" \
  -d '{
    "customers": [
      {
        "customer_id": "CUST001",
        "tenure_months": 12,
        "monthly_charges": 65.5,
        ...
      },
      {
        "customer_id": "CUST002",
        "tenure_months": 24,
        "monthly_charges": 85.0,
        ...
      }
    ]
  }'
```

### 5. Model Information
- **URL**: `/model-info`
- **Method**: GET
- **Response**: Details about the trained model

**Example**:
```bash
curl http://localhost:5000/model-info
```

### 6. Model Results
- **URL**: `/model-results`
- **Method**: GET
- **Response**: Model evaluation metrics (accuracy, precision, recall, F1, ROC-AUC)

**Example**:
```bash
curl http://localhost:5000/model-results
```

## Running the API

```bash
cd backend
python app.py
```

The API will be available at `http://localhost:5000`

## Required Input Features

All customer records must include:
- `tenure_months`: Customer tenure in months
- `monthly_charges`: Monthly subscription cost
- `total_charges`: Total charges to date
- `contract_length`: Contract duration in months
- `internet_service`: Binary (0/1)
- `phone_service`: Binary (0/1)
- `streaming_tv`: Binary (0/1)
- `streaming_movies`: Binary (0/1)
- `device_protection`: Binary (0/1)
- `tech_support`: Binary (0/1)
- `online_security`: Binary (0/1)
- `backup_service`: Binary (0/1)
- `satisfaction_score`: 1-5 scale
- `support_tickets`: Number of support tickets
- `payment_delay`: Number of payment delays

## Risk Levels

- **LOW**: Churn probability < 40%
- **MEDIUM**: Churn probability 40-70%
- **HIGH**: Churn probability > 70%
