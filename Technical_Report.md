# Technical Report: Smart Grid Cybersecurity Risk Assessment and Mitigation

## 1. Problem Understanding

The project asks for an analytics solution for the Energy & Utilities domain. The main objective is to analyse cybersecurity vulnerabilities in smart grid infrastructure and build interactive reports that help decision-makers monitor risks, detect anomalies, evaluate mitigation effectiveness, and forecast future cyber-risk trends.

The analysis should answer:

- Which smart grid assets, regions, or systems are most exposed to cyber risk?
- Which cyberattack vectors are most frequent and most severe?
- How resilient is the grid against incidents?
- Which incidents or patterns look suspicious or abnormal?
- Are mitigation actions reducing future risk?
- What future trend is expected based on historical cybersecurity data?

## 2. Tools Recommended

- Excel Power Query for ETL and initial cleaning.
- Power BI or Tableau for dashboard development.
- Python for EDA, anomaly detection, segmentation, forecasting, and cohort analysis.
- SQL for repeatable KPI and aggregation queries.

## 3. Data Preparation

Expected dataset: `Master Energy_Utilities_Data.xlsx`.

Cleaning steps:

1. Import all relevant sheets.
2. Standardize column names.
3. Remove duplicate incident or asset records.
4. Convert date columns into proper date format.
5. Standardize region, asset type, severity, threat category, and mitigation status values.
6. Handle missing values:
   - Categorical fields: replace with `Unknown`.
   - Numeric fields: use median or domain-specific value.
   - Date fields: investigate before filling.
7. Create calculated fields:
   - Risk level.
   - Response time.
   - Recovery time.
   - Mitigation age.
   - Incident month.
   - Asset risk score.

## 4. Data Model

Use a star schema:

- FactCyberEvents: incident ID, asset ID, date ID, threat ID, region ID, risk score, severity, downtime, response time, recovery cost, mitigation status.
- DimDate: date, month, quarter, year.
- DimAsset: asset ID, asset type, asset criticality, owner, location.
- DimThreat: threat type, attack vector, malware/ransomware/phishing category if available.
- DimRegion: region, grid zone, country/state.
- DimMitigation: mitigation status, control type, closure date.

## 5. Exploratory Data Analysis

Perform EDA to understand:

- Total incident volume over time.
- Risk score distribution.
- Severity distribution.
- Most affected asset types.
- Highest-risk regions.
- Most common threat vectors.
- Relationship between risk score, downtime, and response time.
- Outliers in impact, frequency, downtime, and recovery cost.

Suggested charts:

- Monthly incident trend.
- Severity breakdown.
- Top 10 high-risk assets.
- Threat vector bar chart.
- Region-wise heat map.
- Box plot of response time by severity.
- Scatter plot: risk score vs downtime.

## 6. Segmentation

Segment assets using an RFM-style cybersecurity model:

- Recency: days since last incident.
- Frequency: number of incidents per asset.
- Magnitude: average or total risk impact.

Suggested asset groups:

- Critical High-Risk Assets: recent, frequent, high impact.
- Frequently Targeted Assets: high frequency but medium impact.
- High-Impact Rare Events: low frequency but severe incidents.
- Stable Assets: old or no recent incident, low frequency, low impact.
- Recently Compromised Assets: recent incident requiring active monitoring.

## 7. KPI Monitoring

Recommended KPIs:

- Total incidents.
- Critical incidents.
- Average risk score.
- Open vulnerabilities.
- Mitigation completion rate.
- Average response time.
- Average recovery time.
- Mean time to detect.
- Mean time to resolve.
- High-risk asset count.
- Repeat-incident asset count.
- Top threat vector.

## 8. Anomaly Detection

Use both rule-based and statistical detection.

Rule-based flags:

- Risk score >= 80.
- Severity = Critical.
- Response time above SLA.
- Recovery time above SLA.
- Same asset attacked repeatedly in a short period.
- Incident count spike by region or threat type.

Statistical flags:

- Incident frequency greater than mean + 2 standard deviations.
- Risk score greater than upper IQR threshold.
- Downtime greater than upper IQR threshold.
- Monthly incident volume outside expected rolling range.

## 9. Forecasting

Use historical incident or risk data to forecast future trends.

Forecasting target options:

- Monthly cyber incidents.
- Average monthly risk score.
- Critical vulnerability count.
- Downtime hours.

Recommended methods:

- Power BI built-in line chart forecasting.
- Python exponential smoothing for quick forecasting.
- ARIMA or Prophet if the dataset is sufficiently large.

Output should include future values with confidence intervals.

## 10. Cohort / Retention Analysis

Create cohorts by first incident month or first vulnerability detection month.

Track:

- Whether assets continue to experience incidents after mitigation.
- Repeat incident rate by cohort.
- Reduction in risk after mitigation.
- Long-term behaviour of vulnerable asset groups.

This helps prove whether mitigation actions are effective.

## 11. Dashboard Solution

Create a command-center dashboard with these pages:

1. Executive Overview.
2. Risk and Vulnerability Trends.
3. Asset and Region Risk.
4. Threat Vector Analysis.
5. Anomaly Detection.
6. Mitigation Performance.
7. Forecasting.
8. Cohort and Retention Analysis.

## 12. Business Recommendations

- Prioritize mitigation for assets with high frequency and high impact.
- Monitor regions with repeated high-severity incidents.
- Strengthen controls against the most common attack vectors.
- Reduce response and recovery time through SLA monitoring.
- Use anomaly alerts to catch unusual attack patterns early.
- Review mitigation effectiveness monthly using cohort trends.
- Allocate cybersecurity budget based on risk score, asset criticality, and forecasted exposure.

## 13. Final Deliverables

The submission should include:

- Cleaned and processed dataset.
- Technical report.
- Dashboard screenshots or interactive dashboard file.
- Python, SQL, Power Query, or Power BI scripts.
- Summary of insights and recommendations.
