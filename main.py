import funciones as f
import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'

respuesta = requests.get(url)
agenda = respuesta.json()

while(True):
    f.menu1()
    option = input('Elegir opción: ')
    f.handleOption(option, agenda)
