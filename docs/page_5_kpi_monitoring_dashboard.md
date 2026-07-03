# Page 5: KPI Monitoring Dashboard

## 1. Page Objective
This page monitors operational and strategic cybersecurity KPIs such as response speed, recovery performance, downtime, financial loss, mitigation success, anomaly rate, and risk exposure. It serves as a central Command Center dashboard where stakeholders can quickly assess the overall health, resilience, and defensive posture of the smart grid infrastructure.

## 2. KPI Categories
Organize the KPIs into the following distinct logical groups on the dashboard:

**A. Incident Volume KPIs**
- Total Incidents
- Critical Incidents
- High Risk Assets
- Anomaly Count

**B. Operational Resilience KPIs**
- Avg Downtime
- Total Downtime
- Avg Recovery Time
- Total Recovery Time

**C. Financial Impact KPIs**
- Total Financial Loss
- Average Financial Loss

**D. Security Performance KPIs**
- Mitigation Success Rate
- Failed Mitigation Count
- Anomaly Rate
- Risk Score

**E. Threat Intelligence KPIs**
- Avg Vulnerability Score
- Avg Threat Intel Score

## 3. Page Layout
Design a professional KPI monitoring dashboard utilizing the following structure:
- **Header Title:** Top-center (e.g., "Cybersecurity KPI Command Center").
- **KPI Category Card Groups:** A structured grid at the top of the canvas grouping cards by the categories listed above.
- **Gauge Visuals:** Positioned below the cards to track target-oriented rates and scores (e.g., Mitigation Success).
- **Trend Visuals:** Middle canvas dedicated to line and combo charts tracking KPIs over time.
- **Comparison Charts:** Middle-lower canvas for categorizing operational failures by asset and attack type.
- **KPI Health Table:** Bottom section featuring a comprehensive matrix evaluating KPI health across regions.
- **Slicer Panel:** Left-hand pane for detailed metric slicing.
- **Insight/Recommendation Box:** Top right or near the KPI Health Table for actionable summaries.

## 4. Visuals Required
Add these visuals to the canvas with the exact configurations below:

### A. KPI Card Grid
- **Display:** All key KPI measures outlined in Section 2, cleanly grouped by category.

### B. Gauge
- **Title:** Mitigation Success Rate
- **Value:** Mitigation Success Rate
- **Target:** 85%

### C. Gauge
- **Title:** Average Risk Score
- **Value:** Risk Score
- **Target/Threshold:** 45 or lower

### D. Line Chart
- **Title:** KPI Trend - Incidents and Anomalies Over Time
- **Axis:** `month_year` or `date`
- **Values:** Total Incidents, Anomaly Count

### E. Combo Chart
- **Title:** Financial Loss and Downtime Over Time
- **Axis:** `month_year`
- **Column Values:** Total Financial Loss
- **Line Values:** Avg Downtime

### F. Bar Chart
- **Title:** Average Recovery Time by Asset Type
- **Axis:** `asset_type`
- **Values:** Avg Recovery Time

### G. Column Chart
- **Title:** Failed Mitigation Count by Attack Type
- **Axis:** `attack_type`
- **Values:** Failed Mitigation Count

### H. Matrix/Table
- **Title:** KPI Health by Region
- **Rows:** `region`
- **Columns/Measures:** Total Incidents, Critical Incidents, High Risk Assets, Avg Downtime, Total Financial Loss, Mitigation Success Rate, Risk Score, Anomaly Rate

## 5. KPI Health Rules
Implement and document the following KPI status logic across visual tooltips and matrix conditional formatting:
- **Mitigation Success Rate:**
  - `>= 85%` = Healthy (Green)
  - `70% - 84%` = Warning (Yellow/Orange)
  - `< 70%` = Critical (Red)
- **Risk Score:**
  - `<= 45` = Healthy (Green)
  - `46 - 70` = Warning (Yellow/Orange)
  - `> 70` = Critical (Red)
- **Anomaly Rate:**
  - `<= 10%` = Healthy (Green)
  - `11% - 20%` = Warning (Yellow/Orange)
  - `> 20%` = Critical (Red)

## 6. Conditional Formatting
Apply strict conditional formatting based on the rules above:
- **Mitigation Success Rate, Risk Score, Anomaly Rate:** Apply background/font color rules in the KPI Matrix and Gauge charts using the precise thresholds defined in Section 5.
- **Total Financial Loss, Avg Downtime, Failed Mitigation Count:** Apply data bars within the matrix to instantly highlight the regions generating the highest operational friction and financial damage.

## 7. Slicers
Add the following slicers to the Slicer Panel:
- Date Range
- Region
- Asset Type
- Attack Type
- Severity
- Risk Level
- Mitigation Status

## 8. Business Questions Answered
This dashboard is explicitly structured to answer the following business questions:
- **Is the cybersecurity response process improving?** *(Answered by Gauge B and Combo Chart E)*
- **Which regions have poor KPI health?** *(Answered by Matrix H)*
- **Are anomalies increasing?** *(Answered by Line Chart D)*
- **Are financial losses and downtime reducing?** *(Answered by Combo Chart E)*
- **Is mitigation success meeting the target?** *(Answered by Gauge B)*
- **Which asset types need operational improvement?** *(Answered by Bar Chart F)*

## 9. Recommendation Box
Insert a Text Box onto the dashboard with the following template:
> "Regions or asset types with low mitigation success, high anomaly rate, and high average risk score should be prioritized for operational improvement, faster response, and protocol hardening."

## 10. Viva Explanation
*Use this explanation during presentations or project vivas:*
> "This page monitors cybersecurity KPIs like mitigation success rate, downtime, recovery time, financial loss, anomaly rate, and risk score. It works as a command center for operational and strategic decision-making."
