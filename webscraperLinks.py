# import libraries
from bs4 import BeautifulSoup
import csv
import requests

# Collect first page of artists’ list
page = requests.get('http://familyvoicesal.org/resources/?category=&text=&action=List')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Create a file to write to, add headers row
f = csv.writer(open('WebScraperLinks.csv', 'w'))
f.writerow(['Name', 'Link'])

# Pull all text from the BodyText div
resource_link_list = soup.find(class_='col-sm-8')

# Pull text from all instances of <li> tag within col-sm-8 div
resource_link_list_items = resource_link_list.find_all('a')

# Create for loop to print out all resources
for resource_link in resource_link_list_items:
    # links = resource_link.contents[0]
    links = resource_link.get('a')
    # print(links)
    print(links)

        # Add each artist’s name and associated link to a row
    f.writerow([links])
