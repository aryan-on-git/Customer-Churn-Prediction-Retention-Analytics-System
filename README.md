# Customer Churn Prediction & Retention Analytics System

A comprehensive machine learning system to predict customer churn and provide actionable retention insights.

## Project Overview

This project builds a classification model to predict customer churn using logistic regression and tree-based methods. It includes:
- **Data Analysis**: EDA and feature engineering to identify churn drivers
- **ML Models**: Logistic Regression and Decision Tree/Random Forest classifiers
- **API Backend**: Flask REST API for model serving
- **Dashboard Frontend**: React-based visualization of churn risk and customer insights

## Tech Stack

- **Backend**: Python, Pandas, Scikit-learn, Flask
- **Frontend**: React, Axios
- **Data Processing**: Jupyter Notebook for EDA

## Project Structure

```
├── backend/              # Flask API server
├── frontend/             # React dashboard
├── notebooks/            # Jupyter notebooks for EDA and analysis
├── data/                 # Dataset storage
├── models/               # Trained model artifacts
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- pip, npm

### Installation

#### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## Features

- 📊 Customer churn prediction using ML models
- 📈 Comprehensive EDA and feature analysis
- 🎯 Model evaluation with accuracy, precision-recall, and ROC-AUC metrics
- 🔌 RESTful API for real-time predictions
- 📱 Interactive dashboard for visualization
- 💾 Model persistence and versioning

## Model Performance

Model evaluation metrics will be updated as models are trained.

## Usage

1. Prepare your data in `data/` folder
2. Run EDA notebook in `notebooks/`
3. Train models through the backend
4. Access predictions via API or dashboard

## Contributing

Commit messages should follow: `[commit-type] Step X: Description`

## License

MIT
