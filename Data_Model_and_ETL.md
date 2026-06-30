# Data Model and ETL Plan

## ETL Workflow

1. Load `Master Energy_Utilities_Data.xlsx`.
2. Inspect all sheets and identify fact and dimension columns.
3. Rename columns using snake case or clean business names.
4. Remove duplicates.
5. Convert all date fields.
6. Standardize categorical values.
7. Fill missing values carefully.
8. Create calculated columns.
9. Split into fact and dimension tables.
10. Load to Power BI/Tableau or export cleaned CSV files.

## Suggested Star Schema

### FactCyberEvents

- incident_id
- asset_id
- date_id
- threat_id
- region_id
- mitigation_id
- risk_score
- severity
- downtime_hours
- response_time_hours
- recovery_time_hours
- estimated_loss
- incident_count

### DimDate

- date_id
- date
- day
- month
- month_name
- quarter
- year

### DimAsset

- asset_id
- asset_name
- asset_type
- asset_criticality
- owner_department

### DimThreat

- threat_id
- threat_type
- attack_vector
- source_type

### DimRegion

- region_id
- region
- grid_zone
- state
- country

### DimMitigation

- mitigation_id
- mitigation_status
- control_type
- detection_date
- closure_date

## Data Quality Rules

- `incident_id` should be unique.
- `risk_score` should be numeric and within a defined range, usually 0 to 100.
- `severity` should use consistent categories: Low, Medium, High, Critical.
- Date fields should not be in the future unless representing forecasts.
- Closed incidents should have a closure date.
- Response and recovery time should not be negative.

## Useful Calculated Columns

- `incident_month`
- `days_since_last_incident`
- `is_critical`
- `is_open`
- `sla_breach`
- `risk_band`
- `anomaly_flag`
- `repeat_incident_flag`
