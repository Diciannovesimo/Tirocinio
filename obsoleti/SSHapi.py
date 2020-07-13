import sys
import semanticscholar as sch
# autore
print("Script Python")
author = sch.author(sys.argv[1])

file = open('autore.txt' , 'w' , encoding='utf8')

file.write("INFORMAZIONI AUTORE: " + str(author))

file.write("\nNOME AUTORE: " + str(author['name']))
file.write("\nPUBBLICAZIONI DELL'AUTORE: " + str(author['papers']))
file.write("\n" + str(len(author['papers'])))
file.write("\n------------------------------------------------------")
# documento
paper = sch.paper(sys.argv[2])
file.write("\n" + str(paper.keys()))
file.write("\nTITOLO DOCUMENTO: " + str(paper['title']))
file.write("\n------------------------------------------------------")
file.write("\nNOME E ID DI TUTTI GLI AUTORI")
for author in paper['authors']:
    file.write("\n" + str(author['name']))
    file.write("\n" + str(author['authorId']))

file.close()
