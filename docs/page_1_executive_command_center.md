# Page 1: Executive Cybersecurity Command Center

## 1. Page Objective
This page acts as the main overview dashboard for the Smart Grid Cybersecurity Risk Assessment and Mitigation project. It gives management and CISO-level stakeholders a high-level overview of cybersecurity incidents, risk exposure, mitigation performance, and operational impact on the smart grid infrastructure.

## 2. Page Layout
Design a professional, grid-based Power BI layout utilizing a dark theme (resembling a SOC environment) structured as follows:
- **Header Title:** Top-center (e.g., "Smart Grid Cybersecurity Command Center").
- **Slicer Panel:** A vertical pane on the left or horizontal pane under the header.
- **KPI Card Row:** A prominent horizontal row below the header displaying the top-level metrics.
- **Main Visual Section:** The central canvas dedicated to key charts (trends, regions, asset types).
- **Risk and Impact Section:** Lower canvas dedicated to high-risk asset tables and deeper analytical visuals.
- **Insight / Recommendation Text Box:** Positioned strategically on the canvas to highlight actionable takeaways.

## 3. KPI Cards
Populate the KPI row using the following DAX measures:

| KPI Card | Measure Name | Display Format | Business Meaning |
|---|---|---|---|
| **Total Incidents** | Total Incidents | Whole Number | Total volume of cyber attacks across the grid. |
| **High Risk Assets** | High Risk Assets | Whole Number | Count of unique assets identified as high-risk targets. |
| **Critical Incidents** | Critical Incidents | Whole Number | Attacks classified as 'Critical' severity. |
| **Avg Downtime** | Avg Downtime | Decimal Number, 2 decimals | Average hours grid components are offline per incident. |
| **Avg Recovery Time** | Avg Recovery Time | Decimal Number, 2 decimals | Average hours taken to fully recover from an incident. |
| **Total Financial Loss** | Total Financial Loss | Currency | Estimated financial damage caused by breaches. |
| **Mitigation Success Rate** | Mitigation Success Rate | Percentage | Percentage of threats successfully neutralized. |
| **Anomaly Count** | Anomaly Count | Whole Number | Number of highly unusual or anomalous incidents detected. |

## 4. Visuals Required
Add these visuals to the canvas with the exact configurations below:

### A. Donut Chart
- **Title:** Risk Level Distribution
- **Legend:** `risk_level`
- **Values:** Count of `incident_id`

### B. Bar Chart
- **Title:** Incidents by Region
- **Axis:** `region`
- **Values:** Total Incidents

### C. Column Chart
- **Title:** Attack Type Distribution
- **Axis:** `attack_type`
- **Values:** Total Incidents

### D. Treemap
- **Title:** Risk Exposure by Asset Type
- **Group:** `asset_type`
- **Values:** Average `risk_score` (or the `Risk Score` DAX Measure)

### E. Line Chart
- **Title:** Monthly Incident Trend
- **Axis:** `month_year` or `date`
- **Values:** Monthly Incident Count

### F. Table
- **Title:** Top 10 High Risk Assets
- **Columns:** `asset_id`, `asset_type`, `region`, `risk_score`, `risk_level`, `financial_loss`, `mitigation_status`
- **Note:** Sort by `risk_score` descending to rank the most at-risk assets at the top.

## 5. Slicers
Add the following slicers to the Slicer Panel to allow deep-dive filtering:
- Date range
- Region
- Asset Type
- Attack Type
- Severity
- Risk Level
- Mitigation Status

## 6. Interaction Rules
Configure the visual interactions as follows:
- **Global Slicers:** Slicers must affect all visuals on the page.
- **Cross-Filtering:** The Risk Level donut chart should explicitly cross-filter other visuals when clicked.
- **Responsive Tables:** The Top 10 table must dynamically respond to region and date filters.
- **Data Model Integrity:** Ensure you use single-direction filtering from your dimension tables to the `FactCyberIncidents` fact table.

## 7. Conditional Formatting
Apply conditional formatting to enhance readability:
- **`risk_level`:** Color code Background/Font (High/Critical = Red, Medium = Orange/Yellow, Low = Green).
- **`anomaly_flag`:** Highlight anomaly rows with icons or distinct background colors.
- **`financial_loss`:** Ensure currency formatting.
- **`mitigation_success_rate`:** Ensure percentage formatting.

## 8. Insight Box
Insert a Text Box onto the dashboard with the following actionable template:
> "Current cybersecurity risk is mainly concentrated in [region/asset type]. High-risk assets require immediate patching, improved monitoring, and faster mitigation response. Failed mitigation incidents show higher downtime and financial loss."

## 9. Viva Explanation
*Use this short explanation when presenting the dashboard:*
> "This page acts as an executive command center. It summarizes total incidents, high-risk assets, financial loss, downtime, anomaly count, and mitigation success. It helps decision makers quickly identify the most vulnerable regions, assets, and attack types."
