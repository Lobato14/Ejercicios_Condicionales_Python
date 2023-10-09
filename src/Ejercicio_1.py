# Escribir un programa que pregunte al usuario su edad y 
# muestre por pantalla si es mayor de edad o no.

def edadEscrita(edad):
    if edad <= 0:
        return "Número incorrecto"
    elif edad < 18:
        return "Es menor de edad"
    elif edad >= 18 and edad <= 120:
        return "Es mayor de edad"
    else:
        return "Número incorrecto"

if __name__=="__main__":
    while True:
        try:
            edad = int(input("Escribe su edad: "))
            print(edadEscrita(edad))
            if edad > 0:
                break
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    