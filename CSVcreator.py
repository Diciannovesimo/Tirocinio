import semanticscholar as sch

print("Analisi di rilevanza di articoli scientifici mediante visualizzazioni")
"""
variable declarations
count:      for the csv file
MAX:        for numbers of papers that the user want to view
author:     select an author in the semantic scholar database
name:       author name
file:       the csv file
CSVstring:  string to write to the CSV file
"""
print("inserisci l'id dell'autore che si vuole analizzare")
print("esempio: Turing 2262347")
number_auth = input()
author = sch.author(number_auth)

print("quanti documenti scientifici vuoi analizzare?")
print("documenti totali di questo autore: " + str(len(author['papers'])))
MAX = int(input())
if(MAX < 0):
    MAX = int(len(author['papers']))

count = 0
name = author['name']
CSVstring = ""
file = open('author.csv' , 'w' , encoding='utf8')

print("Analisi in corso...")
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

    print("Analisi documento numero: " + str(count))
    if(count > MAX-1):
        print("Analisi completata")
        break

    file.write("\n")

file.close()


import time
from selenium import webdriver

"""
variable declarations
option:
driver:
time:       waiting time between calls
input_file: csv file
button:     element of the paohvis site
"""
print("apertura del sito paohvis in corso...")
time.sleep(4)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("http://www.di.uniba.it/~buono/paohvis/paoh.html")
time.sleep(1)

input_file = driver.find_element_by_xpath('//*[@id="inputFileOpen"]')
input_file.send_keys("D:/github/Tirocinio/author.csv")
time.sleep(1)

button = driver.find_element_by_xpath('//*[@id="btnheatmapbsp"]/span')
button.click()
print("apertura del sito completata")
print("sul sito è disponibile la visualizzazione dei documenti")
