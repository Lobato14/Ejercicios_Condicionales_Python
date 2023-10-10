from src.Ejercicio_5 import tributarImpuesto

def test_tributarImpuesto():
    assert tributarImpuesto(16, 100.0) == "Usted no puede tributar"
    assert tributarImpuesto(0, -1.4) == "No se pueden introducir números negativos o su edad debe ser mayor a 0"
    assert tributarImpuesto(-4, 0) == "No se pueden introducir números negativos o su edad debe ser mayor a 0"
    assert tributarImpuesto(15, 1500.50) == "Usted no puede tributar"
    assert tributarImpuesto(18, 1500.50) == "Usted puede tributar"