def menu1():
    print('-----------------')
    print('-1_ Create ------')
    print('-2_ Read --------')
    print('-3_ Update ------')
    print('-4_ Delete ------')
    print('-----------------')

def handleOption(option, agenda):
    if option == '1':
        createContact()
    elif option == '2':
        readContact(agenda)
    elif option == '3':
        updateContact()
    elif option == '4':
        deleteContact()
    else:
        defaultError()


def createContact():
    print('Crear Contacto')

def readContact(agenda):
    print('Mostar Contacto')
    numero = input('Ingrese el Nro de Contacto:')
    print(agenda[int(numero)]['name'])

def updateContact():
    print('Actualizar Contacto')

def deleteContact():
    print('borrar Contacto')

def defaultError():
    print('La opción seleccionada no es válida',menu1())

