import sys

from peculiar import (misma_paridad, alterna_paridad, es_peculiar, 
n_esimo_peculiar, cant_peculiares_entre)

def procesar_llamado_por_consola():
    nombre_funcion:str = sys.argv[1]
    numero_ingresado_uno:int = int(sys.argv[2])

    if nombre_funcion == 'misma_paridad':

        numero_ingresado_dos:int = int(sys.argv[3])

        if misma_paridad(numero_ingresado_uno, numero_ingresado_dos):
            print('sí')
        else:
            print('no')

    elif nombre_funcion == 'alterna_paridad':

        if alterna_paridad(numero_ingresado_uno):
            print('sí')
        else:
            print('no')

    elif nombre_funcion == 'es_peculiar':

        if es_peculiar(numero_ingresado_uno):
            print('sí')
        else:
            print('no')

    elif nombre_funcion == 'n_esimo_peculiar':

        print(n_esimo_peculiar(numero_ingresado_uno))

    elif nombre_funcion == 'cant_peculiares_entre':

        numero_ingresado_dos:int = int(sys.argv[3])

        print(cant_peculiares_entre(numero_ingresado_uno, numero_ingresado_dos))

procesar_llamado_por_consola()