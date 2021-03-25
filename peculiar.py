'''
Funciones
    - misma_paridad
    - alterna_paridad
    - es_peculiar
    - n_esimo_peculiar
    - cant_peculiares_entre
    
'''
def es_par (n:int) -> str:
    
    

def misma_paridad (n:int, m:int) -> str:
    '''
    Dados n; m que pertenecen a L (donde L= naturales + 0), determina
    si n y m son ambos pares, o bien ambos impares
    Precondición: n, m >=0
    Postcondición: imprime 'sí' si ambos números son pares/impares e imprime
       es 'no' si la paridad de los númemros es distinta
    '''
    if n % 2 == 0 and m % 2 == 0:
        print('sí')
    elif  n % 2 == 1 and m % 2 == 1:
        print('sí')
    else:
        print('no')
'''
PREGUNTAR SI HAY QUE HACER QUE DIGA ERROR CUANDO LE METES CON COMA
'''
n:int = 494.544
m:int = 54546546.65464564

misma_paridad(n, m)

# def alterna_paridad (n:int) -> str:
#     '''
#     Dado n perteneciente a L (donde L= naturales + 0),  determina si los 
#     dígitos de n alternan su paridad 1 a 1
#     Precondición: n >=0
#     Postcondición: imrprime 'sí' si los dígitos alternan su paridad y si no,
#     imprime 'no'
#     '''

# i=0
# if i=0 repetir hasta len(n):
#     'hola'[i]
#     i = i + 1

        
    