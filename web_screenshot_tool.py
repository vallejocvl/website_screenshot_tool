import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse

# Set up Chrome (you can make it headless later)
options = Options()
options.add_argument("--headless")  # Uncomment if you want headless
driver = webdriver.Chrome(options=options)

# Load the csv and extract URLs
df = pd.read_csv('database/sitemap.csv')
urls = df['url__loc'].dropna().tolist()
output_folder = 'screenshots'
print(f"Found {len(urls)} URLs")

# Define function
def filename_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path:
        return 'homepage'
    else:
        return path.replace('/', '-')

# Loop through my URLs
for url in urls:
    print(f'Processing: {url}')
    driver.get(url)
    time.sleep(3)

    # Scroll Down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for lazy-loaded content

    # Adjust window size to capture full page
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, height)
    time.sleep(1)

    # Save PNG
    filename = filename_url(url) + '.png'
    filepath = os.path.join(output_folder, filename)
    driver.save_screenshot(filepath)
    print(f"Saved screenshot: {filepath}")

# Close Browser
driver.quit()