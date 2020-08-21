import semanticscholar as sch
import time
from selenium import webdriver

print("Analisi di rilevanza di articoli scientifici mediante visualizzazioni")
"""
variable declarations
count:         for the csv file
numbers_paper: for numbers of papers that the user want to view
MAX:           number of documents the author has written
author:        select an author in the semantic scholar database
name:          author name
file:          the csv file
CSVstring:     string to write to the CSV file
"""
print("inserisci l'id dell'autore che si vuole analizzare")
print("esempio: Turing 2262347")

number_auth = input()
author = sch.author(number_auth)
try:
    MAX = int(len(author['papers']))
    pass
except KeyError:
    print("Numero autore non valido: " + number_auth)
    print("Il programma verrà interrotto...")
    time.sleep(3)
    exit()


print("quanti documenti scientifici vuoi analizzare?")
print("documenti totali di questo autore: " + str(MAX))
numbers_paper = int(input())
if(numbers_paper < 0 or numbers_paper > MAX):
    print("Numero non valido, verranno analizzati tutti i documenti")
    numbers_paper = MAX

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
    if(count > numbers_paper-1):
        print("Analisi completata")
        break

    file.write("\n")

file.close()

"""
variable declarations
option:     for optimize the windows that will be opened
driver:     to get url and elements of the site, which will be used
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
