import React, { useState } from 'react';
import axios from 'axios';
import '../styles/PredictionForm.css';

function PredictionForm({ onPrediction, apiUrl }) {
  const [formData, setFormData] = useState({
    tenure_months: 12,
    monthly_charges: 65.5,
    total_charges: 786,
    contract_length: 12,
    internet_service: 1,
    phone_service: 1,
    streaming_tv: 0,
    streaming_movies: 0,
    device_protection: 0,
    tech_support: 1,
    online_security: 1,
    backup_service: 0,
    satisfaction_score: 4,
    support_tickets: 2,
    payment_delay: 0
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'number' ? parseFloat(value) : value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(`${apiUrl}/predict`, formData);
      onPrediction(response.data);
    } catch (err) {
      setError('Error making prediction. Please try again.');
      console.error('Prediction error:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadSampleHighRisk = () => {
    setFormData({
      tenure_months: 3,
      monthly_charges: 85.0,
      total_charges: 255,
      contract_length: 6,
      internet_service: 1,
      phone_service: 1,
      streaming_tv: 1,
      streaming_movies: 1,
      device_protection: 1,
      tech_support: 0,
      online_security: 0,
      backup_service: 0,
      satisfaction_score: 2,
      support_tickets: 5,
      payment_delay: 2
    });
  };

  const loadSampleLowRisk = () => {
    setFormData({
      tenure_months: 36,
      monthly_charges: 55.0,
      total_charges: 1980,
      contract_length: 24,
      internet_service: 1,
      phone_service: 1,
      streaming_tv: 0,
      streaming_movies: 0,
      device_protection: 0,
      tech_support: 1,
      online_security: 1,
      backup_service: 1,
      satisfaction_score: 5,
      support_tickets: 1,
      payment_delay: 0
    });
  };

  return (
    <div className="prediction-form">
      {error && <div className="error-message">{error}</div>}

      <div className="form-buttons">
        <button type="button" className="sample-btn high-risk" onClick={loadSampleHighRisk}>
          Load High Risk Sample
        </button>
        <button type="button" className="sample-btn low-risk" onClick={loadSampleLowRisk}>
          Load Low Risk Sample
        </button>
      </div>

      <form onSubmit={handleSubmit}>
        <div className="form-grid">
          {/* Numeric Inputs */}
          <div className="form-group">
            <label>Tenure (months)</label>
            <input
              type="number"
              name="tenure_months"
              value={formData.tenure_months}
              onChange={handleChange}
              min="0"
              max="100"
            />
          </div>

          <div className="form-group">
            <label>Monthly Charges ($)</label>
            <input
              type="number"
              name="monthly_charges"
              value={formData.monthly_charges}
              onChange={handleChange}
              min="0"
              step="0.1"
            />
          </div>

          <div className="form-group">
            <label>Total Charges ($)</label>
            <input
              type="number"
              name="total_charges"
              value={formData.total_charges}
              onChange={handleChange}
              min="0"
              step="0.1"
            />
          </div>

          <div className="form-group">
            <label>Contract Length (months)</label>
            <input
              type="number"
              name="contract_length"
              value={formData.contract_length}
              onChange={handleChange}
              min="0"
              max="60"
            />
          </div>

          <div className="form-group">
            <label>Satisfaction Score (1-5)</label>
            <input
              type="number"
              name="satisfaction_score"
              value={formData.satisfaction_score}
              onChange={handleChange}
              min="1"
              max="5"
            />
          </div>

          <div className="form-group">
            <label>Support Tickets</label>
            <input
              type="number"
              name="support_tickets"
              value={formData.support_tickets}
              onChange={handleChange}
              min="0"
              max="20"
            />
          </div>

          <div className="form-group">
            <label>Payment Delays</label>
            <input
              type="number"
              name="payment_delay"
              value={formData.payment_delay}
              onChange={handleChange}
              min="0"
              max="10"
            />
          </div>

          {/* Binary Inputs */}
          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="internet_service"
                checked={formData.internet_service === 1}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    internet_service: e.target.checked ? 1 : 0
                  })
                }
              />
              Internet Service
            </label>
          </div>

          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="phone_service"
                checked={formData.phone_service === 1}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    phone_service: e.target.checked ? 1 : 0
                  })
                }
              />
              Phone Service
            </label>
          </div>

          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="streaming_tv"
                checked={formData.streaming_tv === 1}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    streaming_tv: e.target.checked ? 1 : 0
                  })
                }
              />
              Streaming TV
            </label>
          </div>

          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="streaming_movies"
                checked={formData.streaming_movies === 1}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    streaming_movies: e.target.checked ? 1 : 0
                  })
                }
              />
              Streaming Movies
            </label>
          </div>

          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="device_protection"
                checked={formData.device_protection === 1}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    device_protection: e.target.checked ? 1 : 0
                  })
                }
              />
              Device Protection
            </label>
          </div>

          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="tech_support"
                checked={formData.tech_support === 1}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    tech_support: e.target.checked ? 1 : 0
                  })
                }
              />
              Tech Support
            </label>
          </div>

          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="online_security"
                checked={formData.online_security === 1}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    online_security: e.target.checked ? 1 : 0
                  })
                }
              />
              Online Security
            </label>
          </div>

          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="backup_service"
                checked={formData.backup_service === 1}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    backup_service: e.target.checked ? 1 : 0
                  })
                }
              />
              Backup Service
            </label>
          </div>
        </div>

        <button
          type="submit"
          className="submit-btn"
          disabled={loading}
        >
          {loading ? 'Predicting...' : '🚀 Predict Churn'}
        </button>
      </form>
    </div>
  );
}

export default PredictionForm;
