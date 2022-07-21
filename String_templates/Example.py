'''
Created on 2 may. 2020

@author: RSSpe
'''
#Importamos string porque el template no esta por default y tenemos que cargarlo
import string

template = string.Template('$player choose $character in $mode')

#Sustituyendo valores en el Template usando 'substitute()', esta funcion toma valores y los etablece en key=value

print(template.substitute(player='Ricardo', character="Sigmund", mode="Hero"))

#Si no tenemos todos los valores para dar en el template podemos usar 'safe_substitute()' para que no genere error
print(template.safe_substitute(player='Ricardo', character="Sigmund"))

#Una ventaja es que podemos llamar al template y poner valores diferentes para asi reusarlo

#-----------------------------------------------------------------

#Tambien podemos sustituir valores guardandolos en un diccionario
diccionario = {'player':'Ricardo', 'character':'Sigmund', 'mode':'Hero'}

print(template.substitute(diccionario))