# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

def divisionDosNum(numero1, numero2):
    if numero2 == 0:
        return "Error: No se puede dividir por cero."
    elif numero1 < 0 or numero2 < 0:
        return "El número no puede ser menor a 0."
    else:
        resultado = numero1 / numero2
        return "El resultado es: " + str(resultado)

if __name__=="__main__":
    numero1 = int(input("Escriba un número: "))
    numero2 = int(input("Escriba un número: "))
    print(divisionDosNum(numero1, numero2))