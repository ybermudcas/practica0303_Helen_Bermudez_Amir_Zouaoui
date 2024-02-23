import pygame
#creamos la clase ladrillo con 4 parametros uno para hacer referencia al objeto , los otros dos para la posición y uno para los bloques irrompibles
class ladrillo_1:
    def __init__(self, x, y,irrompible=False):
        self.rect = pygame.Rect(x, y, 100, 20)#ponemos el ancho y atura del ladrillo
        self.irrompible = irrompible

#creamos la clase para la lista de ladrillos
class listaladrillos:
    def __init__(self):
        self.lista_ladrillos = [] #se crea una lista vacia

    def crear_ladrillos(self): #esto creara la lista de ladrillos
        for i in range(16):#cuantos bloques creara en el eje x
            for j in range(3):#cuantas filas de bloques creara en el eje y
                if i % 4 == 0 and j % 2 == 0:#crearemos algunos ladrillos irrompibles
                    ladrillo = ladrillo_1(0 + i * 100, 30 + j * 40, irrompible=True)#posicion de ladrillos y el espacio que tendran
                else:
                    ladrillo = ladrillo_1(0 + i * 100, 30 + j * 40)
                self.lista_ladrillos.append(ladrillo)#lo metera en la lista de ladrillos
        

        


              

