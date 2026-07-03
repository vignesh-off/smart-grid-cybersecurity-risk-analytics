# Power BI Implementation Guide

This guide walks you through the steps required to import the synthetic Smart Grid Cybersecurity dataset into Power BI and set up the underlying data model.

## 1. Data Ingestion
1. Open **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV**.
3. Navigate to `data/smart_grid_cybersecurity_data.csv` and select it.
4. Click **Transform Data** to open the Power Query Editor.

## 2. Power Query Transformations
While the Python script handles most calculations, ensure the following data types are correctly interpreted:
- **`date`**: Date/Time
- **`financial_loss`**: Fixed Decimal Number (Currency)
- **`response_time_hours`, `recovery_time_hours`, `downtime_hours`**: Decimal Number
- **`anomaly_flag`**: True/False (Logical)
- **`risk_score`, `vulnerability_score`, `threat_intel_score`**: Decimal Number / Whole Number

*Optional:* If you wish to build a Star Schema instead of a flat table:
1. **Dim_Asset:** Reference the main query, select `asset_id`, `asset_type`, remove duplicates.
2. **Dim_Date:** Create a standard Date Table in DAX using `CALENDARAUTO()`.
3. **Dim_Region:** Reference the main query, select `region`, remove duplicates.
4. **Fact_Incidents:** Main table containing the events and IDs.

## 3. Data Modeling
If using a flat table (default), no relationships are needed.
If using a Star Schema, establish One-to-Many relationships:
- `Dim_Asset[asset_id]` -> `Fact_Incidents[asset_id]`
- `Dim_Date[Date]` -> `Fact_Incidents[date]` (date portion)

## 4. Applying DAX Measures
1. Create a new dummy table named `_Measures` for organization (`Enter Data` -> Name it `_Measures`).
2. Open `docs/dax_measures.md` and copy the formulas one by one into Power BI.
3. Assign appropriate formatting (e.g., Currency for financial metrics, Percentage for rates).

## 5. Visualizing the Dashboard
Refer to `docs/dashboard_page_plan.md` for specific visual selections and layout strategies.

## 6. Theme and Aesthetics
- Use a **Dark Theme** to simulate a Cybersecurity Command Center (SOC).
- Suggested Colors:
  - Background: `#1E1E1E`
  - Visual Background: `#252526`
  - Accent (Low Risk): `#4CAF50` (Green)
  - Accent (Medium Risk): `#FFC107` (Yellow)
  - Accent (High Risk): `#FF9800` (Orange)
  - Accent (Critical/Anomaly): `#F44336` (Red)
