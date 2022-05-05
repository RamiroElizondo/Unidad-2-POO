#lista
import csv
from claseProyecto import Proyecto


class ManejadorProyecto:
    __listaobjetos: list[Proyecto]
    def __init__(self):
        self.__listaobjetos = []
    
    def cargarListaP(self):
        with open("Integrador Optativo\proyectos.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Proyecto(linea[0],linea[1],linea[2])
                self.__listaobjetos.append(objeto)
    
    def obtener(self):
        lista = []
        for proyecto in self.__listaobjetos:
            lista.append(proyecto.getIdProyecto())
        return lista