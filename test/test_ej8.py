from src.Ejercicio_8 import evaluarEmple

def test_evaluarEmple():
    assert evaluarEmple(0.0) == "Error, su puntuación no puede ser menor o igual que 0." 
    assert evaluarEmple(-1.2) == "Error, su puntuación no puede ser menor o igual que 0."
    assert evaluarEmple(0.3) == "Su nivel de rendimiento es Inaceptable.\nSu cantidad anual es de 720.0 €"
    assert evaluarEmple(0.4) == "Su nivel de rendimiento es Aceptable.\nSu cantidad anual es de 960.0 €"
    assert evaluarEmple(0.6) == "Su nivel de rendimiento es Meritorio.\nSu cantidad anual es de 1440.0 €"