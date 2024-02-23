import pygame

#creamos la clase ladrillo con 3 parametros uno para hacer referencia al objeto y los otros dos para la posición
class ladrillo_1:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 20)#ponemos el ancho y atura del ladrillo

#creamos la clase para la lista de ladrillos
class listaladrillos:
    def __init__(self):
        self.lista_ladrillos = [] #se crea una lista vacia

    def crear_ladrillos(self): #esto creara la lista de ladrillos
        for i in range(16):#cuantos bloques creara en el eje x
            for j in range(3):#cuantas filas de bloques creara en el eje y
                ladrillo = ladrillo_1(0 + i * 100, 30 + j * 40)#posicion de los ladrillos y el espacio que tendran
                self.lista_ladrillos.append(ladrillo)#lo metera en la lista de ladrillos
    
