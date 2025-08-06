#strings o cadenas de texto

nombre ="Tu nombre"
apellido = 'Apellido'

print(nombre + "y" + apellido)

texto = "Este texto \n tiene salto de línea y \t tabulación"
print(texto)

#formateo

user, password, email="Emanuel",54321, "quete@importa.com"
print("Su usuario y contrasela son {} {} y su email {}".format(user,password,email))
print("Su usuario y contrasela son %s %d y su email %s"%(user,password,email))
print("Su usuario y contrasela son "+ user +" "+str(password) + "y su email"+email)
print(f"Su usuario y contraseña son {user} {password} y email {email}")