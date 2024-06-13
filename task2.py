import requests
from bs4 import BeautifulSoup
import csv
import json
def scrape_website(url, output_format='csv'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_list = []
    headlines = soup.find_all('h2', class_='headline')
    for headline in headlines:
        data_list.append(headline.text.strip())
    if output_format == 'csv':
        with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Headline'])
            for data in data_list:
                writer.writerow([data])
        print("Data has been saved to output.csv")
    elif output_format == 'json':
        with open('output.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data_list, jsonfile, ensure_ascii=False, indent=4)
        print("Data has been saved to output.json")
    else:
        print("Invalid output format. Please choose either 'csv' or 'json'.")
scrape_website('https://www.reddit.com/?rdt=47026', output_format='csv')
scrape_website('https://www.reddit.com/?rdt=47026', output_format='json')