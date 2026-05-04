import pandas as pd
import numpy as np
from sklearn.datasets import make_classification

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic customer churn data
n_samples = 1000
features, target = make_classification(
    n_samples=n_samples,
    n_features=15,
    n_informative=10,
    n_redundant=5,
    random_state=42,
    weights=[0.7, 0.3]  # 70% no churn, 30% churn
)

# Create customer IDs
customer_ids = np.arange(1001, 1001 + n_samples)

# Create DataFrame with meaningful column names
data = pd.DataFrame(features, columns=[
    'tenure_months', 'monthly_charges', 'total_charges', 'contract_length',
    'internet_service', 'phone_service', 'streaming_tv', 'streaming_movies',
    'device_protection', 'tech_support', 'online_security', 'backup_service',
    'satisfaction_score', 'support_tickets', 'payment_delay'
])

# Add customer_id and churn columns
data.insert(0, 'customer_id', customer_ids)
data['churn'] = target

# Normalize some columns to be more realistic
data['tenure_months'] = np.abs(np.round(data['tenure_months'] * 20 + 12)).astype(int)
data['monthly_charges'] = np.abs(data['monthly_charges'] * 30 + 50)
data['total_charges'] = data['tenure_months'] * data['monthly_charges']
data['contract_length'] = np.abs(np.round(data['contract_length'] * 24 + 12)).astype(int)
data['satisfaction_score'] = np.clip(np.round(data['satisfaction_score'] * 2 + 3), 1, 5).astype(int)
data['support_tickets'] = np.abs(np.round(data['support_tickets'] * 5)).astype(int)
data['payment_delay'] = np.abs(np.round(data['payment_delay'] * 10)).astype(int)

# Convert binary features to 0/1
for col in ['internet_service', 'phone_service', 'streaming_tv', 'streaming_movies',
            'device_protection', 'tech_support', 'online_security', 'backup_service']:
    data[col] = (data[col] > 0).astype(int)

# Save dataset
data.to_csv('../data/customer_churn.csv', index=False)
print(f"Dataset created with shape: {data.shape}")
print(f"\nFirst few rows:\n{data.head()}")
print(f"\nChurn distribution:\n{data['churn'].value_counts()}")
print(f"\nChurn rate: {data['churn'].mean():.2%}")
