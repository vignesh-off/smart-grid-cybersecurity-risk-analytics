# Page 2: EDA and Incident Pattern Analysis

## 1. Page Objective
This page analyzes incident patterns, distributions, outliers, and relationships between cybersecurity metrics. It supports the Day 2 requirement for Descriptive Statistics and Exploratory Data Analysis (EDA) to uncover underlying patterns, identify anomalies, and understand the spread and concentration of the data.

## 2. Page Layout
Design a professional Power BI layout integrating exploratory statistical views:
- **Header Title:** Top-center (e.g., "EDA and Incident Pattern Analysis").
- **Slicer Panel:** A left-hand vertical pane for exploratory filtering.
- **Descriptive KPI Cards:** A row immediately below the header showing averages and totals for context.
- **Distribution Charts:** Top row of the main canvas focusing on histograms/bins for scores and downtime.
- **Relationship/Correlation Visuals:** Middle canvas utilizing scatter plots and categorized bar charts to show metric interactions.
- **Outlier Table:** Bottom section dedicated to explicitly highlighting anomalous records.
- **Insight Text Box:** Positioned near the correlation visuals or top right to present a synthesized summary.

## 3. KPI Cards
Use the following DAX measures to build the descriptive KPI row:

| KPI Card | Measure Name | Display Format | Analytical Meaning |
|---|---|---|---|
| **Total Incidents** | Total Incidents | Whole Number | Baseline volume of data points in the current filtered context. |
| **Avg Vulnerability Score** | Avg Vulnerability Score | Decimal Number, 2 decimals | General baseline vulnerability of the grid/asset selection. |
| **Avg Threat Intel Score** | Avg Threat Intel Score | Decimal Number, 2 decimals | Average external threat severity score. |
| **Avg Downtime** | Avg Downtime | Decimal Number, 2 decimals | Average hours components remain offline. |
| **Average Financial Loss** | Average Financial Loss | Currency | Average cost per incident. |
| **Risk Score** | Risk Score | Decimal Number, 2 decimals | Aggregate composite risk rating for the selected data. |
| **Anomaly Count** | Anomaly Count | Whole Number | Count of statistical outliers detected. |

## 4. Visuals Required
Configure the exploratory visuals precisely as follows:

### A. Histogram / Column Chart
- **Title:** Vulnerability Score Distribution
- **Axis:** `vulnerability_score` bins (use Power BI Data Groups to create bins, e.g., size 10)
- **Values:** Count of `incident_id`

### B. Histogram / Column Chart
- **Title:** Downtime Hours Distribution
- **Axis:** `downtime_hours` bins (use Data Groups to create bins)
- **Values:** Count of `incident_id`

### C. Box Plot Alternative (or Column Chart)
- **Title:** Financial Loss by Severity
- **Visual type:** Column chart (or a custom Box and Whisker visual if available)
- **Axis:** `severity`
- **Values:** Average `financial_loss`
- **Tooltip:** Min `financial_loss`, Max `financial_loss`, and Avg `financial_loss` (if using a standard column chart).

### D. Scatter Plot
- **Title:** Vulnerability Score vs Downtime
- **X-axis:** `vulnerability_score`
- **Y-axis:** `downtime_hours`
- **Size:** `financial_loss`
- **Legend:** `severity`
- **Tooltip:** `asset_id`, `attack_type`, `risk_score`

### E. Line Chart
- **Title:** Incident Trend Over Time
- **Axis:** `date` or `month_year`
- **Values:** Monthly Incident Count
- **Legend:** `severity`

### F. Bar Chart
- **Title:** Average Recovery Time by Attack Type
- **Axis:** `attack_type`
- **Values:** Avg Recovery Time

### G. Table
- **Title:** Outlier Incident Records
- **Columns:** `incident_id`, `date`, `asset_id`, `region`, `attack_type`, `severity`, `downtime_hours`, `financial_loss`, `risk_score`, `anomaly_flag`
- **Filter:** Set a visual-level filter where `anomaly_flag` = `TRUE()` (or `"Anomaly"` based on your dataset loading).
- **Sort by:** `financial_loss` descending.

## 5. Slicers
Provide the following slicers in the Slicer Panel:
- Date range
- Region
- Asset Type
- Attack Type
- Severity
- Risk Level
- Anomaly Flag

## 6. EDA Questions Answered
This dashboard is explicitly structured to answer the following exploratory questions:
- **Which severity levels cause the highest financial loss?** *(Answered by Visual C)*
- **Do vulnerable assets experience more downtime?** *(Answered by Scatter Plot D)*
- **Which attack types have slower recovery?** *(Answered by Visual F)*
- **Are incidents increasing or decreasing over time?** *(Answered by Visual E)*
- **Which records behave like outliers?** *(Answered by Table G)*

## 7. Insight Box
Insert a Text Box onto the dashboard with the following template:
> "EDA shows that high vulnerability scores and critical severity incidents are associated with higher downtime and financial loss. Outlier incidents should be prioritized for root-cause analysis and security improvement."

## 8. Viva Explanation
*Use this explanation during presentations or project vivas:*
> "This page performs exploratory data analysis. It helps identify distributions, trends, correlations, and outliers in smart grid cybersecurity incidents."
