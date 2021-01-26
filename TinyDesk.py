#https://realpython.com/python-web-scraping-practical-introduction/#scrape-and-parse-text-from-websites

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

outfile = open('tables.csv', "w", newline='')
writer = csv.writer(outfile)



url = "https://en.wikipedia.org/wiki/Tiny_Desk_Concerts"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, "lxml")

#tables = soup.find_all('table')
#print(tables[0])
list_of_tables = []
for tables in soup.find_all("table"):

    list_of_rows = []
    for row in tables.find_all('tr'):
        list_of_cells = []
        for cell in row.find_all(["th","td"]):
            text = cell.text
            list_of_cells.append(text)

        list_of_rows.append(list_of_cells)

    for item in list_of_rows:
        writer.writerow(item)
        #print(' '.join(item))

#title_index = html.find("<title>")
#start_index = title_index + len("<title>")
#end_index = html.find("</title>")
#title = html[start_index:end_index]
#print(title)


#pattern = "<title.*?>.*?</title.*?>"
#match_results = re.search(pattern, html, re.IGNORECASE)
#new_title = match_results.group()
#new_title = re.sub("<.*?>", "", title)

#print(new_title)
#print(soup.get_text())
