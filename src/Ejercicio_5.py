# Para tributar un determinado impuesto se debe ser mayor de 16 años
# y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
# y muestre por pantalla si el usuario tiene que tributar o no.

def tributarImpuesto(edad, ingreso):
    if edad <= 0 or ingreso < 0:
        return "No se pueden introducir números negativos o su edad debe ser mayor a 0"
    elif edad < 16 or ingreso < 1000:
        return "Usted no puede tributar"
    else:
        return "Usted puede tributar"

if __name__=="__main__":
    edad = int(input("Escriba su edad: "))
    ingreso = float(input("Escriba sus ingresos anuales: "))
    print(tributarImpuesto(edad, ingreso))
