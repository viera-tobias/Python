edad = int (input("Ingres se edad    \n" ) )
print(f"Usted teine {edad}  años " )
'''
cuando utilizamos { },
dabe tener "f" al princpio
'''
if edad >= 18  and edad < 60 :
    print("Usted es mayor de edad, Acceda a la licencia de adulto ")
elif edad > 18 and edad >= 16:
    print("Usted es menor de edad, Licencia de menor ")
else:
    print("Usted esno puede tener aun licencia de conducir ")