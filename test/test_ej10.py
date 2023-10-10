from src.Ejercicio_10 import crear_pizza

def test_crear_pizza():
    ingredientes = crear_pizza("sí", "Pimiento")
    assert ingredientes == ["mozzarella", "tomate", "Pimiento"]

    ingredientes = crear_pizza("sí", "Tofu")
    assert ingredientes == ["mozzarella", "tomate", "Tofu"]

    ingredientes = crear_pizza("no", "Peperoni")
    assert ingredientes == ["mozzarella", "tomate", "Peperoni"]

    ingredientes = crear_pizza("no", "Jamón")
    assert ingredientes == ["mozzarella", "tomate", "Jamón"]

    ingredientes = crear_pizza("no", "Salmón")
    assert ingredientes == ["mozzarella", "tomate", "Salmón"]

    ingredientes = crear_pizza("sí", "Pollo")
    assert ingredientes == ["mozzarella", "tomate"]

    ingredientes = crear_pizza("no", "Cebolla")
    assert ingredientes == ["mozzarella", "tomate"]