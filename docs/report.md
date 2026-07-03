# Smart Grid Cybersecurity Risk Assessment - Final Technical Report

## 1. Executive Summary & Problem Statement
The objective of this project is to develop an advanced analytics and interactive reporting solution for smart grid infrastructure cybersecurity. Smart grid operators face sophisticated cyber threats. This solution analyzes cyberattack vectors, vulnerable assets, risk levels, mitigation effectiveness, system resilience, and impact on energy supply over a 2-year period, presenting actionable intelligence through a Power BI command center.

## 2. Methodology & ETL
A robust synthetic dataset consisting of 5,000 incident records was generated to represent realistic threat scenarios. The ETL (Extract, Transform, Load) workflow involved:
- **Data Generation:** Pre-computation of complex analytics (RFM scores, risk scoring, standard deviation anomalies) natively in Python to ensure maximum Power BI performance.
- **Power BI Loading:** Direct CSV ingestion.
- **Data Modeling:** Establishment of a Star Schema (`FactCyberIncidents` connecting to `DimDate`, `DimAsset`, `DimAttack`, etc.) supporting advanced DAX calculations.

## 3. Exploratory Data Analysis (EDA)
EDA revealed that highly vulnerable SCADA systems and Control Centers, while less frequently attacked, result in catastrophic downtime and financial loss. Minor disruptions like phishing on smart meters occur at a higher volume but with significantly lower severity. There is a strong negative correlation between response time and mitigation success.

## 4. Asset Risk Segmentation (RFM)
We adapted traditional RFM (Recency, Frequency, Magnitude) modeling to categorize smart grid assets into actionable security segments:
- **Critical Repeat Targets:** Assets with high attack frequency and magnitude, requiring immediate patching.
- **Stable Assets:** Components experiencing rare, low-impact incidents, requiring only standard monitoring cycles.

## 5. Anomaly Detection
Rule-based logic and statistical outlier detection (e.g., financial losses exceeding 3 standard deviations for an asset type, or critical attacks taking >48 hours to respond to) were deployed. Incidents breaking these thresholds are flagged as anomalies for immediate root-cause investigation by the SOC team.

## 6. KPI Monitoring Dashboard
The core Command Center tracks multi-faceted operational health metrics:
- **Volume KPIs:** Total Incidents, Critical Incidents, High Risk Assets.
- **Performance KPIs:** Mitigation Success Rate, Avg Recovery Time.
- **Financial KPIs:** Total Financial Loss, Avg Downtime.
A structured matrix highlights underperforming regions, tracking KPI health against strict benchmarks (e.g., Success Rate < 70% is Critical).

## 7. 90-Day Forecasting
Using historical two-year trend data, Power BI's native forecasting analytics (with 95% confidence intervals) projects upcoming incident volumes and financial losses over a 90-day horizon, supporting proactive resource allocation and readiness.

## 8. Cohort and Repeat Incident Analysis
Advanced retention-style cohort analysis tracks assets based on their first recorded attack month (`cohort_month`). The retention heatmaps reveal whether historical mitigation successfully hardened the asset, or if it continues to experience persistent, repeated attacks.

## 9. Insights and Recommendations
- **Operational Priority:** Immediate incident response optimization is required for Critical severity attacks, as failed mitigations drastically increase financial loss.
- **Asset Hardening:** "Critical Repeat Target" assets must be isolated or patched, as they drive the bulk of grid vulnerability.
- **Predictive Posture:** If the 90-day forecast trends upward, security teams must proactively pre-allocate response resources to regions showing historical anomaly density.

## 10. Limitations
- The accuracy of the 90-day forecast is highly dependent on historical data quality and cannot reliably predict unprecedented "zero-day" exploits.
- Synthetic data, while modeled with realistic correlations, requires validation against live ICS (Industrial Control System) network telemetry before real-world operational deployment.
