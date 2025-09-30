import requests
from bs4 import BeautifulSoup
import csv
import os

# Create data directory
os.makedirs('data', exist_ok=True)

# Target site
url = 'https://news.ycombinator.com/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("❌ Failed to fetch page")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Collect titles (new structure)
titles = [a.get_text() for a in soup.select('.titleline a')]

# Save to CSV
file_path = 'data/hackernews.csv'
with open(file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    for title in titles:
        writer.writerow([title])

print(f"✅ {len(titles)} items saved to {file_path}")
