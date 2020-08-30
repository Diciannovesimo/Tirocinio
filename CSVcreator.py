import semanticscholar as sch
import time
from selenium import webdriver

print("Analisi di rilevanza di articoli scientifici mediante visualizzazioni")
"""
variable declarations
count:              ID for every paper
numbers_of_papers:  for numbers of papers that the user want to view
MAX:                number of documents the author has written
author:             select an author in the semantic scholar database
name:               author name
file:               the csv file
CSVstring:          string to write to the CSV file
auth_name_file:     name of the file, compose of iD and author name
team:               group of people who worked on the same document
"""
print("inserisci l'id dell'autore che si vuole analizzare")
print("esempio: Turing 2262347")

iD_auth = input()
author = sch.author(iD_auth)
try:
    MAX = int(len(author['papers']))
    pass
except KeyError:
    print("Numero autore non valido: " + iD_auth)
    print("Il programma verrà interrotto...")
    time.sleep(2)
    exit()


print("quanti documenti scientifici vuoi analizzare?")
print("documenti totali di questo autore: " + str(MAX))
numbers_of_papers = int(input())
if(numbers_of_papers < 0 or numbers_of_papers > MAX):
    print("Numero non valido, verranno analizzati tutti i documenti")
    numbers_of_papers = MAX

count = 0
name = author['name']
CSVstring = ""
auth_name_file = iD_auth + '_' + name + '_author.csv'
file = open( auth_name_file, 'w' , encoding='utf8')

print("Analisi in corso...")
for paper in author['papers']:

    paper_year = paper['year']
    if(paper_year != None):
        paper_title = str(paper['title'])
        paper_title = paper_title.replace(',','')

        count+=1
        CSVstring = str(count) + "," + name + "," + str(paper_year) + "," + paper_title
        file.write(CSVstring)

        paper = sch.paper(paper['paperId'])
        team = "team_" + str(count)
        for author in paper['authors']:
            if(str(author['authorId']) != iD_auth):
                file.write("\n")
                CSVstring = str(count) + "," + str(author['name']) + "," + str(paper_year) + "," + paper_title + "," + team
                file.write(CSVstring)

        print("Analisi documento numero: " + str(count))
        if(count > numbers_of_papers-1):
            print("Analisi completata")
            break

        file.write("\n")
    else:
        print("Questo documento: " + str(paper['title']) + " ha una data invalida")
        count+=1
        if(count > numbers_of_papers-1):
            print("Analisi completata")
            break
        else:
            count-=1
            numbers_of_papers-=1


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
time.sleep(2)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("http://www.di.uniba.it/~buono/paohvis/paoh.html")
time.sleep(2)

input_file = driver.find_element_by_xpath('//*[@id="inputFileOpen"]')
input_file.send_keys("D:/github/Tirocinio/" + auth_name_file)


button = driver.find_element_by_xpath('//*[@id="btnheatmapbsp"]/span')
button.click()
print("apertura del sito completata")
print("sul sito è disponibile la visualizzazione dei documenti")
