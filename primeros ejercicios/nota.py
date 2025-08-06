#promedio y estado
notas =[]
Tam = 3
sumatoria = 0

for x in range(Tam):
    nota = 0
    while nota < 1 or nota > 5:
        nota = int(input(f"Nota: {x + 1}: "))

    notas.append(nota)

for x in range(len(notas)):
    sumatoria = sumatoria + notas[x]


print("----------------ESTADISTICAS--------------------")
print(F"Promedio: {sumatoria/ Tam}")
estado =""
if (float(sumatoria/Tam) > 1.7):
    estado  ="APROBADO"
else:
    estado = "REPROBADO"

print(f"Estado: {estado}")
