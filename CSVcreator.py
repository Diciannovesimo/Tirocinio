import semanticscholar as sch

print("Script Python")
"""
variable declarations
count:      for the csv file
MAX:        for numbers of papers that the user want to view
author:     select an author in the semantic scholar database
name:       author name
file:       the csv file
CSVstring:  string to write to the CSV file
"""
count = 0
MAX = 78
author = sch.author('2262347')
name = author['name']
CSVstring = ""
file = open('author.csv' , 'w' , encoding='utf8')

for paper in author['papers']:

    count+=1
    CSVstring = str(count) + "," + name + "," + str(paper['year']) + "," + str(paper['title'])
    file.write(CSVstring)

    paper = sch.paper(paper['paperId'])
    for author in paper['authors']:
        if(str(author['name']) != name):
            file.write("\n")
            CSVstring = str(count) + "," + str(author['name']) + "," + str(paper['year']) + "," + str(paper['title'])
            file.write(CSVstring)

    if(count > MAX-1):
        break

    file.write("\n")

file.close()

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("http://www.di.uniba.it/~buono/paohvis/paoh.html")
time.sleep(2)

input_file = driver.find_element_by_xpath('//*[@id="inputFileOpen"]')
input_file.send_keys("D:/github/Tirocinio/author.csv")
time.sleep(2)

button = driver.find_element_by_xpath('//*[@id="btnheatmapbsp"]/span')
button.click()
