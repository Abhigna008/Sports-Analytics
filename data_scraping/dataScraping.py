import sys

# --- 1. COMPATIBILITY PATCH FOR PYTHON 3.12+ ---
try:
    import distutils.version
except ImportError:
    import setuptools
    import types
    m = types.ModuleType('distutils.version')
    m.LooseVersion = setuptools.distutils.version.LooseVersion
    sys.modules['distutils.version'] = m
# -----------------------------------------------

import undetected_chromedriver as uc
import pandas as pd
from io import StringIO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def start_scraping():
    print("🚀 Launching Stealth Browser...")
    driver = uc.Chrome()
    
    try:
        url = "https://www.cricmetric.com/sage/?q=virat+kohli"
        driver.get(url)

        print("⏳ Waiting for tables to render...")
        # Wait up to 20 seconds for the tables to appear
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        # 2. Extract HTML and find all tables
        html_data = StringIO(driver.page_source)
        all_tables = pd.read_html(html_data)
        
        # 3. FILTER LOGIC: Only keep tables that have 'Runs' (Batting) 
        # and ignore tables that have 'Wickets' or 'Overs' (Bowling)
        batting_tables = []
        for table in all_tables:
            if 'Runs' in table.columns and 'Overs' not in table.columns:
                batting_tables.append(table)

        print(f"📊 Found {len(batting_tables)} Batting tables.")

        # 4. Save the correct tables
        formats = ["Test", "ODI", "T20I"]
        for i in range(min(len(batting_tables), 3)):
            format_name = formats[i]
            df = batting_tables[i]
            
            # Save to CSV
            filename = f"kohli_{format_name.lower()}_batting.csv"
            df.to_csv(filename, index=False)
            print(f"✅ Saved {format_name} Batting stats to {filename}")

    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    start_scraping()