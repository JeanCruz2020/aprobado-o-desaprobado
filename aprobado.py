#Ejercicio que determina si un estudiante 
#esta aprobado o no

def determinaraprobado(promedio):
    if promedio <=10.5:
        resultado = "ALUMNO DESAPROBADO"
    
    else:
         resultado = "ALUMNO APROBADO"
         
    return resultado

promedio = float(input ("Promedio: "))
print(determinaraprobado(promedio))