# import libraries
from bs4 import BeautifulSoup
import csv
import requests

# Collect first page of artists’ list
page = requests.get('http://familyvoicesal.org/resources/?category=&text=&action=List')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Create a file to write to, add headers row
f = csv.writer(open('WebScraper.csv', 'w'))
f.writerow(['Name', 'Link'])

# Pull all text from the BodyText div
resource_name_list = soup.find(class_='col-sm-8')

# Pull text from all instances of <li> tag within col-sm-8 div
resource_name_list_items = resource_name_list.find_all('li')

# Create for loop to print out all resources
for resource_name in resource_name_list_items:
    names = resource_name.contents[0]
    # links = resource_name.get('a')
    print(names)
    # print(links)

        # Add each artist’s name and associated link to a row
    f.writerow([names])
