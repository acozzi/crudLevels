import funciones as f
import json

db = open('./base.json','r+')
agenda = json.load(db)




while(True):
    f.menu1()
    option = input('Elegir opción: ')
    f.handleOption(option, agenda)
