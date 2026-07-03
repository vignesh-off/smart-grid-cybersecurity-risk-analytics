import pandas as pd
import numpy as np
import uuid
import random
from datetime import datetime, timedelta
import os

# Configuration
NUM_RECORDS = 5000
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2024, 1, 1)

# Categories
REGIONS = ['North', 'South', 'East', 'West', 'Central']
ASSET_TYPES = ['Substation', 'Smart Meter', 'Control Center', 'SCADA System', 'Transmission Line']
ATTACK_TYPES = ['DDoS', 'Ransomware', 'Phishing', 'Malware', 'Insider Threat', 'Man-in-the-Middle']
SEVERITIES = ['Low', 'Medium', 'High', 'Critical']
SEVERITY_WEIGHTS = {'Low': 1, 'Medium': 2, 'High': 3, 'Critical': 4}
MITIGATION_ACTIONS = ['System Isolation', 'Patch Applied', 'Blocked IP', 'Malware Removed', 'Password Reset', 'No Action']
MITIGATION_STATUSES = ['Successful', 'Failed', 'Pending']
ENERGY_SUPPLY_IMPACTS = ['No Impact', 'Minor Disruption', 'Major Outage']

# Pre-generate some assets to ensure repeat attacks
NUM_ASSETS = 500
ASSET_IDS = [f"AST-{str(i).zfill(4)}" for i in range(1, NUM_ASSETS + 1)]

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def generate_data():
    data = []
    
    # Track first attack for cohort analysis
    first_attack = {}

    for _ in range(NUM_RECORDS):
        incident_date = random_date(START_DATE, END_DATE)
        asset_id = random.choice(ASSET_IDS)
        
        if asset_id not in first_attack or incident_date < first_attack[asset_id]:
            first_attack[asset_id] = incident_date

        severity = random.choice(SEVERITIES)
        attack_type = random.choice(ATTACK_TYPES)
        
        mitigation_action = random.choice(MITIGATION_ACTIONS)
        mitigation_status = random.choices(MITIGATION_STATUSES, weights=[70, 20, 10])[0]

        # Correlate response/recovery with severity
        if severity == 'Low':
            resp_hours = round(random.uniform(0.1, 4.0), 1)
            rec_hours = round(random.uniform(0.5, 12.0), 1)
            fin_loss = round(random.uniform(100, 5000), 2)
            impact = 'No Impact'
        elif severity == 'Medium':
            resp_hours = round(random.uniform(1.0, 12.0), 1)
            rec_hours = round(random.uniform(4.0, 48.0), 1)
            fin_loss = round(random.uniform(5000, 25000), 2)
            impact = random.choice(['No Impact', 'Minor Disruption'])
        elif severity == 'High':
            resp_hours = round(random.uniform(4.0, 24.0), 1)
            rec_hours = round(random.uniform(24.0, 120.0), 1)
            fin_loss = round(random.uniform(25000, 150000), 2)
            impact = random.choice(['Minor Disruption', 'Major Outage'])
        else: # Critical
            resp_hours = round(random.uniform(8.0, 72.0), 1)
            rec_hours = round(random.uniform(72.0, 336.0), 1) # up to 2 weeks
            fin_loss = round(random.uniform(150000, 2000000), 2)
            impact = 'Major Outage'

        if mitigation_status == 'Failed':
            fin_loss *= random.uniform(1.2, 1.8)
            rec_hours *= random.uniform(1.2, 1.5)

        # Introduce some anomalies (random very high values)
        if random.random() < 0.05:
            fin_loss *= random.uniform(3.0, 6.0)
            rec_hours *= random.uniform(2.0, 4.0)

        record = {
            'incident_id': str(uuid.uuid4())[:8].upper(),
            'date': incident_date,
            'region': random.choice(REGIONS),
            'asset_id': asset_id,
            'asset_type': random.choice(ASSET_TYPES),
            'attack_type': attack_type,
            'severity': severity,
            'vulnerability_score': random.randint(1, 100),
            'threat_intel_score': random.randint(1, 100),
            'response_time_hours': resp_hours,
            'recovery_time_hours': rec_hours,
            'downtime_hours': round(rec_hours * random.uniform(0.5, 1.0), 1),
            'financial_loss': fin_loss,
            'security_protocol_score': random.randint(1, 100),
            'mitigation_action': mitigation_action,
            'mitigation_status': mitigation_status,
            'energy_supply_impact': impact
        }
        data.append(record)
        
    df = pd.DataFrame(data)
    
    # Sort by date
    df = df.sort_values('date').reset_index(drop=True)
    
    # ---------------- CALCULATED FIELDS ----------------
    
    # Date formatting
    df['month_year'] = df['date'].dt.to_period('M').astype(str)
    
    # Cohort mapping
    df['cohort_month'] = df['asset_id'].map(lambda x: first_attack[x].strftime('%Y-%m'))
    
    # Severity weight
    df['severity_weight'] = df['severity'].map(SEVERITY_WEIGHTS)
    
    # Normalized scores (Min-Max scaling proxy)
    max_downtime = df['downtime_hours'].max()
    df['downtime_score'] = (df['downtime_hours'] / max_downtime) * 100
    
    max_loss = df['financial_loss'].max()
    df['financial_loss_score'] = (df['financial_loss'] / max_loss) * 100
    
    # Risk Score Calculation
    df['risk_score'] = (
        (df['vulnerability_score'] * 0.3) + 
        (df['threat_intel_score'] * 0.3) + 
        ((df['severity_weight'] * 25) * 0.2) + # scale severity 1-4 to 25-100
        (df['financial_loss_score'] * 0.2)
    ).round(2)
    
    # Risk Level
    def get_risk_level(score):
        if score < 40: return 'Low'
        elif score < 70: return 'Medium'
        elif score < 90: return 'High'
        else: return 'Critical'
        
    df['risk_level'] = df['risk_score'].apply(get_risk_level)
    
    # Anomaly Detection Logic
    mean_loss_by_asset = df.groupby('asset_type')['financial_loss'].transform('mean')
    std_loss_by_asset = df.groupby('asset_type')['financial_loss'].transform('std')
    
    # Condition 1: Loss > 3 Std Dev from mean for that asset type
    cond1 = df['financial_loss'] > (mean_loss_by_asset + 3 * std_loss_by_asset)
    
    # Condition 2: Response Time > 48hrs for Critical Severity
    cond2 = (df['severity'] == 'Critical') & (df['response_time_hours'] > 48)
    
    df['anomaly_flag'] = cond1 | cond2
    
    # RFM Scoring Logic (Grouped by Asset)
    # Recency: Days since last attack from max date in dataset
    max_date = df['date'].max()
    rfm_df = df.groupby('asset_id').agg(
        last_attack_date=('date', 'max'),
        rfm_frequency_score=('incident_id', 'count'),
        rfm_magnitude_score=('financial_loss', 'sum')
    ).reset_index()
    
    rfm_df['rfm_recency_days'] = (max_date - rfm_df['last_attack_date']).dt.days
    
    # Invert recency (smaller days = higher risk score 1-5)
    rfm_df['rfm_recency_score'] = pd.qcut(rfm_df['rfm_recency_days'], 5, labels=[5,4,3,2,1], duplicates='drop')
    
    # Frequency & Magnitude (higher = higher risk score 1-5)
    # Using rank to avoid duplicate bin edges in qcut
    rfm_df['rfm_frequency_score'] = pd.qcut(rfm_df['rfm_frequency_score'].rank(method='first'), 5, labels=[1,2,3,4,5])
    rfm_df['rfm_magnitude_score'] = pd.qcut(rfm_df['rfm_magnitude_score'], 5, labels=[1,2,3,4,5])
    
    def segment_asset(row):
        r, f, m = int(row['rfm_recency_score']), int(row['rfm_frequency_score']), int(row['rfm_magnitude_score'])
        if f >= 4 and m >= 4:
            return 'High-Risk Repeat Targets'
        elif f <= 2 and m <= 2:
            return 'Low-Impact Nuisances'
        elif r <= 2 and f >= 4:
            return 'Dormant Threats (Historically frequent)'
        elif m >= 4:
            return 'High-Impact Anomalies'
        else:
            return 'Standard Monitoring'
            
    rfm_df['asset_segment'] = rfm_df.apply(segment_asset, axis=1)
    
    # Merge RFM back to main dataframe
    rfm_df = rfm_df[['asset_id', 'rfm_recency_score', 'rfm_frequency_score', 'rfm_magnitude_score', 'asset_segment']]
    df = df.merge(rfm_df, on='asset_id', how='left')
    
    # Mitigation Effectiveness Score (1-100)
    # Successful mitigation + fast response = high score
    df['mitigation_effectiveness'] = 50 # Base score
    df.loc[df['mitigation_status'] == 'Successful', 'mitigation_effectiveness'] += 30
    df.loc[df['mitigation_status'] == 'Failed', 'mitigation_effectiveness'] -= 30
    
    # Penalize slow response
    max_resp = df['response_time_hours'].max()
    df['mitigation_effectiveness'] += ((1 - (df['response_time_hours'] / max_resp)) * 20)
    df['mitigation_effectiveness'] = df['mitigation_effectiveness'].clip(0, 100).round(2)
    
    return df

if __name__ == "__main__":
    print("Generating Smart Grid Cybersecurity Dataset...")
    df = generate_data()
    
    # Ensure data directory exists
    os.makedirs('../data', exist_ok=True)
    
    output_path = '../data/smart_grid_cybersecurity_data.csv'
    df.to_csv(output_path, index=False)
    
    print(f"Dataset generated successfully with {len(df)} records!")
    print(f"Output saved to: {output_path}")
