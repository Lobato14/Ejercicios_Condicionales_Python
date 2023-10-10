from src.Ejercicio_1 import edadEscrita

def test_edadEscrita():
    assert edadEscrita(-1) == "Número incorrecto"
    assert edadEscrita(0) == "Número incorrecto"
    assert edadEscrita(18) == "Es mayor de edad"
    assert edadEscrita(16) == "Es menor de edad"