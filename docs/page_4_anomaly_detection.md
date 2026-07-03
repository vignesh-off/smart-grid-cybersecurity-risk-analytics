# Page 4: Anomaly Detection and Suspicious Activity Flagging

## 1. Page Objective
This page highlights abnormal cybersecurity incidents that require immediate investigation. By surfacing events with unusually high financial loss, high downtime, repeated attacks, failed mitigations, or critical severity, it empowers the security operations team to quickly identify and investigate outliers before they severely impact grid reliability.

## 2. Anomaly Logic Explanation
The anomaly detection engine relies on a combination of rule-based flagging and statistical outlier detection based on strict cybersecurity risk thresholds. Examples of logic driving these flags include:
- **Statistical Outliers:** `financial_loss` or `downtime_hours` exceeding the 95th percentile (e.g., > 3 standard deviations from the mean for that asset type).
- **Risk Thresholds:** Incidents resulting in a `risk_score` >= 75.
- **Rule-Based Flagging:** Events where `severity` = Critical AND `mitigation_status` = Failed.
- **Behavioral Anomalies:** Repeated incidents on the exact same asset within a short window, or combinations of a high `vulnerability_score` paired with a high `threat_intel_score`.

## 3. Page Layout
Design a professional Power BI layout optimized for incident investigation:
- **Header Title:** Top-center (e.g., "Anomaly Detection & Suspicious Activity").
- **Slicer Panel:** Left-hand pane for focused filtering.
- **Anomaly KPI Cards:** A row immediately below the header summarizing the scale of anomalous events.
- **Anomaly Trend Visual:** A line chart spanning the top of the canvas tracking anomalies over time.
- **Suspicious Incident Distribution Visuals:** Middle canvas containing donut, bar, and column charts breaking down anomalies by attack type and mitigation status.
- **Financial/Downtime Map:** A scatter plot visualizing the exact intersection of downtime and financial loss.
- **High-Risk Anomaly Table / Root-Cause Section:** Bottom canvas dedicated to an exhaustive table of suspicious incidents for root-cause investigation.
- **Insight/Recommendation Box:** Top right or near the table to guide analyst workflow.

## 4. KPI Cards
Use the following DAX measures to build the anomaly KPI row:

| KPI Card | Measure Name | Display Format | Cybersecurity Meaning |
|---|---|---|---|
| **Anomaly Count** | Anomaly Count | Whole Number | Total number of incidents flagged as suspicious. |
| **Anomaly Rate** | Anomaly Rate | Percentage | Proportion of total incidents classified as anomalies. |
| **Critical Incidents** | Critical Incidents | Whole Number | Volume of the most severe attacks. |
| **Failed Mitigation Count** | Failed Mitigation Count | Whole Number | Number of incidents where defensive measures failed. |
| **Total Financial Loss** | Total Financial Loss | Currency | Total economic damage from the selected incidents. |
| **Avg Downtime** | Avg Downtime | Decimal Number, 2 decimals | Average operational offline hours. |
| **Risk Score** | Risk Score | Decimal Number, 2 decimals | Average composite risk of the selected incidents. |
| **High Risk Assets** | High Risk Assets | Whole Number | Count of specific assets targeted by these anomalies. |

## 5. Visuals Required
Add these visuals to the canvas with the exact configurations below:

### A. Donut Chart
- **Title:** Anomaly vs Normal Incident Distribution
- **Legend:** `anomaly_flag`
- **Values:** Count of `incident_id`

### B. Line Chart
- **Title:** Monthly Anomaly Trend
- **Axis:** `month_year` or `date`
- **Values:** Anomaly Count
- **Legend:** `severity`

### C. Bar Chart
- **Title:** Anomalies by Attack Type
- **Axis:** `attack_type`
- **Values:** Anomaly Count

### D. Column Chart
- **Title:** Failed Mitigation Incidents by Severity
- **Axis:** `severity`
- **Values:** Failed Mitigation Count

### E. Scatter Plot
- **Title:** Financial Loss vs Downtime Anomaly Map
- **X-axis:** `downtime_hours`
- **Y-axis:** `financial_loss`
- **Size:** `risk_score`
- **Legend:** `anomaly_flag`
- **Tooltip:** `incident_id`, `asset_id`, `attack_type`, `severity`, `risk_score`, `mitigation_status`

### F. Treemap
- **Title:** Regional Anomaly Impact
- **Group:** `region`
- **Details:** `asset_type`
- **Values:** Total Financial Loss (or Anomaly Count)

### G. Table
- **Title:** Suspicious Incident Investigation Table
- **Columns:** `incident_id`, `date`, `asset_id`, `region`, `asset_type`, `attack_type`, `severity`, `downtime_hours`, `financial_loss`, `risk_score`, `risk_level`, `mitigation_status`, `anomaly_flag`
- **Filter:** Set a visual-level filter where `anomaly_flag` = `TRUE()` (or `"Anomaly"`).
- **Sort by:** `risk_score` descending or `financial_loss` descending.

## 6. Slicers
Add the following slicers to the Slicer Panel:
- Date Range
- Region
- Asset Type
- Attack Type
- Severity
- Risk Level
- Mitigation Status
- Anomaly Flag

## 7. Investigation Questions Answered
This dashboard is structured to answer critical investigation questions:
- **Which incidents are abnormal?** *(Answered by Table G and Scatter Plot E)*
- **Which attack types create most anomalies?** *(Answered by Bar Chart C)*
- **Which regions have highest anomaly impact?** *(Answered by Treemap F)*
- **Are anomalies increasing over time?** *(Answered by Line Chart B)*
- **Are failed mitigations linked with abnormal losses?** *(Answered by Column Chart D and Scatter Plot E)*
- **Which incidents should security teams investigate first?** *(Answered by Table G sorting)*

## 8. Recommendation Box
Insert a Text Box onto the dashboard with the following template:
> "Anomalous incidents should be escalated for root-cause analysis. Priority should be given to critical severity, failed mitigation, high financial loss, and high downtime events."

## 9. Viva Explanation
*Use this explanation during presentations or project vivas:*
> "This page uses rule-based and statistical anomaly detection to flag suspicious cybersecurity incidents. It helps security teams investigate abnormal events before they affect grid reliability."
