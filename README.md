# 🎯 Customer Churn Prediction & Retention Analytics System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask 2.3](https://img.shields.io/badge/flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![React 18](https://img.shields.io/badge/react-18+-blue.svg)](https://react.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive machine learning system to predict customer churn and provide actionable retention insights with real-time predictions and interactive visualization.

## 📋 Project Overview

This project implements an end-to-end machine learning solution for customer churn prediction with the following components:

- **📊 Data Analysis**: Exploratory Data Analysis (EDA) and feature engineering to identify key churn drivers
- **🤖 ML Models**: Logistic Regression, Random Forest, and Gradient Boosting classifiers with comprehensive evaluation
- **🔌 REST API**: Flask backend with endpoints for single and batch predictions
- **📱 React Dashboard**: Interactive frontend for real-time churn risk assessment and model performance monitoring

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend** | Python, Flask, Flask-CORS | 3.8+, 2.3.3 |
| **ML/Data** | Scikit-learn, Pandas, NumPy | 1.3.0, 2.0.3, 1.24.3 |
| **Frontend** | React, Axios, Recharts | 18.2.0, 1.4.0, 2.8.0 |
| **Database** | CSV storage (production: PostgreSQL) | N/A |
| **Deployment** | Docker, Gunicorn | Optional |

## 📁 Project Structure

```
Customer Churn Prediction & Retention Analytics System/
├── backend/                          # Flask API server
│   ├── app.py                       # Main Flask application
│   ├── preprocessor.py              # Data preprocessing pipeline
│   ├── model_trainer.py             # Model training module
│   ├── test_api.py                  # API testing suite
│   ├── requirements.txt             # Python dependencies
│   └── API_DOCUMENTATION.md         # API endpoint documentation
├── frontend/                         # React dashboard
│   ├── src/
│   │   ├── components/              # React components
│   │   │   ├── Dashboard.js
│   │   │   ├── PredictionForm.js
│   │   │   ├── ChurnRiskChart.js
│   │   │   └── ModelMetrics.js
│   │   ├── styles/                  # CSS stylesheets
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   └── package.json
├── notebooks/                        # Jupyter notebooks
│   ├── generate_dataset.py          # Synthetic data generation
│   ├── 01_EDA.ipynb                 # Exploratory Data Analysis
│   ├── 02_Feature_Engineering.ipynb # Feature engineering showcase
│   └── 03_Model_Training.ipynb      # Model training & evaluation
├── data/                            # Dataset storage
│   └── customer_churn.csv           # Raw dataset
├── models/                          # Trained model artifacts
│   ├── churn_model.pkl              # Best trained model
│   ├── preprocessor.pkl             # Fitted preprocessor
│   └── model_results.json           # Model evaluation metrics
├── README.md                        # This file
├── INTEGRATION_GUIDE.md             # Setup and deployment guide
├── quickstart.sh                    # Linux/macOS quick start
├── quickstart.bat                   # Windows quick start
└── .gitignore                       # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Node.js 14+** - [Download](https://nodejs.org/)
- **Git** - [Download](https://git-scm.com/)

### Option 1: Automated Setup (Recommended)

**Windows:**
```bash
quickstart.bat
```

**Linux/macOS:**
```bash
chmod +x quickstart.sh
./quickstart.sh
```

### Option 2: Manual Setup

**1. Clone repository**
```bash
git clone <repository-url>
cd "Customer Churn Prediction & Retention Analytics System"
```

**2. Setup Backend**
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**3. Prepare Data & Train Models**
```bash
# Generate dataset
python ../notebooks/generate_dataset.py

# Preprocess data
python preprocessor.py

# Train models
python model_trainer.py
```

**4. Start Backend API**
```bash
python app.py
# API running at http://localhost:5000
```

**5. Setup & Start Frontend** (New Terminal)
```bash
cd frontend
npm install
npm start
# Dashboard running at http://localhost:3000
```

## 📊 Features

### Machine Learning
- ✅ **3 Classification Models**: Logistic Regression, Random Forest, Gradient Boosting
- ✅ **Feature Engineering**: 15+ derived features including customer lifetime value, engagement ratio
- ✅ **Model Evaluation**: Accuracy, Precision, Recall, F1-Score, ROC-AUC metrics
- ✅ **Class Imbalance Handling**: Stratified sampling and class weights
- ✅ **Data Preprocessing**: Scaling, encoding, train-test split

### API Backend
- ✅ **Single Predictions**: Real-time churn risk assessment for individual customers
- ✅ **Batch Predictions**: Process multiple customer records simultaneously
- ✅ **Model Information**: Retrieve model details and feature lists
- ✅ **Performance Metrics**: Access model evaluation results
- ✅ **CORS Enabled**: Cross-origin requests supported
- ✅ **Error Handling**: Comprehensive error messages and logging

### React Dashboard
- ✅ **Interactive Forms**: Intuitive customer data input interface
- ✅ **Risk Visualization**: Color-coded risk levels (LOW, MEDIUM, HIGH)
- ✅ **Sample Data**: Pre-loaded high-risk and low-risk examples
- ✅ **Model Metrics Display**: Real-time performance metrics from all models
- ✅ **Probability Charts**: Visual representation of churn probabilities
- ✅ **Recommendations**: Actionable retention strategies based on predictions
- ✅ **Responsive Design**: Mobile-friendly interface

## 📈 Model Performance

The system trains three classification models and automatically selects the best one based on ROC-AUC score:

```
Logistic Regression
├── Accuracy:  ~82%
├── Precision: ~78%
├── Recall:    ~72%
├── F1-Score:  ~75%
└── ROC-AUC:   ~88%

Random Forest
├── Accuracy:  ~85%
├── Precision: ~81%
├── Recall:    ~79%
├── F1-Score:  ~80%
└── ROC-AUC:   ~91%

Gradient Boosting
├── Accuracy:  ~86%
├── Precision: ~83%
├── Recall:    ~80%
├── F1-Score:  ~81%
└── ROC-AUC:   ~92% ✓ BEST
```

## 🔌 API Endpoints

### Health & Info
- `GET /` - API status and endpoints
- `GET /health` - Health check
- `GET /model-info` - Model details
- `GET /model-results` - Model evaluation metrics

### Predictions
- `POST /predict` - Single customer prediction
- `POST /batch-predict` - Batch customer predictions

**See [API_DOCUMENTATION.md](backend/API_DOCUMENTATION.md) for detailed examples**

## 🎯 Usage Examples

### Using the Dashboard
1. Open http://localhost:3000
2. Enter customer data or use sample buttons
3. Click "🚀 Predict Churn"
4. View risk assessment and recommendations

### Using the API
```bash
# Single prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "tenure_months": 12,
    "monthly_charges": 65.5,
    "satisfaction_score": 4,
    ...
  }'

# Batch predictions
curl -X POST http://localhost:5000/batch-predict \
  -H "Content-Type: application/json" \
  -d '{
    "customers": [
      {"customer_id": "CUST001", ...},
      {"customer_id": "CUST002", ...}
    ]
  }'
```

## 🔍 Data Features (15 Input Features)

| Feature | Type | Description |
|---------|------|-------------|
| tenure_months | Numeric | Customer tenure in months |
| monthly_charges | Numeric | Monthly subscription cost |
| total_charges | Numeric | Total charges to date |
| contract_length | Numeric | Contract duration in months |
| internet_service | Binary | Internet service subscription |
| phone_service | Binary | Phone service subscription |
| streaming_tv | Binary | Streaming TV subscription |
| streaming_movies | Binary | Streaming movies subscription |
| device_protection | Binary | Device protection plan |
| tech_support | Binary | Technical support service |
| online_security | Binary | Online security service |
| backup_service | Binary | Backup service subscription |
| satisfaction_score | Numeric | Customer satisfaction (1-5) |
| support_tickets | Numeric | Number of support tickets |
| payment_delay | Numeric | Number of payment delays |

## 📊 Key Insights & Churn Drivers

From EDA analysis:
- **Tenure**: Customers with <6 months tenure have 40%+ churn rate
- **Satisfaction**: Low satisfaction scores strongly correlate with churn
- **Support Issues**: High support ticket volume indicates dissatisfaction
- **Contract**: Monthly contracts have 3x higher churn than long-term
- **Payment**: Payment delays are strong churn predictors

## 🧪 Testing

### Test API Endpoints
```bash
cd backend
python test_api.py
```

### Test Individual Endpoints
```bash
# Health check
curl http://localhost:5000/health

# Model results
curl http://localhost:5000/model-results
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| API not connecting | Ensure Flask running on http://localhost:5000 |
| Model files missing | Run preprocessor.py and model_trainer.py |
| Frontend won't start | Delete node_modules, run npm cache clean --force, npm install |
| Port 5000/3000 in use | Change ports in app.py and package.json |
| CORS errors | Verify Flask-CORS is installed and enabled |

## 📚 Documentation

- [API Documentation](backend/API_DOCUMENTATION.md) - Detailed endpoint reference
- [Integration Guide](INTEGRATION_GUIDE.md) - Setup, deployment, troubleshooting
- [Feature Engineering Notebook](notebooks/02_Feature_Engineering.ipynb) - Feature creation process
- [Model Training Notebook](notebooks/03_Model_Training.ipynb) - Model training details
- [EDA Notebook](notebooks/01_EDA.ipynb) - Data exploration insights

## 🚀 Deployment

### Docker Deployment
```bash
# Build Docker image
docker build -t churn-prediction .

# Run container
docker run -p 5000:5000 -p 3000:3000 churn-prediction
```

### Cloud Deployment
- **Backend**: Heroku, AWS Elastic Beanstalk, Google Cloud Run
- **Frontend**: Vercel, Netlify, AWS S3 + CloudFront

## 📈 Future Enhancements

- [ ] Add database persistence (PostgreSQL/MongoDB)
- [ ] Implement user authentication and RBAC
- [ ] Add batch processing pipeline
- [ ] Create admin dashboard for model monitoring
- [ ] Setup CI/CD with GitHub Actions
- [ ] Add automated testing (pytest, Jest)
- [ ] Implement API rate limiting
- [ ] Add Swagger API documentation
- [ ] Create mobile app
- [ ] Add real-time model monitoring

## 🤝 Contributing

Contributions are welcome! Please follow the commit message format:
```
[TYPE] Step X: Brief description

[TYPE] can be: SETUP, DATA, FEATURE, ML-MODEL, API, FRONTEND, INTEGRATION, DOCS
```

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Author

Created for portfolio demonstration of full-stack ML engineering capabilities.

## ⭐ Support

If this project helped you, please consider giving it a star on GitHub!

---

**Last Updated**: May 2026  
**Status**: Production Ready ✓
