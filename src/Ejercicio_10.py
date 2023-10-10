# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y 
# en función de su respuesta le muestre un menú con los ingredientes disponibles para 
# que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que 
# están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
# vegetariana o no y todos los ingredientes que lleva.

def crear_pizza(tipo_pizza):
    ingredientes_comunes = ["mozzarella", "tomate"]
    if tipo_pizza == "sí":
        print("Ingredientes disponibles para pizza vegetariana: Pimiento y Tofu.")
        ingrediente_elegido = input("Elija un ingrediente: ").capitalize()
        if ingrediente_elegido in ["Pimiento", "Tofu"]:
            ingredientes_comunes.append(ingrediente_elegido)
        else:
            print("Ingrediente no válido. Se añadirá mozzarella y tomate solamente.")
    else:
        print("Ingredientes disponibles para pizza no vegetariana: Peperoni, Jamón y Salmón.")
        ingrediente_elegido = input("Elija un ingrediente: ").capitalize()
        if ingrediente_elegido in ["Peperoni", "Jamón", "Salmón"]:
            ingredientes_comunes.append(ingrediente_elegido)
        else:
            print("Ingrediente no válido. Se añadirá mozzarella y tomate solamente.")

    return ingredientes_comunes

if __name__ == "__main__":
    tipo_pizza = input("¿Quiere una pizza vegetariana? (Sí/No): ").lower()
    ingredientes = crear_pizza(tipo_pizza)
    tipo = "vegetariana" if tipo_pizza == "sí" else "no vegetariana"
    print(f"Su pizza es {tipo} y lleva los siguientes ingredientes: {', '.join(ingredientes)}")