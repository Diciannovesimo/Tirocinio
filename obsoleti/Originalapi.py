import semanticscholar as sch
# autore
author = sch.author(2262347)
print("INFORMAZIONI AUTORE: ", author)
print("NOME AUTORE: ", author['name'])
print("PUBBLICAZIONI DELL'AUTORE: ", author['papers'])
print(len(author['papers']))
print("------------------------------------------------------")
# documento
paper = sch.paper('ab7790485f26ce65f9d83dd700c43e49058bdd2b')
print(paper.keys())
print("TITOLO DOCUMENTO: ", paper['title'])
print("------------------------------------------------------")
print("NOME E ID DI TUTTI GLI AUTORI")
for author in paper['authors']:
    print(author['name'])
    print(author['authorId'])

sch.restful
