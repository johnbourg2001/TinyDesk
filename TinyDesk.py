#https://realpython.com/python-web-scraping-practical-introduction/#scrape-and-parse-text-from-websites

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

outfile = open('tables.csv', "w", encoding = "utf-8", newline='')
writer = csv.writer(outfile)



url = "https://en.wikipedia.org/wiki/Tiny_Desk_Concerts"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, "lxml")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
list_of_tables = []
for tables in soup.find_all("table"):

    list_of_rows = []

    for row in tables.find_all('tr'):

        list_of_cells = []

        cells = row.find_all("td")

        if len(cells)==2  and (cells[0].text.split(' ')[0] in months):
            print(cells[0].text)
            list_of_cells.append(cells[1].text)


        list_of_rows.append(list_of_cells)

    for item in list_of_rows:
        writer.writerow(item)
