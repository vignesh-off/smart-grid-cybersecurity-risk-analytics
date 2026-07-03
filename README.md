# Smart Grid Cybersecurity Risk Assessment and Mitigation

## Overview
This repository contains the data generation scripts and documentation for a Power BI-focused Data Analytics project simulating cybersecurity risk assessment for a smart grid infrastructure. 

The goal of this project is to provide a complete analytics solution, from raw data synthesis to advanced Power BI dashboards, allowing security analysts and stakeholders to:
- Monitor grid threats in real-time.
- Assess and quantify cyber risks across different asset types.
- Detect statistical anomalies in incident response and financial loss.
- Predict upcoming threats using 90-day forecasting.
- Perform cohort analysis on repeat-targeted assets.

## Directory Structure
- `data/`: Contains the generated synthetic dataset (`.csv`).
- `scripts/`: Contains the Python data generation script (`generate_dataset.py`).
- `docs/`: Contains all Power BI implementation guides, DAX measures, dashboard plans, and analytical reports.

## Getting Started
1. Run `python scripts/generate_dataset.py` to create the synthetic `smart_grid_cybersecurity_data.csv` dataset in the `data/` folder.
2. Review the `docs/powerbi_implementation_guide.md` for instructions on loading the data into Power BI Desktop.
3. Review `docs/dashboard_page_plan.md` to build out the 7 interactive dashboard pages.
4. Copy the required DAX formulas from `docs/dax_measures.md` to support your visualizations.

## Power BI Data Model
For instructions on building an optimized star schema with this dataset, see the [Power BI Data Model Guide](docs/powerbi_data_model_star_schema.md).

## Tools Used
- **Python:** `pandas`, `numpy` for synthetic data generation and heavy logic processing (RFM, anomaly detection).
- **Power BI:** Data visualization, interactive dashboarding, and ad-hoc DAX calculations.
