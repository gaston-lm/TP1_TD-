def es_par (n:int) -> bool:
    ''' Determina si un numero es par.
        Pre: n pertenece a los enteros.
        Post: Devuelve True si n es par y False si es impar.
    '''
    vr:bool = n % 2 == 0
    return vr


def multiplo_de_22(n:int) -> bool:
    ''' Determina si n es un número múltiplo de 22
        Pre: n pertenece a los enteros.
        Post: vr equivale a si n es múltiplo de 22.
    '''    
    vr = n % 22 == 0
    return vr
    

def misma_paridad (n:int, m:int) -> bool:
    ''' Determina si tienen la misma paridad.
        Pre: n, m  pertenecen a L (donde L = naturales + 0)
        Post: vr equivale a que ambos números son pares o ambos impares
    '''
    vr:bool = es_par(n) and es_par(m) or not es_par(n) and not es_par(m)
    return vr


def alterna_paridad(n:int) -> bool:
    ''' Determina si los dígitos de n alternan su paridad.
        Pre: n pertenece a L (donde L = naturales + 0).
        Post: vr equivale a que los dígitos de n alternen su paridad.
    '''
    i:int = 1
    string_n:str = str(n)
    vr:bool = True

    # (A)
    while i < len(string_n):
        # (B)
        vr = vr and not misma_paridad(int(string_n[i-1]),int(string_n[i]))
        i = i + 1
        # (C)            
    # (D)
    return vr


def es_peculiar(n:int) -> bool:
    ''' Determina si n es lo que se considera un numero "peculiar"
        Pre: n pertenece a L (donde L = naturales + 0)
        Post: vr equivale a si n es peculiar si y solo si n es multiplo de 22
        y sus digitos alternan paridad.
    '''        
    vr:bool = multiplo_de_22(n) and alterna_paridad(n)
    return vr
            

def n_esimo_peculiar(n:int) -> bool:
    ''' Determina el n-ésimo número peculiar
        Pre: n pertence a L (donde L = naturales + 0)
        Post: vr equivale el i-ésimo peculiar
    '''
    i:int = 0 #contador del bucle
    j:int = 0 #recorido de números
    vr:int = 0
  
    # (A)
    while i < n:
        # (B)
        j = j + 1
        if es_peculiar(j):
            i = i + 1
            vr = j
        # (C)   
    # (D)
    return vr


def cant_peculiares_entre(n:int, m:int) -> int:
    ''' Determina la cantidad de números peculiares entre n y m
        Pre: n, m  pertenecen a L (donde L = naturales + 0) y n < m
        Post: vr equivale a la cantidad de números peculiares en el intervalo
        cerrado [n, m]
    '''
    vr:int = 0
    i:int = n
    # (A)
    while i <= m:
        # (B)
        if es_peculiar(i):
            vr = vr + 1
        i = i + 1    
        # (C)
    # (D)
    return vr