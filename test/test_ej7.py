from src.Ejercicio_7 import tipoImpos

def test_tipoImpos():
    assert tipoImpos(5000) == "El tipo de impositivo es del 5%"
    assert tipoImpos(15000) == "El tipo de impositivo es del 15%"
    assert tipoImpos(25000) == "El tipo de impositivo es del 20%"
    assert tipoImpos(50000) == "El tipo de impositivo es del 30%"
    assert tipoImpos(70000) == "El tipo de impositivo es del 45%"
    assert tipoImpos(-1000) == "Error, la renta anual no puede ser un número negativo"