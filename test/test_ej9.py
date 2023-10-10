from src.Ejercicio_9 import mostrarPrecio

def test_mostrarPrecio():
    assert mostrarPrecio(-1) == "Error, no se puede introducir un número menor a 0."
    assert mostrarPrecio(0) == "Error, no se puede introducir un número menor a 0."
    assert mostrarPrecio(3) == "¡Puedes entrar gratis!"
    assert mostrarPrecio(10) == "Debes pagar 5 €"
    assert mostrarPrecio(25) == "Debes pagar 10 €"
    assert mostrarPrecio(18) == "Debes pagar 10 €"