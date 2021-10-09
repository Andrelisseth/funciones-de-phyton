#Para la resta utilizar 2 paramentros y verificar con un if que el 
#primer paramentro sea mayor que el segundo

def resta(n1,n2):
    if n1>n2:
        return n1-n2
    else:
        return 0
 
capturadatosdefuncion = resta(6,1)

if capturadatosdefuncion ==0:
    print("No queremos mostrar numeros negativos")
else:
    print(capturadatosdefuncion)
