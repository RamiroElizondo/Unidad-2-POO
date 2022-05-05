from numpy import False_
from ManejadorIntegrantes import ManejadorIntegrante
from ManejadorProyecto import ManejadorProyecto


if __name__ == '__main__':
    manejadorI = ManejadorIntegrante()
    manejadorP = ManejadorProyecto()
    manejadorI.cargarArregloI()
    manejadorP.cargarListaP()
    lista = manejadorP.obtener()
    puntajes: list[int] = []
    i:int=0
    for proyecto in lista:
        p1:int=manejadorI.calcular1(proyecto)
        #print('Punto 1:{}'.format(p1))
        p2:int=manejadorI.calcular2(proyecto)
        #print('Punto 2:{}'.format(p2))
        p3:int=manejadorI.calcular3(proyecto)
        #print('Punto 3:{}'.format(p3))
        valor1=manejadorI.calcular4(proyecto)
        valor2=manejadorI.calcular5(proyecto)
        p4:int=0
        if valor1 == False or valor2 == False:
            p4:int=-10
        #print('Punto 4:{}'.format(p4))
        totalP = p1+p2+p3+p4
        puntajes.append(totalP)
        i+=1
    print(puntajes)