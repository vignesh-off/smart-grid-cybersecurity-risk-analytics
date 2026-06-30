"""
Problem 83: Smart Grid Cybersecurity Risk Assessment and Mitigation

Starter Python template for EDA, segmentation, anomaly detection,
forecasting, and cohort analysis.

Place Master Energy_Utilities_Data.xlsx in the same folder before running.
Adjust column names after inspecting the actual dataset.
"""

from pathlib import Path

import numpy as np
import pandas as pd


DATA_FILE = Path("Master Energy_Utilities_Data.xlsx")
CSV_FALLBACK_FILE = Path("Master Energy_Utilities_Data.csv")


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return df


def load_data() -> pd.DataFrame:
    if not DATA_FILE.exists() and not CSV_FALLBACK_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE} or {CSV_FALLBACK_FILE}")

    if CSV_FALLBACK_FILE.exists():
        return clean_columns(pd.read_csv(CSV_FALLBACK_FILE))

    sheets = pd.read_excel(DATA_FILE, sheet_name=None)
    frames = []

    for sheet_name, sheet_df in sheets.items():
        sheet_df = clean_columns(sheet_df)
        sheet_df["source_sheet"] = sheet_name
        frames.append(sheet_df)

    return pd.concat(frames, ignore_index=True, sort=False)


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in df.columns:
        if "date" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    numeric_candidates = [
        "risk_score",
        "downtime_hours",
        "response_time_hours",
        "recovery_time_hours",
        "estimated_loss",
    ]

    for col in numeric_candidates:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna("Unknown").astype(str).str.strip()

    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].median())

    return df.drop_duplicates()


def create_kpis(df: pd.DataFrame) -> dict:
    kpis = {
        "total_records": len(df),
    }

    if "incident_id" in df.columns:
        kpis["total_incidents"] = df["incident_id"].nunique()

    if "severity" in df.columns:
        kpis["critical_incidents"] = int((df["severity"].str.lower() == "critical").sum())

    if "risk_score" in df.columns:
        kpis["average_risk_score"] = round(df["risk_score"].mean(), 2)
        kpis["high_risk_records"] = int((df["risk_score"] >= 80).sum())

    if "mitigation_status" in df.columns:
        complete = df["mitigation_status"].str.lower().isin(["closed", "completed", "resolved"])
        kpis["mitigation_completion_rate"] = round(complete.mean() * 100, 2)

    return kpis


def segment_assets(df: pd.DataFrame) -> pd.DataFrame:
    required = {"asset_id", "incident_date", "risk_score"}
    if not required.issubset(df.columns):
        return pd.DataFrame()

    snapshot_date = df["incident_date"].max() + pd.Timedelta(days=1)

    rfm = (
        df.groupby("asset_id")
        .agg(
            recency_days=("incident_date", lambda x: (snapshot_date - x.max()).days),
            frequency=("incident_date", "count"),
            magnitude=("risk_score", "mean"),
        )
        .reset_index()
    )

    rfm["recency_score"] = pd.cut(
        rfm["recency_days"].rank(method="first", ascending=False),
        bins=4,
        labels=[1, 2, 3, 4],
    )
    rfm["frequency_score"] = pd.cut(
        rfm["frequency"].rank(method="first"),
        bins=4,
        labels=[1, 2, 3, 4],
    )
    rfm["magnitude_score"] = pd.cut(
        rfm["magnitude"].rank(method="first"),
        bins=4,
        labels=[1, 2, 3, 4],
    )

    score_cols = ["recency_score", "frequency_score", "magnitude_score"]
    rfm[score_cols] = rfm[score_cols].astype(int)
    rfm["risk_segment_score"] = rfm[score_cols].sum(axis=1)

    rfm["segment"] = np.select(
        [
            rfm["risk_segment_score"] >= 10,
            rfm["frequency_score"] >= 4,
            rfm["magnitude_score"] >= 4,
            rfm["recency_score"] >= 4,
        ],
        [
            "Critical High-Risk Asset",
            "Frequently Targeted Asset",
            "High-Impact Asset",
            "Recently Compromised Asset",
        ],
        default="Stable / Lower-Risk Asset",
    )

    return rfm


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["anomaly_flag"] = False
    df["anomaly_reason"] = ""

    if "risk_score" in df.columns:
        q1 = df["risk_score"].quantile(0.25)
        q3 = df["risk_score"].quantile(0.75)
        iqr = q3 - q1
        risk_limit = q3 + 1.5 * iqr
        mask = (df["risk_score"] >= 80) | (df["risk_score"] > risk_limit)
        df.loc[mask, "anomaly_flag"] = True
        df.loc[mask, "anomaly_reason"] += "High risk score; "

    if "response_time_hours" in df.columns:
        mask = df["response_time_hours"] > df["response_time_hours"].mean() + 2 * df["response_time_hours"].std()
        df.loc[mask, "anomaly_flag"] = True
        df.loc[mask, "anomaly_reason"] += "Unusual response time; "

    if "asset_id" in df.columns:
        counts = df["asset_id"].value_counts()
        frequent_assets = counts[counts > counts.mean() + 2 * counts.std()].index
        mask = df["asset_id"].isin(frequent_assets)
        df.loc[mask, "anomaly_flag"] = True
        df.loc[mask, "anomaly_reason"] += "Repeated incidents for asset; "

    return df


def monthly_forecast_input(df: pd.DataFrame) -> pd.DataFrame:
    if "incident_date" not in df.columns:
        return pd.DataFrame()

    monthly = (
        df.set_index("incident_date")
        .resample("MS")
        .size()
        .rename("incident_count")
        .reset_index()
    )
    monthly["rolling_3_month_avg"] = monthly["incident_count"].rolling(3, min_periods=1).mean()
    return monthly


def cohort_analysis(df: pd.DataFrame) -> pd.DataFrame:
    required = {"asset_id", "incident_date"}
    if not required.issubset(df.columns):
        return pd.DataFrame()

    cohort = df[["asset_id", "incident_date"]].dropna().copy()
    cohort["incident_month"] = cohort["incident_date"].dt.to_period("M")
    cohort["cohort_month"] = cohort.groupby("asset_id")["incident_month"].transform("min")
    cohort["period_number"] = (cohort["incident_month"] - cohort["cohort_month"]).apply(lambda x: x.n)

    matrix = (
        cohort.groupby(["cohort_month", "period_number"])["asset_id"]
        .nunique()
        .reset_index()
        .pivot(index="cohort_month", columns="period_number", values="asset_id")
    )

    return matrix


def main() -> None:
    raw = load_data()
    df = prepare_data(raw)

    print("KPIs")
    print(create_kpis(df))

    detect_anomalies(df).to_csv("anomaly_detection_output.csv", index=False)
    segment_assets(df).to_csv("asset_segmentation_output.csv", index=False)
    monthly_forecast_input(df).to_csv("monthly_forecast_input.csv", index=False)
    cohort_analysis(df).to_csv("cohort_analysis_output.csv")

    df.to_csv("cleaned_smart_grid_cybersecurity_data.csv", index=False)
    print("Analysis files exported.")


if __name__ == "__main__":
    main()
