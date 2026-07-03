# Dashboard Page Plan

This document outlines the layout, visuals, and purpose of the 7 Power BI dashboard pages.

## Page 1: Executive Cybersecurity Command Center
**Purpose:** High-level overview for CISO and executive stakeholders.
- **KPI Cards:** 
  - Total Incidents (Count of incident_id)
  - Total Financial Loss (Sum of financial_loss)
  - Avg Downtime Hours (Average of downtime_hours)
  - Critical Risk Incidents (Count where risk_level = 'Critical')
- **Visual 1 (Map):** Incidents by Region. Size = Total Loss, Color = Avg Risk Score.
- **Visual 2 (Line Chart):** Incidents over Time (Month-Year) grouped by Severity.
- **Visual 3 (Bar Chart):** Top 5 Most Targeted Asset Types.

## Page 2: EDA and Incident Pattern Analysis
**Purpose:** Deep dive into the distribution of attacks.
- **Visual 1 (Donut Chart):** Attack Types breakdown.
- **Visual 2 (100% Stacked Bar):** Energy Supply Impact by Attack Type.
- **Visual 3 (Scatter Plot):** Vulnerability Score (X) vs. Threat Intel Score (Y), bubble size = Financial Loss.

## Page 3: Asset Risk Segmentation (RFM)
**Purpose:** Identify which assets need immediate intervention based on Recency, Frequency, and Magnitude of attacks.
- **Visual 1 (Matrix):** Rows = `asset_segment`, Values = Count of Assets, Avg Financial Loss, Avg Downtime.
- **Visual 2 (Scatter Plot):** RFM Frequency (X) vs RFM Magnitude (Y).
- **Visual 3 (Table):** Action List filtering only for 'High-Risk Repeat Targets', showing Asset ID, Asset Type, and Total Loss.

## Page 4: Anomaly Detection and Suspicious Activity Flagging
**Purpose:** Highlight extreme outliers.
- **Visual 1 (Card):** Total Anomalies Detected (`anomaly_flag = True`).
- **Visual 2 (Line Chart with Error Bands):** Daily Average Financial Loss. Highlight points that break the upper control limit.
- **Visual 3 (Table):** Detailed list of anomalous incidents, showing Incident ID, Date, Asset Type, Financial Loss, and Response Time.

## Page 5: KPI Monitoring Dashboard
**Purpose:** Evaluate the performance of the response team.
- **Visual 1 (Gauge):** Average Mitigation Effectiveness Score.
- **Visual 2 (Clustered Column Chart):** Avg Response Time vs. Avg Recovery Time by Asset Type.
- **Visual 3 (Funnel Chart):** Mitigation Status (Successful, Pending, Failed) count.

## Page 6: 90-Day Forecasting Dashboard
**Purpose:** Predictive insights for resource allocation.
- **Visual 1 (Line Chart with Forecast):** Total Incidents over Time. Utilize Power BI's Analytics pane to add a Forecast (90 periods, standard seasonality).
- **Visual 2 (Line Chart with Forecast):** Total Financial Loss over Time with Forecast.

## Page 7: Cohort and Repeat Incident Analysis
**Purpose:** Understand long-term vulnerability of breached assets.
- **Visual 1 (Matrix - Heatmap):** 
  - Rows: `cohort_month`
  - Columns: Months since first attack (requires DAX calculated column for DateDiff between `cohort_month` and incident `date`).
  - Values: Count of repeat attacks or percentage of cohort attacked again.
