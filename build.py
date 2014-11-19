#-*-coding: utf-8 -*-
import json
f = open('country-source.txt', 'r')
text = f.read()
obj = json.loads(text)
f.close()
newlist = list()
# you can build your json

for e in obj:
    for el in e["callingCode"]:
        if el:
            #print el
            nset = {}
            nset["en"]=e["name"]
            nset["call"]= el
            nset["cca3"]= e["cca3"]
            nset["ja"]=e["translations"]["ja"]
            nset["ch"]=e["translations"]["ch"]
            newlist.append(nset)
        
    #print e["translations"]["ja"]

a = open('country.json','w')
ttt = json.dumps(newlist)
a.write(ttt)
a.close()
