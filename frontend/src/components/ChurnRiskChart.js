import React from 'react';
import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import '../styles/ChurnRiskChart.css';

function ChurnRiskChart({ prediction }) {
  if (!prediction || prediction.status !== 'success') {
    return <div className="no-prediction">No prediction yet</div>;
  }

  const data = [
    {
      name: 'Probability',
      'No Churn': prediction.no_churn_probability * 100,
      'Churn': prediction.churn_probability * 100
    }
  ];

  const getRiskColor = (riskLevel) => {
    switch (riskLevel) {
      case 'HIGH':
        return '#e74c3c';
      case 'MEDIUM':
        return '#f39c12';
      case 'LOW':
        return '#27ae60';
      default:
        return '#3498db';
    }
  };

  return (
    <div className="churn-risk-chart">
      <div className="prediction-summary">
        <div className="risk-indicator">
          <div
            className={`risk-badge ${prediction.risk_level.toLowerCase()}`}
            style={{ backgroundColor: getRiskColor(prediction.risk_level) }}
          >
            {prediction.risk_level} RISK
          </div>
        </div>

        <div className="prediction-details">
          <div className="detail-item">
            <span className="label">Churn Probability:</span>
            <span className="value">{(prediction.churn_probability * 100).toFixed(2)}%</span>
          </div>
          <div className="detail-item">
            <span className="label">No Churn Probability:</span>
            <span className="value">{(prediction.no_churn_probability * 100).toFixed(2)}%</span>
          </div>
          <div className="detail-item">
            <span className="label">Prediction:</span>
            <span className="value">
              {prediction.prediction === 1 ? '⚠️ Will Churn' : '✓ Will Not Churn'}
            </span>
          </div>
        </div>
      </div>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip formatter={(value) => `${value.toFixed(2)}%`} />
          <Legend />
          <Bar dataKey="No Churn" fill="#27ae60" />
          <Bar dataKey="Churn" fill="#e74c3c" />
        </BarChart>
      </ResponsiveContainer>

      <div className="recommendation">
        {prediction.risk_level === 'HIGH' && (
          <p>⚠️ <strong>Recommendation:</strong> Initiate retention strategy immediately. Consider personalized offers or outreach.</p>
        )}
        {prediction.risk_level === 'MEDIUM' && (
          <p>📋 <strong>Recommendation:</strong> Monitor customer closely. Prepare retention initiatives if engagement decreases.</p>
        )}
        {prediction.risk_level === 'LOW' && (
          <p>✅ <strong>Recommendation:</strong> Customer appears satisfied. Continue standard service delivery.</p>
        )}
      </div>
    </div>
  );
}

export default ChurnRiskChart;
