# Page 7: Cohort and Repeat Incident Analysis

## 1. Page Objective
This page analyzes repeat cyber incidents over time using cohort analysis. It helps security leaders identify whether specific assets continue to experience attacks after their first recorded incident and evaluate whether past mitigation actions successfully reduce repeated attacks in the long term.

## 2. Cohort Logic Explanation
This page adapts traditional customer retention analysis strictly for cybersecurity incident recurrence:
- **`cohort_month`:** The exact month and year an asset experienced its *first* recorded cyber incident.
- **Repeat Incidents:** Any subsequent attacks recorded on that same asset in later months.
- **Retention (Recurrence):** The percentage or count of assets/incidents continuing to appear in later months.
- **Analytical Value:** A lower repeat rate in the months following an initial breach indicates an improved security posture and effective mitigation, whereas high recurrence indicates persistent vulnerabilities or active targeting.

*Note: This is similar to customer retention analysis, but adapted specifically to cyber incident recurrence.*

## 3. Page Layout
Design a professional Power BI layout integrating cohort analysis matrices:
- **Header Title:** Top-center (e.g., "Cohort & Repeat Incident Analysis").
- **Slicer Panel:** Vertical pane on the left or top to filter cohorts, dates, and regions.
- **Cohort KPI Cards:** A row of metrics sitting directly below the header to establish baseline volumes and success rates.
- **Cohort Heatmap / Matrix:** The centerpiece of the top/middle canvas detailing the retention-style grid over time.
- **Repeat Incident Trends:** Flanking or below the heatmap, charting recurrence by asset type and mitigation status.
- **Repeat Attack Risk Map:** A scatter plot mapping repeat frequencies against risk scores.
- **Asset Repeat Attack Table:** Lower canvas dedicated to an actionable watchlist of repeatedly compromised assets.
- **Insight/Recommendation Text Box:** Top right or near the watchlist to summarize actionable takeaways.

## 4. KPI Cards
Use the following DAX measures to establish cohort and repeat attack baselines:

| KPI Card | Measure Name | Display Format | Cohort Meaning |
|---|---|---|---|
| **Total Incidents** | Total Incidents | Whole Number | Overall volume of attacks within the selected cohort view. |
| **High Risk Assets** | High Risk Assets | Whole Number | Volume of targeted assets identified as high risk. |
| **Anomaly Count** | Anomaly Count | Whole Number | Volume of statistical outliers occurring in these repeat attacks. |
| **Failed Mitigation Count** | Failed Mitigation Count | Whole Number | Number of times defenses failed during repeat attacks. |
| **Mitigation Success Rate** | Mitigation Success Rate | Percentage | Effectiveness of stopping repeat targeting. |
| **Risk Score** | Risk Score | Decimal Number, 2 decimals | The aggregate severity and impact of repeat attacks. |
| **Avg Downtime** | Avg Downtime | Decimal Number, 2 decimals | Operational hours lost to these recurring incidents. |
| **Total Financial Loss** | Total Financial Loss | Currency | Economic damage caused by repeat exploitation. |

## 5. Visuals Required
Add these visuals to the canvas with the exact configurations below:

### A. Matrix / Heatmap
- **Title:** Cohort Repeat Incident Heatmap
- **Rows:** `cohort_month`
- **Columns:** `month_year`
- **Values:** Count of `incident_id` (or Total Incidents)
- **Conditional Formatting:** Apply Background Color intensity based on incident count (e.g., darker red for higher counts) to visually represent retention.

### B. Line Chart
- **Title:** Repeat Incident Trend Over Time
- **Axis:** `month_year` or `date`
- **Values:** Total Incidents
- **Legend:** `asset_segment` or `risk_level`

### C. Bar Chart
- **Title:** Repeat Incidents by Asset Type
- **Axis:** `asset_type`
- **Values:** Total Incidents
- **Legend:** `risk_level`

### D. Column Chart
- **Title:** Mitigation Status Impact on Repeat Incidents
- **Axis:** `mitigation_status`
- **Values:** Total Incidents
- **Tooltip:** Avg Downtime, Total Financial Loss, Risk Score

### E. Scatter Plot
- **Title:** Repeat Attack Risk Map
- **X-axis:** `rfm_frequency_score`
- **Y-axis:** `risk_score`
- **Size:** `financial_loss`
- **Legend:** `mitigation_status`
- **Tooltip:** `asset_id`, `asset_type`, `region`, `attack_type`, `anomaly_flag`

### F. Table
- **Title:** Repeat Attack Asset Watchlist
- **Columns:** `asset_id`, `asset_type`, `region`, `cohort_month`, `month_year`, `asset_segment`, `risk_score`, `risk_level`, `anomaly_flag`, `mitigation_status`, `financial_loss`, `downtime_hours`
- **Sort by:** `risk_score` descending.

## 6. Slicers
Add the following slicers to the Slicer Panel:
- Cohort Month
- Date Range
- Region
- Asset Type
- Asset Segment
- Risk Level
- Mitigation Status
- Attack Type

## 7. Cohort Questions Answered
This dashboard is explicitly structured to answer the following business questions:
- **Which asset cohorts continue to experience incidents?** *(Answered by Matrix A)*
- **Are repeat incidents reducing after mitigation?** *(Answered by Column Chart D and Matrix A)*
- **Which asset types are repeatedly attacked?** *(Answered by Bar Chart C)*
- **Which cohorts have the highest long-term risk?** *(Answered by Line Chart B)*
- **Which assets need long-term monitoring?** *(Answered by Table F)*
- **Are failed mitigations linked with repeat attacks?** *(Answered by Scatter Plot E and Column Chart D)*

## 8. Recommendation Box
Insert a Text Box onto the dashboard with the following template:
> "Asset cohorts with repeated incidents after mitigation should be prioritized for deeper security review, patch validation, continuous monitoring, and incident response improvement."

## 9. Viva Explanation
*Use this explanation during presentations or project vivas:*
> "This page adapts cohort and retention analysis for cybersecurity. Instead of customer retention, we track whether smart grid assets continue to experience cyber incidents after their first attack month."
