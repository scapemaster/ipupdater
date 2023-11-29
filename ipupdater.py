#!/usr/bin/python3
#coding=utf-8

# Achtung dieses Tool funktioniert nur, wenn es auf dem Server ausgeführt wird.
# Auf dem Server muss die currentip.php installiert sein und er Pfad muss dorthin
# muss richtig eingestellt sein.
import requests

# Hier wird der Pfad zur Hauptseite eingetragen, welcher über den
# Anbieter immer mit der neuen Dyn-IP versorgt wird. Natürlich mit dem
# genauen Pfad zur currentip.php
path2currentip = 'https://your-main-domain/currentip.php'

# Welche Domain(s) soll upgedatet werden? Gib die Werte als Array-Item an.
domain = ['your-side-domain']

# Update Main-Page
page = 'main-domain-update-access'

# Passwort der Update-Mainpage
pwd = 'main-domain-update-password'

### Hier wird der request ausgeführt und die aktuelle IP-Adresse abgerufen
r         = requests.get(path2currentip)
currentip = r.text
r.close()

### Folgend wird die aktuelle IP mit der alten IP abgeglichen. 
try:
    lastaddr = open('oldip.dat','r')
    lastip   = lastaddr.readline()
    lastaddr.close()
except IOError:
    lastip = "0.0.0.0"

### gibt es Unterschiede, dann werden die requests zur erneuerung der IP durchgeführt.
if currentip != lastip:
    lastaddr = open('oldip.dat','w')
    lastaddr.write(currentip)
    lastaddr.close()
    for item in domain:
        n = requests.get('https://'+page+':'+pwd+'@dyndns.strato.com/nic/update?hostname='+item+'&myip='+currentip)
    updatedip = n.text
    n.close()
