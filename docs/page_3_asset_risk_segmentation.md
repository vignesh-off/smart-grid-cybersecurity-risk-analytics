# Page 3: Asset Risk Segmentation

## 1. Page Objective
This page segments smart grid assets based on incident recency, attack frequency, and impact magnitude. By grouping assets into behavioral clusters, this dashboard allows security teams to quickly identify and prioritize critical risk groups over stable, low-priority assets.

## 2. RFM Logic Explanation
This page adapts the traditional RFM (Recency, Frequency, Monetary) model, typically used for customer segmentation, into a robust **cybersecurity asset segmentation** model:

- **R = Recency:** How recently an asset experienced a cyber incident. Assets attacked more recently score higher, indicating an active threat vector.
- **F = Frequency:** How often the asset has been attacked over the assessed period. Repeated attacks indicate persistent targeting.
- **M = Magnitude:** The impact level of incidents based on financial loss, downtime, severity, and risk score. Replaces the traditional "Monetary" aspect with a broader operational impact score.

*Note: This is not customer segmentation, but an adapted framework specifically designed for cybersecurity asset segmentation.*

## 3. Page Layout
Design a professional, structured Power BI layout to facilitate asset analysis:
- **Header Title:** Top-center (e.g., "Asset Risk Segmentation (RFM)").
- **Slicer Panel:** Left-side pane for quick filtering by region, segment, and date.
- **RFM KPI Cards:** A row below the header summarizing incident metrics and risk across the selected assets.
- **Segment Distribution Visuals:** Top row of the canvas displaying the spread and risk scores across the different asset segments.
- **Risk Comparison Visuals:** Middle canvas featuring a dynamic Frequency vs Magnitude scatter plot and regional treemaps.
- **Asset Drill-Down Table:** Bottom canvas dedicated to an actionable list of individual assets and their exact RFM scores.
- **Insight/Recommendation Text Box:** Prominently placed to provide immediate strategic guidance.

## 4. KPI Cards
Use the following DAX measures for the top-level KPI row:

| KPI Card | Measure Name | Display Format | Business Meaning |
|---|---|---|---|
| **Total Incidents** | Total Incidents | Whole Number | Volume of incidents affecting the filtered segment. |
| **High Risk Assets** | High Risk Assets | Whole Number | Count of assets explicitly classified as high-risk targets. |
| **Risk Score** | Risk Score | Decimal Number, 2 decimals | Aggregate risk score of the selected asset group. |
| **Average Financial Loss** | Average Financial Loss | Currency | Average monetary impact for the filtered assets. |
| **Avg Downtime** | Avg Downtime | Decimal Number, 2 decimals | Average downtime in hours. |
| **Failed Mitigation Count** | Failed Mitigation Count | Whole Number | Count of mitigation failures, indicating defensive weakness. |
| **Critical Incidents** | Critical Incidents | Whole Number | Number of critical-severity attacks on these assets. |

## 5. Visuals Required
Add these visuals to the canvas with the exact configurations below:

### A. Donut Chart
- **Title:** Asset Segment Distribution
- **Legend:** `asset_segment`
- **Values:** Count of `asset_id` (Distinct) or Total Incidents

### B. Bar Chart
- **Title:** Average Risk Score by Asset Segment
- **Axis:** `asset_segment`
- **Values:** Risk Score

### C. Column Chart
- **Title:** Incident Frequency by Asset Type
- **Axis:** `asset_type`
- **Legend:** `asset_segment`
- **Values:** Total Incidents

### D. Scatter Plot
- **Title:** Frequency vs Magnitude Risk Map
- **X-axis:** `rfm_frequency_score`
- **Y-axis:** `rfm_magnitude_score`
- **Size:** `risk_score`
- **Legend:** `asset_segment`
- **Tooltip:** `asset_id`, `asset_type`, `region`, `risk_score`, `financial_loss`, `downtime_hours`

### E. Treemap
- **Title:** Risk Contribution by Region and Asset Type
- **Group:** `region`
- **Details:** `asset_type`
- **Values:** Risk Score or Total Financial Loss

### F. Table
- **Title:** Asset Segment Drill-Down
- **Columns:** `asset_id`, `asset_type`, `region`, `asset_segment`, `rfm_recency_score`, `rfm_frequency_score`, `rfm_magnitude_score`, `risk_score`, `risk_level`, `financial_loss`, `mitigation_status`
- **Sort by:** `risk_score` descending.

## 6. Suggested Segment Names
The underlying dataset categorizes assets into predefined segments based on their RFM scores. Ensure users understand these possible segments:
- **Critical Repeat Target:** High frequency and high magnitude. Requires immediate intervention.
- **High Impact Asset:** Low frequency but catastrophic magnitude when breached.
- **Frequently Targeted Asset:** High frequency but lower immediate magnitude.
- **Moderate Risk Asset:** Average frequency and impact.
- **Stable Asset:** Low recency, low frequency, low magnitude.
- **Needs Monitoring:** Dormant threats that have historically high frequency but haven't been attacked recently.

## 7. Slicers
Add the following slicers to the Slicer Panel:
- Region
- Asset Type
- Asset Segment
- Risk Level
- Severity
- Mitigation Status
- Date Range

## 8. Business Questions Answered
This dashboard is explicitly structured to answer the following business questions:
- **Which assets are repeatedly attacked?** *(Answered by Scatter Plot X-axis and Table F)*
- **Which assets create the highest financial impact?** *(Answered by Scatter Plot Y-axis and Treemap E)*
- **Which asset types need priority hardening?** *(Answered by Column Chart C)*
- **Which regions have more critical assets?** *(Answered by Treemap E)*
- **Which assets are stable and low priority?** *(Answered by Donut Chart A and filtering Table F)*

## 9. Recommendation Box
Insert a Text Box onto the dashboard with the following template:
> "Assets classified as Critical Repeat Target or High Impact Asset should receive immediate patching, continuous monitoring, and incident response optimization. Stable assets can follow standard monitoring cycles."

## 10. Viva Explanation
*Use this explanation during presentations or project vivas:*
> "This page uses RFM-style segmentation adapted for cybersecurity. Instead of customers, we segment smart grid assets based on recent incidents, attack frequency, and impact magnitude."
