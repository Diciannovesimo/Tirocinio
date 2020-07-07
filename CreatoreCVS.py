import sys
import semanticscholar as sch

print("Script Python")

list_of_paper = []
count = 0
MAX = int(sys.argv[1])

author = sch.author(sys.argv[2])

file = open('autore.csv' , 'w' , encoding='utf8')

for paper in author['papers']:
    if(count > MAX-1):
        break
    list_of_paper.append((count+1,author['name'],paper['year'],paper['title'],paper['paperId']))
    count+=1

file.write(str(list_of_paper))
print(list_of_paper)

file.close()
