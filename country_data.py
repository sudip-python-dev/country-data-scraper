import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.scrapethissite.com/pages/simple/"

print(f"Scraping started :  {url}")

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

print("Page scraped successfully.")
print("Processing data...")

countries_list = [
    country.text.strip()
    for country in soup.find_all('h3')
]


data_1 = [data.text.strip() for data in soup.find_all('strong')]

data_2 = [data.text.strip() for data in soup.find_all('span')]

all_data = list(zip(data_1, data_2))

result = [
    all_data[i:i+3]
    for i in range(0, len(all_data), 3)
]

rows = []

for country, details in zip(countries_list, result):
    row = {
        "Country": country,
        "Capital": details[0][1],
        "Population": details[1][1],
        "Area(km²)": details[2][1]
    }

    rows.append(row)

print("Data processed. Writing to CSV...")

with open('country_data.csv', 'w', newline='', encoding='utf-8') as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            'Country',
            'Capital',
            'Population',
            'Area(km²)'
        ]
    )

    writer.writeheader()
    writer.writerows(rows)

print('All done !')