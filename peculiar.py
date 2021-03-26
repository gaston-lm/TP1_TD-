'''
Funciones 
    - misma_paridad
    - alterna_paridad
    - es_peculiar
    - n_esimo_peculiar
    - cant_peculiares_entre
    
'''
def es_par (n:int) -> str:
    """Dice si un numero es par.
       Pre: Ninguna
       Post: Devuelve True si n es par y False si es impar.
    """
    vr:bool = (n % 2 == 0)
    return vr
    

def misma_paridad (n:int, m:int) -> str:
    '''
    Dados n; m que pertenecen a L (donde L = naturales + 0), determina
    si n y m son ambos pares, o si bien alguno no es impar.
    Precondición: n, m >=0
    Postcondición: imprime 'sí' si ambos números son pares/impares e imprime
       es 'no' si la paridad de los númemros es distinta
    '''
    if es_par(n) and es_par(m) or not es_par(n) and not es_par(m):
        #print("sí")
        return True  
    else:
        return False
        #print('no')
'''
PREGUNTAR SI HAY QUE HACER QUE DIGA ERROR CUANDO LE METES CON COMA
'''
n:int = 1212
m:int = 5555

if misma_paridad(n, m) == True:
    print("sí")
else:
    print("no")

def alterna_paridad (n:int) -> str:
    '''
    Dado n perteneciente a L (donde L= naturales + 0),  determina si los 
    dígitos de n alternan su paridad 1 a 1
    Precondición: n >= 0
    Postcondición: imprime 'sí' si los dígitos alternan su paridad y "no"
    si no lo hacen.
    '''
    #Predicado invariante
    i:int = 0
    #vt:int = 0
    
    while i != len(str(n)):
        
        str(n) [i]
        i = i + 1
        print(i)
        #este print es para checkear que
        #analice todas las cifras de n
        if not misma_paridad(i, i+1) == True:
            # vt:int = vt + 1
            # if vt == n:
            #     print(vt)
            return
        else:
            return False   
        return True
    
#Mostrar q el ciclo termina en word
        
#si todos son True, entonces el n alterna paridad
#Como hacemos para que checkee que todos son True en el while?
#actualmente con un solo while te tira q todo bien

if alterna_paridad(n) == True:
    print("sí(alternan paridad)")
else: 
    print("no(no alternan paridad)")

def es_peculiar(n:int) -> str:
    ''' 
    Determina si n es lo que se considera un numero "peculiar".
    Precondición: n >= 0 (n pertenece a L = naturales + 0)
    Postcondición: 
    '''        
    if n % 22 == 1:
        print
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    