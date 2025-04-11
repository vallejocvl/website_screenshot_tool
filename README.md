# website_screenshot_tool
This Python script captures full-page screenshots of all the URLs listed in a sitemap, using Selenium to navigate and render each page. The script extracts the URLs from a CSV file generated from an XML sitemap, then visits each URL, scrolls to the bottom to ensure all content loads, and saves a screenshot of the full page.

## Requirements

Before running the script, ensure you have the following dependencies installed:
	•	Selenium
	•	Pandas
	•	ChromeDriver

## Setup
	1.	Generate the Sitemap CSV:
To use this script, you will need a CSV file containing the URLs you want to screenshot. Follow these steps:
	•	Use XML-Sitemaps (https://www.xml-sitemaps.com/) to generate your XML sitemap from your website.
	•	Then, convert the XML file to CSV using Data.Page (https://data.page/xml/csv)
	•	Save the CSV file as sitemap.csv in the database folder.
The CSV file should have at least one column with the name url__loc, containing the URLs of your website.
    2. Directory Structure
        ├── database
        │   └── sitemap.csv
        └── screenshots
        └── .gitignore
        └── README.md
        └── web_screenshot_tool.py