# Smart Grid Cybersecurity Risk Assessment - DAX Measures

This document contains fully optimized, copy-paste ready DAX measures for your Power BI Data Model. 

**Note:** All measures explicitly reference the `FactCyberIncidents` table. 

---

## 1. Primary KPI Measures

```dax
Total Incidents = 
COUNTROWS(FactCyberIncidents)
```

```dax
High Risk Assets = 
CALCULATE(
    DISTINCTCOUNT(FactCyberIncidents[asset_id]),
    FactCyberIncidents[risk_level] = "High"
)
```

```dax
Critical Incidents = 
CALCULATE(
    COUNTROWS(FactCyberIncidents),
    FactCyberIncidents[severity] = "Critical"
)
```

```dax
Avg Downtime = 
AVERAGE(FactCyberIncidents[downtime_hours])
```

```dax
Avg Recovery Time = 
AVERAGE(FactCyberIncidents[recovery_time_hours])
```

```dax
Total Financial Loss = 
SUM(FactCyberIncidents[financial_loss])
```

```dax
Mitigation Success Rate = 
DIVIDE(
    CALCULATE(
        COUNTROWS(FactCyberIncidents),
        FactCyberIncidents[mitigation_status] = "Successful"
    ),
    COUNTROWS(FactCyberIncidents),
    0
)
```

```dax
Anomaly Count = 
CALCULATE(
    COUNTROWS(FactCyberIncidents),
    FactCyberIncidents[anomaly_flag] = TRUE()
)
```
*(Note: If your anomaly flag is loaded as text "Anomaly" via Power Query, change `TRUE()` to `"Anomaly"`. Native python script outputs it as a True/False boolean).*

```dax
Risk Score = 
AVERAGE(FactCyberIncidents[risk_score])
```

```dax
Monthly Incident Count = 
COUNTROWS(FactCyberIncidents)
```

---

## 2. Additional Useful Measures

```dax
Medium Risk Incidents = 
CALCULATE(
    COUNTROWS(FactCyberIncidents),
    FactCyberIncidents[risk_level] = "Medium"
)
```

```dax
Low Risk Incidents = 
CALCULATE(
    COUNTROWS(FactCyberIncidents),
    FactCyberIncidents[risk_level] = "Low"
)
```

```dax
Failed Mitigation Count = 
CALCULATE(
    COUNTROWS(FactCyberIncidents),
    FactCyberIncidents[mitigation_status] = "Failed"
)
```

```dax
Avg Vulnerability Score = 
AVERAGE(FactCyberIncidents[vulnerability_score])
```

```dax
Avg Threat Intel Score = 
AVERAGE(FactCyberIncidents[threat_intel_score])
```

```dax
Total Downtime = 
SUM(FactCyberIncidents[downtime_hours])
```

```dax
Total Recovery Time = 
SUM(FactCyberIncidents[recovery_time_hours])
```

```dax
Average Financial Loss = 
AVERAGE(FactCyberIncidents[financial_loss])
```

```dax
Energy Impact Incidents = 
CALCULATE(
    COUNTROWS(FactCyberIncidents),
    FactCyberIncidents[energy_supply_impact] IN {"Minor Disruption", "Major Outage"}
)
```

```dax
Anomaly Rate = 
DIVIDE(
    [Anomaly Count],
    [Total Incidents],
    0
)
```

```dax
Critical Risk Incidents = 
CALCULATE(
    COUNTROWS(FactCyberIncidents),
    FactCyberIncidents[risk_level] = "Critical"
)
```

---

## 3. Formatting & Visual Usage Guidance

Once you paste the formulas, click on each measure in the Data pane and apply the recommended formatting from the Measure Tools ribbon.

| Measure Name | Formatting | Primary Visual Usage |
|---|---|---|
| Total Incidents | Whole Number | KPI Card, Line Chart (trend over time) |
| High Risk Assets | Whole Number | KPI Card, Bar Chart (by region) |
| Critical Incidents | Whole Number | KPI Card, Donut Chart |
| Avg Downtime | Decimal Number, 2 decimals | KPI Card, Table |
| Avg Recovery Time | Decimal Number, 2 decimals | KPI Card, Table |
| Total Financial Loss | Currency | KPI Card, Bar Chart (by asset type) |
| Mitigation Success Rate | Percentage | KPI Card, Gauge Chart |
| Risk Score | Decimal Number, 2 decimals | KPI Card, Scatter Plot, Tooltip |
| Anomaly Rate | Percentage | KPI Card, Table |
| Medium Risk Incidents | Whole Number | Donut Chart, Table |
| Low Risk Incidents | Whole Number | Donut Chart, Table |
| Failed Mitigation Count | Whole Number | Bar Chart, KPI Card |
| Avg Vulnerability Score | Decimal Number, 2 decimals | Tooltip, Scatter Plot |
| Avg Threat Intel Score | Decimal Number, 2 decimals | Tooltip, Scatter Plot |
| Total Downtime | Decimal Number, 2 decimals | Bar Chart, Table |
| Total Recovery Time | Decimal Number, 2 decimals | Bar Chart, Table |
| Average Financial Loss | Currency | KPI Card, Bar Chart |
| Energy Impact Incidents | Whole Number | KPI Card, Donut Chart |
| Critical Risk Incidents | Whole Number | KPI Card, Donut Chart |
| Monthly Incident Count | Whole Number | Line Chart, Bar Chart |
| Anomaly Count | Whole Number | KPI Card, Table |

---

## 4. DAX Validation Checklist

- [x] **Check measure names:** All measure names are distinct, accurately described, and match the requested dashboard requirements.
- [x] **Check table name:** All formulas strictly reference the `FactCyberIncidents` table.
- [x] **Check column names:** All columns accurately map to the underlying dataset export.
- [x] **Check aggregation type:** Frequencies utilize `COUNTROWS()`, sums use `SUM()`, and averages use `AVERAGE()`.
- [x] **Check percentage formatting:** Rates (like Mitigation Success) use `DIVIDE()` logic explicitly requesting the user to format as a Percentage natively in Power BI.
- [x] **Check blank handling using DIVIDE:** All `DIVIDE()` functions include `0` as the final argument (alternate result) to prevent dividing-by-zero or `(Blank)` errors dynamically.
