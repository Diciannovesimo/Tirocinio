import sys
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
MAX = int(sys.argv[1])
author = sch.author(sys.argv[2])
name = author['name']
CSVstring = ""
file = open('author.csv' , 'w' , encoding='utf8')

for paper in author['papers']:

    count+=1
    CSVstring = str(count) + "," + name + "," + str(paper['year']) + "," + str(paper['title']) + "," + str(paper['paperId'])
    print(CSVstring)
    file.write(CSVstring)

    if(count > MAX-1):
        break

    file.write("\n")

file.close()
