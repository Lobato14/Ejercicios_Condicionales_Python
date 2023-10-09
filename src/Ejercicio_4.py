# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es par o impar.

def numParImpar(numero):
    if numero < 0:
        return str(numero) + " no es un número entero"
    elif numero % 2 == 0:
        return str(numero) + " es un número par."
    else:
        return str(numero) + " es un número impar."

if __name__=="__main__":
    numero = int(input("Escribe un número entero: "))
    print(numParImpar(numero))