#operadores aritmeticos
#imprimir la suma de 3 + 4
print("La suma de 10 + 4 es: ", 10+4)

#resolver todas las operaciones : 10-4, 10*4, 10/4, 10%4, 10//4, 10**4
print("La resta de 10 - 4 es: ", 10-4)
print("La multiplicación de 10 x 4 es: ", 10*4)
print("La diviasio de 10 por 4 es: " ,10 /4)
print("El modulo de 10 por 4 es: " ,10 %4)
print("La diviasio sin decimal  de 10 por 4 es: " ,10 //4)
print("Diez potencia de cuatro es: " ,10 **4)


import math
#resuelve las ecuaciones cuadraticas: 2x²-7x+3=0
a=2
b=-7
c=3

# Calculamos el discriminante
discriminante = b**2 - 4*a*c

# Verificamos si hay soluciones reales
if discriminante >= 0:
 # Calculamos las dos soluciones
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")
else:
    print("La ecuación no tiene soluciones reales.")

#operaciones con cadenas de texto
print("snpp"+"ctfppj"+"programación python")
print("aula"+ "2102")

#operaciones mixtas
print("tun chi" * 5)
print("ja" *(2 ** 3))

#operadores de comparacion
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#operadores con cadenas de texto
print("python" >"PYTHON")
print("aaa" >="abaa")#operaciones alfabetica por ascii
print(len("aaa") >= len("abaa"))#cuenta caracteres

print("python" != "PYTHON")

### operadores lógicos
print(10> 4 and "Z">"A")
print(10> 4 or "Z">"A")
print(not(10>4)and"Z">"A")