import sys
from peculiar import (misma_paridad, alterna_paridad, es_peculiar, 
n_esimo_peculiar, cant_peculiares_entre)

comando:str = sys.argv[1]

if comando.lower() == "misma_paridad":
    n:int = int(sys.argv[2])
    m:int = int(sys.argv[3])
    
    if misma_paridad(n, m):
        print('sí')
    else:
        print('no')

elif comando.lower() == "alterna_paridad":
    n:int = int(sys.argv[2])
    
    if alterna_paridad(n):
        print('sí')
    else:
        print('no')

elif comando.lower() == "es_peculiar":
    n:int = int(sys.argv[2])
    
    if es_peculiar(n):
        print('sí')
    else:
        print('no')

elif comando.lower() == "n_esimo_peculiar":
    n:int = int(sys.argv[2])
    
    print(n_esimo_peculiar(n))
    
elif comando.lower() == "cant_peculiares_entre":
    n:int = int(sys.argv[2])
    m:int = int(sys.argv[3])
    
    print(cant_peculiares_entre(n, m))
    
elif comando == "--help":   
    ayuda:str = '''Comandos disponibles
    
    misma_paridad
    alterna_paridad
    es_peculiar
    n_esimo_peculiar
    cant_peculiares_entre
    '''
    print(ayuda)
    
else: 
    print("Comando no reconocido. Para ayuda comando: --help")
    