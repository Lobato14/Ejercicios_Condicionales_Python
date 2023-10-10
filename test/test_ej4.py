from src.Ejercicio_4 import numParImpar

def test_numParImpar():
    assert numParImpar(0) == "0 es un número par"
    assert numParImpar(-1) == "-1 no es un número entero"
    assert numParImpar(2) == "2 es un número par"
    assert numParImpar(13) == "13 es un número impar"