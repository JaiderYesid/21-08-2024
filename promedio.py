cantidad = int(input("Cantidad de aprendices: "))
promedio = 0

for i in range(1,cantidad):
    edad = int(input("Ingrese la edad: "))
    promedio = promedio + edad
    
promedio = promedio/cantidad
print(f"Promedio: {promedio}")