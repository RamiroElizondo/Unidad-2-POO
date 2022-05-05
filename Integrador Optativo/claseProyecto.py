class Proyecto:
    __idProyecto:str = ""
    __titulo:str = ""
    __palabrasClaves:str = ""
    def __init__(self, id:str, titulo:str, palabras:str):
        self.__idProyecto = id
        self.__titulo = titulo
        self.__palabrasClaves = palabras
    
    def getIdProyecto(self):
        return self.__idProyecto