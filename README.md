# 🏏 Sports Analytics: Virat Kohli Career Dashboard

![Dashboard Preview](image_fac30e.jpg)

## 📌 Project Overview
This project is an end-to-end **Sports Analytics** application designed to track and visualize the career statistics of Virat Kohli across all major formats: Test, ODI, and T20I. The project demonstrates a full data pipeline, starting from automated web scraping with bot-bypass techniques to professional data visualization.

## 🚀 Key Features
* **Stealth Data Extraction:** Implements `undetected-chromedriver` to scrape data from Cricmetric, bypassing common browser-automation detection.
* **Automated Data Processing:** A custom Python script that identifies, filters, and cleans batting statistics while automatically discarding irrelevant data (like bowling or fielding tables).
* **Multi-Format Insights:** Separate data streams for Test, ODI, and T20I formats.
* **Interactive Dashboard:** A visual representation of career milestones including:
    * **Innings & Runs:** A yearly volume analysis of performance.
    * **Boundary Breakdown:** Ratio analysis of 4s and 6s.
    * **Trend Analysis:** Tracking the frequency of 50s and 100s across the timeline.
    * **Performance Metrics:** Live view of Batting Average (51.33) and Strike Rate (91.99).

## 🛠️ Technical Stack
* **Language:** Python 3.12+
* **Web Automation:** `Selenium`, `undetected-chromedriver`
* **Data Manipulation:** `Pandas`, `io.StringIO`
* **Visualization:** Plotly / Dashboarding Software

## 📥 Getting Started

### 1. Installation
To run the scraper locally, install the required dependencies:
```bash
pip install undetected-chromedriver pandas selenium setuptools
