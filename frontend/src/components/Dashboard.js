import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PredictionForm from './PredictionForm';
import ChurnRiskChart from './ChurnRiskChart';
import ModelMetrics from './ModelMetrics';
import '../styles/Dashboard.css';

const API_URL = 'http://localhost:5000';

function Dashboard() {
  const [modelInfo, setModelInfo] = useState(null);
  const [modelResults, setModelResults] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [apiStatus, setApiStatus] = useState('checking');

  // Fetch model info and results on component mount
  useEffect(() => {
    fetchModelInfo();
    fetchModelResults();
    checkAPIStatus();
  }, []);

  const checkAPIStatus = async () => {
    try {
      const response = await axios.get(`${API_URL}/health`);
      setApiStatus('connected');
    } catch (err) {
      setApiStatus('disconnected');
      setError('Cannot connect to API. Make sure the Flask server is running on http://localhost:5000');
    }
  };

  const fetchModelInfo = async () => {
    try {
      const response = await axios.get(`${API_URL}/model-info`);
      setModelInfo(response.data.model_info);
    } catch (err) {
      console.error('Error fetching model info:', err);
    }
  };

  const fetchModelResults = async () => {
    try {
      const response = await axios.get(`${API_URL}/model-results`);
      setModelResults(response.data.model_results);
      setLoading(false);
    } catch (err) {
      console.error('Error fetching model results:', err);
      setLoading(false);
    }
  };

  const handlePrediction = (result) => {
    setPrediction(result);
  };

  if (loading) {
    return <div className="loading">Loading dashboard...</div>;
  }

  return (
    <div className="dashboard">
      {/* Header */}
      <header className="dashboard-header">
        <h1>📊 Customer Churn Prediction Dashboard</h1>
        <div className="api-status">
          <span className={`status-indicator ${apiStatus}`}></span>
          {apiStatus === 'connected' ? 'API Connected' : 'API Disconnected'}
        </div>
      </header>

      {/* Error Alert */}
      {error && (
        <div className="alert alert-error">
          ⚠️ {error}
        </div>
      )}

      {/* Main Content */}
      <div className="dashboard-content">
        {/* Left Column - Input */}
        <section className="section input-section">
          <h2>🎯 Predict Churn Risk</h2>
          <PredictionForm onPrediction={handlePrediction} apiUrl={API_URL} />
        </section>

        {/* Middle Column - Prediction Result */}
        {prediction && (
          <section className="section prediction-section">
            <h2>📈 Prediction Result</h2>
            <ChurnRiskChart prediction={prediction} />
          </section>
        )}

        {/* Right Column - Model Metrics */}
        <section className="section metrics-section">
          <h2>🤖 Model Performance</h2>
          <ModelMetrics results={modelResults} />
        </section>
      </div>

      {/* Footer */}
      <footer className="dashboard-footer">
        <p>Customer Churn Prediction & Retention Analytics System v1.0</p>
        {modelInfo && (
          <p>Model: {modelInfo.model_type} | Features: {modelInfo.n_features}</p>
        )}
      </footer>
    </div>
  );
}

export default Dashboard;
