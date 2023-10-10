# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y 
# el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla 
# el grupo que le corresponde.

def divisionGrupo(nombre, sexo):
    primera_letra = nombre[0].lower()
    if sexo == "M":
        if primera_letra < "m":
            grupo = "A"
        else:
            grupo = "B"
    else:
        if primera_letra > "n":
            grupo = "A"
        else:
            grupo = "B"
    return grupo
if __name__ == "__main__":
    nombre = input("Escribe tu nombre: ")
    sexo = input("¿Cuál es tu sexo (M o H)?: ")
    resultado = divisionGrupo(nombre, sexo)
    print("El grupo que te corresponde es el" + resultado)