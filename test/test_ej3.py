from src.Ejercicio_3 import divisionDosNum

def test_dividionDosNum():
    assert divisionDosNum(-1, -8) == "El número no puede ser menor a 0."
    assert divisionDosNum(4, 2) == "El resultado es: 2.0"
    assert divisionDosNum(0, 2) == "El resultado es: 0.0"
    assert divisionDosNum(4, 0) == "Error: No se puede dividir por cero."
