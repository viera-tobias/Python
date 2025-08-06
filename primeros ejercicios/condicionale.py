

print("Ejercicio 8 . ")

num1=input("Ingrese un numero: ")
num1 = float(num1)
num2=input("Ingrese un numero: ")
num2 = float(num2)
if num1> num2 and num1 & 2 == 0: 
    print(" El numero mayor es: ", num1)

else:
    print("El numero mayor es: ", num2)

""" Pedir al usuario que escriba dos números
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))

# Comparar los números para saber cuál es mayor
if numero1 > numero2:
    mayor = numero1
elif numero2 > numero1:
    mayor = numero2
else:
    print("Los dos números son iguales:", numero1)
    if numero1 % 2 == 0:
        print("Es un número par.")
    else:
        print("Es un número impar.")
    # Termina el programa aquí si son iguales
    exit()

# Mostrar cuál es el número mayor
print("El número mayor es:", mayor)

# Ver si el número mayor es par o impar
if mayor % 2 == 0:
    print("Es un número par.")
else:
    print("Es un número impar.") """