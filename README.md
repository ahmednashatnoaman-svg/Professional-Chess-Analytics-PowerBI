# Professional Chess Analytics Dashboard

This repository contains an end-to-end data analytics project focused on chess games. It transforms raw gameplay data into a high-performance **Power BI Star Schema** and provides a premium, "Glassmorphism" UI design for executive-level visualization.

## 📂 Repository Structure

The project has been professionally organized into the following directories:

*   **`data/`**: Contains the raw `games.csv` dataset and the enriched Star Schema tables (`Fact_Games.csv`, `Dim_Openings.csv`, `Dim_Players.csv`, `Dim_TimeControls.csv`). *(Note: Raw data may be ignored in git depending on size, but the schema tables are included).*
*   **`scripts/`**: Python scripts (`build_star_schema.py` and `data_summary.py`) used to process the flat file into dimensional models, calculate Player Tiers, identify Upsets, and extract Opening Families. Also contains the initial Jupyter Notebook for data exploration.
*   **`dashboard/`**: The primary `Chess Dashboard.pbix` file.
*   **`assets/`**: Contains the generated high-resolution background image for the dashboard (`dashboard_bg.png`), the custom Power BI JSON theme (`professional_chess_theme.json`), and original screenshots.

## 🚀 Key Features

1.  **Optimized Data Architecture**:
    *   Python-driven ETL process that converts a flat CSV into a robust Star Schema.
    *   Pre-calculated analytical flags such as `Is_Upset` (underdog victories) and `Player_Tier`.
2.  **Advanced DAX & Analytics**:
    *   Opening Efficiency Scores.
    *   Performance vs. Elo Expectation.
3.  **Premium UI/UX**:
    *   Custom dark/gold theme designed for Power BI.
    *   Background template designed for "Glassmorphism" visuals (transparent chart backgrounds).

## 🛠️ Setup Instructions

1.  **Data Processing**: Run `python3 scripts/build_star_schema.py` to generate the latest Fact and Dimension tables from `data/games.csv`.
2.  **Power BI Setup**:
    *   Open `dashboard/Chess Dashboard.pbix`.
    *   Ensure the data sources point to the files in the `data/` folder.
    *   Go to **View > Themes > Browse for themes** and select `assets/professional_chess_theme.json`.
    *   Go to **Format Page > Canvas Background**, upload `assets/dashboard_bg.png`, set Transparency to 0% and Image Fit to 'Fit'. Make sure visual backgrounds are turned off.

---
*Built with ❤️ using Python, pandas, and Power BI.*