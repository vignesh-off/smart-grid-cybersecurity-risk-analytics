# Power BI Data Model: Star Schema Guide

This guide explains how to build a proper star schema in Power BI for the Smart Grid Cybersecurity Risk Assessment project using the generated CSV data.

## 1. Fact Table

**Query Name:** `FactCyberIncidents`

This is your main quantitative table containing all the events and metrics. It should contain the following columns:
- `incident_id`
- `date`
- `asset_id`
- `region`
- `asset_type`
- `attack_type`
- `severity`
- `vulnerability_score`
- `threat_intel_score`
- `response_time_hours`
- `recovery_time_hours`
- `downtime_hours`
- `financial_loss`
- `security_protocol_score`
- `mitigation_action`
- `mitigation_status`
- `energy_supply_impact`
- `risk_score`
- `risk_level`
- `anomaly_flag`
- `asset_segment`
- `month_year`
- `cohort_month`

## 2. Dimension Tables

To create a clean star schema, extract categorical dimensions from the main dataset into distinct tables. In **Power Query Editor**, right-click the `FactCyberIncidents` query and select **Reference**. Then, rename the query, keep only the required columns, and click **Remove Duplicates**.

### DimDate
Create a dedicated Date table (using DAX `CALENDARAUTO()` or Power Query) including:
- `date`
- `year`
- `quarter`
- `month`
- `month_name`
- `month_year`

### DimAsset
- `asset_id`
- `asset_type`
- `region`
- `security_protocol_score`
- `asset_segment`

### DimAttack
- `attack_type`
- `severity`
- `severity_weight`

### DimMitigation
- `mitigation_action`
- `mitigation_status`
- `mitigation_effectiveness`

### DimRisk
- `risk_level`
- `risk_score band`
- `anomaly_flag`

## 3. Relationships

In Power BI's **Model View**, connect your dimension tables to the `FactCyberIncidents` table. 

Ensure the following relationships are established as **One-to-Many (*:1)** with a **Single cross filter direction**:
- `DimDate[date]` → `FactCyberIncidents[date]`
- `DimAsset[asset_id]` → `FactCyberIncidents[asset_id]`
- `DimAttack[attack_type]` → `FactCyberIncidents[attack_type]`
- `DimMitigation[mitigation_action]` → `FactCyberIncidents[mitigation_action]`
- `DimRisk[risk_level]` → `FactCyberIncidents[risk_level]`

## 4. Power Query Steps

Follow these steps step-by-step to implement the model:
1. **Load CSV:** Get Data -> Text/CSV -> select `data/smart_grid_cybersecurity_data.csv`. Click **Transform Data**.
2. **Rename query:** Rename the imported query to `FactCyberIncidents`.
3. **Set correct data types:** Ensure all numeric values are decimals/whole numbers and dates are properly formatted (see section 5).
4. **Create reference queries:** Right-click `FactCyberIncidents` -> Reference. Name the new query (e.g., `DimAsset`).
5. **Remove duplicate rows:** Select only the columns needed for that dimension (e.g., `asset_id`, `asset_type`, `region`), right-click the headers -> **Remove Other Columns**. Then select all columns, right-click -> **Remove Duplicates**.
6. **Create date table:** Build `DimDate` either by referencing `FactCyberIncidents` and extracting dates, or create it natively via DAX after loading.
7. **Close & Apply:** Click "Close & Apply" to load the tables into the Model View and set up relationships.

## 5. Data Types

Ensure the following data types are set in Power Query prior to applying:
- **`date`**: Date
- **`incident_id`, `asset_id`**: Text
- **`scores`**: Decimal Number (or Whole Number)
- **`hours`**: Decimal Number
- **`financial_loss`**: Decimal Number
- **categorical fields**: Text

## 6. Validation Checklist

Use this checklist to ensure your model is robust:
- [ ] No blank values
- [ ] Relationship lines active
- [ ] Date table marked as date table
- [ ] Numeric fields summarized correctly
- [ ] Slicers work across all visuals
- [ ] Fact table row count remains 5000
