# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y 
# en función de su respuesta le muestre un menú con los ingredientes disponibles para 
# que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que 
# están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
# vegetariana o no y todos los ingredientes que lleva.

def crear_pizza(tipo_pizza, ingrediente_elegido=None):
    ingredientes_comunes = ["mozzarella", "tomate"]
    if tipo_pizza == "sí":
        print("Ingredientes disponibles para pizza vegetariana: Pimiento y Tofu.")
        if ingrediente_elegido and ingrediente_elegido.capitalize() in ["Pimiento", "Tofu"]:
            ingredientes_comunes.append(ingrediente_elegido.capitalize())
        else:
            print("Ingrediente no válido. Se añadirá mozzarella y tomate solamente.")
    else:
        print("Ingredientes disponibles para pizza no vegetariana: Peperoni, Jamón y Salmón.")
        if ingrediente_elegido and ingrediente_elegido.capitalize() in ["Peperoni", "Jamón", "Salmón"]:
            ingredientes_comunes.append(ingrediente_elegido.capitalize())
        else:
            print("Ingrediente no válido. Se añadirá mozzarella y tomate solamente.")

    return ingredientes_comunes

if __name__ == "__main__":
    tipo_pizza = input("¿Deseas una pizza vegetariana? (sí/no): ").lower()
    ingrediente_elegido = input("Elige un ingrediente (pimiento/tofu/peperoni/jamón/salmón): ").capitalize()
    ingredientes_pizza = crear_pizza(tipo_pizza, ingrediente_elegido)
    if tipo_pizza == "sí":
        print("Has elegido una pizza vegetariana con los siguientes ingredientes:")
    else:
        print("Has elegido una pizza no vegetariana con los siguientes ingredientes:")
    
    print(", ".join(ingredientes_pizza))
    