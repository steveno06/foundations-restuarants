#!/usr/local/bin/python3
import cgi
class Res:
    def __init__(self, loc, name):
        self.loc = loc
        self.name = name


def getInfo():
    info = []
    
    with open('restuarants.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            resLoc = line.split(',')
            info.append(Res(resLoc[0], resLoc[1]))
            line = reader.readline()
    return(info)

def makeList():
    pairs = getInfo()
    con = ""
    for x in range(0, len(pairs)):
        name = (pairs[x]).name
        loc = (pairs[x]).loc
        con = con + "<li>{} {}</li>".format(name, loc)

    return(con)





content = ("""<html>
        
        <body>
        <header>
        <h1>Berlin Restaurants</h1>
        </header>
        <main>
        <ul>
        {}
        </ul>
        </main>
        </body>
        </html>""").format(makeList())


f= open("index.html","w+")
f.write(content)
f.close() 






