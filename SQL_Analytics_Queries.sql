-- Problem 83: Smart Grid Cybersecurity Risk Assessment and Mitigation
-- Adjust table and column names based on the final cleaned dataset.

-- 1. Overall KPI summary
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT incident_id) AS total_incidents,
    AVG(risk_score) AS avg_risk_score,
    SUM(CASE WHEN severity = 'Critical' THEN 1 ELSE 0 END) AS critical_incidents,
    SUM(CASE WHEN mitigation_status IN ('Closed', 'Completed', 'Resolved') THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS mitigation_completion_rate
FROM fact_cyber_events;

-- 2. Monthly incident trend
SELECT
    DATEFROMPARTS(YEAR(incident_date), MONTH(incident_date), 1) AS incident_month,
    COUNT(*) AS incident_count,
    AVG(risk_score) AS avg_risk_score
FROM fact_cyber_events
GROUP BY DATEFROMPARTS(YEAR(incident_date), MONTH(incident_date), 1)
ORDER BY incident_month;

-- 3. Top high-risk assets
SELECT TOP 10
    asset_id,
    COUNT(*) AS incident_count,
    AVG(risk_score) AS avg_risk_score,
    SUM(downtime_hours) AS total_downtime_hours
FROM fact_cyber_events
GROUP BY asset_id
ORDER BY avg_risk_score DESC, incident_count DESC;

-- 4. Threat vector performance
SELECT
    threat_type,
    attack_vector,
    COUNT(*) AS incident_count,
    AVG(risk_score) AS avg_risk_score,
    AVG(response_time_hours) AS avg_response_time_hours
FROM fact_cyber_events
GROUP BY threat_type, attack_vector
ORDER BY incident_count DESC;

-- 5. Region-wise cybersecurity exposure
SELECT
    region,
    COUNT(*) AS incident_count,
    AVG(risk_score) AS avg_risk_score,
    SUM(CASE WHEN severity = 'Critical' THEN 1 ELSE 0 END) AS critical_incidents
FROM fact_cyber_events
GROUP BY region
ORDER BY avg_risk_score DESC;

-- 6. Rule-based anomaly flags
SELECT
    incident_id,
    asset_id,
    incident_date,
    region,
    threat_type,
    severity,
    risk_score,
    response_time_hours,
    downtime_hours,
    CASE
        WHEN risk_score >= 80 THEN 'High Risk Score'
        WHEN severity = 'Critical' THEN 'Critical Severity'
        WHEN response_time_hours > 24 THEN 'Response SLA Breach'
        WHEN downtime_hours > 12 THEN 'High Downtime'
        ELSE 'Normal'
    END AS anomaly_reason
FROM fact_cyber_events
WHERE risk_score >= 80
   OR severity = 'Critical'
   OR response_time_hours > 24
   OR downtime_hours > 12;

-- 7. Repeat incident assets
SELECT
    asset_id,
    COUNT(*) AS incident_count,
    MIN(incident_date) AS first_incident_date,
    MAX(incident_date) AS last_incident_date,
    AVG(risk_score) AS avg_risk_score
FROM fact_cyber_events
GROUP BY asset_id
HAVING COUNT(*) >= 3
ORDER BY incident_count DESC;
