from src.Ejercicio_6 import divisionGrupo

def test_divisionGrupo():
    assert divisionGrupo("Alice", "M") == "A"
    assert divisionGrupo("Michael", "H") == "B"
    assert divisionGrupo("Maria", "M") == "B"
    assert divisionGrupo("Nathan", "H") == "B"
    assert divisionGrupo("Zara", "M") == "B"