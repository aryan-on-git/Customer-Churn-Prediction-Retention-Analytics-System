import React from 'react';
import '../styles/ModelMetrics.css';

function ModelMetrics({ results }) {
  if (!results) {
    return <div className="no-metrics">Loading model metrics...</div>;
  }

  const metrics = Object.entries(results);

  return (
    <div className="model-metrics">
      <div className="metrics-grid">
        {metrics.map(([modelName, data]) => (
          <div key={modelName} className="metric-card">
            <h3>{modelName}</h3>
            <div className="metric-item">
              <span className="metric-label">Accuracy:</span>
              <span className="metric-value">{(data.accuracy * 100).toFixed(2)}%</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">Precision:</span>
              <span className="metric-value">{(data.precision * 100).toFixed(2)}%</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">Recall:</span>
              <span className="metric-value">{(data.recall * 100).toFixed(2)}%</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">F1-Score:</span>
              <span className="metric-value">{(data.f1_score * 100).toFixed(2)}%</span>
            </div>
            <div className="metric-item highlight">
              <span className="metric-label">ROC-AUC:</span>
              <span className="metric-value">{(data.roc_auc * 100).toFixed(2)}%</span>
            </div>
          </div>
        ))}
      </div>

      <div className="metrics-info">
        <h4>📊 Metrics Explanation</h4>
        <ul>
          <li><strong>Accuracy:</strong> Overall correctness of predictions</li>
          <li><strong>Precision:</strong> Correctness of positive predictions</li>
          <li><strong>Recall:</strong> Coverage of actual positive cases</li>
          <li><strong>F1-Score:</strong> Harmonic mean of precision and recall</li>
          <li><strong>ROC-AUC:</strong> Model's ability to distinguish between classes</li>
        </ul>
      </div>
    </div>
  );
}

export default ModelMetrics;
