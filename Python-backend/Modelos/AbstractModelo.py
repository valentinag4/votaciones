from abc import ABCMeta

#Manipular objetos de manera independiente para nuestro modelo ok
class AbstractModelo(metaclass=ABCMeta):
    #data hace referencia a un diccionario, self es una palabra reservada para acceder a atributos y metodos de una clase
    def __init__(self, data):
        #lee items del elemento data (llave y valor)
        for llave, valor in data.items():
            #Establece el valor a un atributo como una cadena
            setattr(self, llave, valor)