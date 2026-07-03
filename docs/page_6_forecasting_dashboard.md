# Page 6: 90-Day Forecasting Dashboard

## 1. Page Objective
This page utilizes historical smart grid cybersecurity data to forecast upcoming incident trends, anomaly trends, downtime impacts, and financial losses for the next 90 days. It helps security leaders and resource planners move from a reactive posture to a proactive, predictive defense strategy.

## 2. Forecasting Approach
This dashboard leverages **Power BI's native forecasting analytics** built directly into the visual interface.
- **Visual Type:** Forecasts are applied strictly to Line Charts.
- **Axis Mapping:** A continuous `date` field must be placed on the X-axis.
- **Values:** The numeric measure (e.g., Total Incidents) is placed on the Y-axis.
- **Configuration (Analytics Pane):**
  - **Forecast length:** 90 days
  - **Confidence interval:** 95%
  - **Seasonality:** Auto (or Monthly if the temporal pattern demands it)

## 3. Page Layout
Design a professional forecasting dashboard with the following structure:
- **Header Title:** Top-center (e.g., "90-Day Cybersecurity Forecast").
- **Forecast KPI Cards:** A row immediately below the header showing current historical baselines prior to the forecast.
- **Main Forecast Charts:** Top/middle canvas featuring large line charts projecting Incidents and Financial Loss.
- **Risk/Downtime & Anomaly Forecast Charts:** Middle canvas tracking predicted anomalies and system risks over time.
- **Forecast-Sensitive Breakdown & Risk Watchlist:** Lower canvas identifying the attack types driving the trends and a table of high-risk assets to monitor.
- **Slicers:** Standard filtering pane on the left or top.
- **Forecast Interpretation & Recommendation Section:** Text boxes guiding stakeholders on how to read the confidence intervals and what actions to take.

## 4. KPI Cards
Use the following DAX measures to establish the historical baseline above the forecasts:

| KPI Card | Measure Name | Display Format | Forecasting Meaning |
|---|---|---|---|
| **Total Incidents** | Total Incidents | Whole Number | Historical baseline volume feeding the forecast. |
| **Anomaly Count** | Anomaly Count | Whole Number | Historical baseline of suspicious events. |
| **Total Financial Loss** | Total Financial Loss | Currency | Historical financial baseline driving future loss models. |
| **Avg Downtime** | Avg Downtime | Decimal Number, 2 decimals | Historical operational downtime average. |
| **Risk Score** | Risk Score | Decimal Number, 2 decimals | Current average risk exposure. |
| **Mitigation Success Rate** | Mitigation Success Rate | Percentage | Historical success rate that future defenses must maintain or exceed. |

## 5. Visuals Required
Add these visuals to the canvas with the exact configurations below:

### A. Line Chart with Power BI Forecast
- **Title:** 90-Day Incident Forecast
- **Axis:** `date`
- **Values:** Monthly Incident Count (or Total Incidents)
- **Analytics Pane Configuration:** Forecast Length: 90 days, Confidence Interval: 95%, Seasonality: Auto

### B. Line Chart with Forecast
- **Title:** 90-Day Financial Loss Forecast
- **Axis:** `date`
- **Values:** Total Financial Loss
- **Analytics Pane Configuration:** Forecast Length: 90 days, Confidence Interval: 95%

### C. Line Chart with Forecast
- **Title:** Anomaly Trend Forecast
- **Axis:** `date`
- **Values:** Anomaly Count
- **Analytics Pane Configuration:** Forecast Length: 90 days, Confidence Interval: 95%

### D. Combo Chart
- **Title:** Downtime and Risk Trend
- **Axis:** `month_year` or `date`
- **Column Values:** Avg Downtime
- **Line Values:** Risk Score

### E. Bar Chart
- **Title:** Forecast-Sensitive Attack Types
- **Axis:** `attack_type`
- **Values:** Total Incidents
- **Tooltip:** Avg Downtime, Total Financial Loss, Risk Score

### F. Table
- **Title:** Forecast Risk Watchlist
- **Columns:** `asset_id`, `asset_type`, `region`, `attack_type`, `risk_score`, `risk_level`, `anomaly_flag`, `financial_loss`, `mitigation_status`
- **Filter:** Apply a visual-level filter where `risk_level` = "High" OR `anomaly_flag` = `TRUE()` (or `"Anomaly"`).
- **Sort by:** `risk_score` descending.

## 6. Slicers
Add the following slicers to the Slicer Panel:
- Date Range
- Region
- Asset Type
- Attack Type
- Severity
- Risk Level

## 7. Forecast Interpretation
Provide the following guidance to dashboard users:
- The forecast is strictly based on historical incident patterns and seasonality.
- The **confidence interval (shaded area)** visualizes uncertainty; wider bands mean higher volatility in historical data.
- An increasing forecast trend indicates a critical need for preventive mitigation before the predicted incidents occur.
- **Note:** The forecast does not guarantee exact future incidents, but rather supports strategic resource and response planning.

## 8. Limitations
Include a disclaimer regarding the model's limitations:
- The forecast depends entirely on the quality and volume of the historical data.
- Sudden, unprecedented "zero-day" attacks or entirely novel threat vectors cannot be predicted exactly by this model.
- The forecast should be used in conjunction with live threat intelligence and active operational monitoring, not as a standalone source of truth.

## 9. Recommendation Box
Insert a Text Box onto the dashboard with the following template:
> "If the 90-day incident forecast increases, security teams should strengthen monitoring, patch high-risk assets, improve incident response readiness, and allocate resources to vulnerable regions and asset types."

## 10. Viva Explanation
*Use this explanation during presentations or project vivas:*
> "This page uses Power BI's built-in time-series forecasting to estimate the next 90 days of cybersecurity incidents, financial loss, and anomalies. The confidence interval helps decision makers understand forecast uncertainty."
