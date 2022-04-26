import csv
from ViajeroFrecuente import ViajeroFrecuente


def test():
    objetoP = ViajeroFrecuente(250, 24941821, 'Ramiro', 'Elizondo', 1500)
    print('Prueba: {}'.format(objetoP.muestra()))
    print('Cantidad: {}'.format(objetoP.cantidadTotalMillas()))
    print('Acumula: {}'.format(objetoP.acumularMillas(1500)))
    print('Canjeo: {}'.format(objetoP.canjerarMillas(2000)))


def buscar(listaobjeto, num, cont):
    j = 0
    while j < cont and num != listaobjeto[j].getnumero():
        j = j+1
    return j


if __name__ == "__main__":
    test()
    with open("Datos.txt", 'r', encoding='utf8') as archivo:
        listaobjetos = []
        cont = 0
        reader = csv.reader(archivo, delimiter=',')
        for lineaA in reader:
            objeto = ViajeroFrecuente(int(lineaA[0]), (lineaA[1]), (lineaA[2]), lineaA[3], int(lineaA[4]))
            listaobjetos.append(objeto)
            cont += 1

    # print(cont)

    numero = int(input('Ingrese el numero de viajero frecuente: '))
    posicion = buscar(listaobjetos, numero, cont)

    if posicion < cont:
        f'Encontrado: posicion: {cont}'
    else:
        print('No coinciden'.center(20, '-'))

    # print(posicion)
    # print(listaobjetos[posicion])

    opcion = None
    while opcion != 'd':
        print('Menu Cuaderno'.center(30, '-'))
        print('a- Consultar Cantidad de Millas')
        print('b- Acumular Millas')
        print('c- Canjear Millas')
        print('d- Salir')
        opcion = input('Tu opcion: ')
        if opcion == 'a':
            cant1 = listaobjetos[posicion].cantidadTotalMillas()
            print('La cantidad total de millas acumuladas es {}\n'.format(cant1))
        elif opcion == 'b':
            cant2 = int(input('Ingrese la cantidad de millas recorridas: '))
            valor1 = listaobjetos[posicion].acumularMillas(cant2)
            print('Valor actualizado de las millas: {}\n'.format(valor1))
        elif opcion == 'c':
            cant3 = int(input('Ingrese la cantidad de millas a canjear: '))
            valor2 = listaobjetos[posicion].canjerarMillas(cant3)
            print('Valor de cantidad de millas acumuladas: {}\n'.format(valor2))
        elif opcion == 'd':
            print('Salimos del programa'.center(30, '-'))
        elif opcion != 'a' and opcion != 'b' and opcion != 'c' and opcion != 'd':
            print('Opcion no valida'.center(30, '-'))
