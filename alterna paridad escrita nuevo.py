
def es_par (n:int) -> str:
    """Dice si un numero es par.
       Pre: Ninguna
       Post: Devuelve True si n es par y False si es impar.
    """
    vr:bool = (n % 2 == 0)
    return vr


def misma_paridad(n:int, m:int) ->bool:
    vr:bool=(es_par(n) and es_par(m) or not es_par(n) and not es_par(m))
    return vr


#Recorrer s de izq a der
#revisar que cada cifra alterne la paridad con la anterior
#si alternan todas las cifras es True

def alterna_paridad(n:int) ->bool:
    """determina si los dígitos de n alternan su paridad
    Pre: n >= 0 (n pertenece a L = naturales + 0)
    Predicado invariante: 1 <= i <= len(n)
                          vr equivale a que los dígitos  de n alternan 
                          su paridad hasta el analisis en la posición i
    Post: vr equivale a que los dígitos de n alternen su paridad después de i
    """
    i:int = 0
    string_n:str = str(n)
    vr:bool = True
    #a
    while i < len(string_n)-1:
        #b
        print(string_n[i])
        print(string_n[i+1])
        
        vr = vr and not misma_paridad(int(string_n[i]),int(string_n[i+1]))
        i = i + 1
        #c            
    return vr
    #d
print(alterna_paridad(2589))
