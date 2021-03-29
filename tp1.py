from peculiar import misma_paridad

def alterna_paridad (n:int) -> str:
    ''' Dado n perteneciente a L (donde L= naturales + 0),  determina si los 
        dígitos de n alternan su paridad
        Precondición: n >= 0
        Postcondición: imprime 'sí' si los dígitos alternan su paridad y "no"
        si no lo hacen.
    '''
    i:int = 0
    string_n:str = str(n)
    vr:bool = True
    print(len(string_n))
    #1244
    #len 4
    while i < len(string_n)-1:
        
        print(string_n[i])
        print(string_n[i+1])

        vr = vr and not misma_paridad(int(string_n[i]),int(string_n[i+1]))
        i = i + 1
            

    return vr
        
print(alterna_paridad(1234))
