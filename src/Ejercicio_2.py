# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contrasena_guardada = "Contrasenia123456"

def almacenaContrasenia(contrasena_usuario):
    if contrasena_usuario.lower() == contrasena_guardada.lower():
        return "Contraseña correcta. ¡Bienvenido!"
    else:
        return "Contraseña incorrecta. Intentalo de nuevo."

if __name__=="__main__":
    contrasenia = input("Escriba su contraseña: ")
    print(almacenaContrasenia(contrasenia))