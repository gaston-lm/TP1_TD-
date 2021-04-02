'''
Funciones 
    - misma_paridad
    - alterna_paridad
    - es_peculiar
    - n_esimo_peculiar
    - cant_peculiares_entre
    
'''

def es_par (n:int) -> bool:
    '''
    Dice si un numero es par.
    Pre: Ninguna
    Post: Devuelve True si n es par y False si es impar.
    '''
    vr:bool = (n % 2 == 0)
    return vr
    

def misma_paridad (n:int, m:int) -> bool:
    '''
    Determina si tienen la misma paridad.
    Pre: n, m  pertenecen a L (donde L = naturales + 0)
    Post: vr equivale a que ambos números son pares o impares
    '''

    vr:bool = es_par(n) and es_par(m) or not es_par(n) and not es_par(m)
    return vr


def alterna_paridad(n:int) -> bool:
    '''
    Determina si los dígitos de n alternan su paridad
    Pre: n >= 0 (n pertenece a L = naturales + 0)
    Predicado invariante: 1 <= i <= len(n)
                          vr equivale a que los dígitos  de n alternan 
                          su paridad hasta el analisis en la posición i
    Post: vr equivale a que los dígitos de n alternen su paridad después de i
    '''
    i:int = 0
    string_n:str = str(n)
    vr:bool = True
    #a
    while i <= len(string_n):
        #b
        vr = vr and not misma_paridad(int(string_n[i]),int(string_n[i+1]))
        i = i + 1
        #c            
    return vr
    #d


def es_peculiar(n:int) -> bool:
    ''' 
    Determina si n es lo que se considera un numero "peculiar"
    Precondición: n >= 0 (n pertenece a L = naturales + 0)
    Postcondición: vr = n es peculiar si y solo si n es multiplo de 22
    y sus digitos alternan paridad
    '''        
    vr:bool = n % 22 == 0 and alterna_paridad(n)
    return vr
            

def n_esimo_peculiar(n:int) -> bool:
    '''
    Determina el n-ésimo número peculiar
    Pre: n >= 0 (n pertenece a L = naturales + 0)
    Post: vr = el n-ésimo peculiar
    '''
    i:int = 0 #Contador de n-ésimos peculiares 
    j:int = 0
    vr:int = 0
    
    while i < n:
        
        j = j + 1
        vr = j * 22
        if alterna_paridad(vr):
            i = i + 1 
    #c        
    return vr
            

def cant_peculiares_entre(n:int, m:int) -> int:
    '''
    Determina la cantidad de números peculiares entre n y m
    Pre: n, m  pertenecen a L (donde L = naturales + 0)
    Post: vr equivale a la cantidaad de números peculiares entre n y m
    '''
    vr:int = 0
    while n <= m:
        
        if es_peculiar(n):
            vr = vr + 1
        n = n + 1    
        
    return vr
