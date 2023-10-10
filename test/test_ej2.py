from src.Ejercicio_2 import almacenaContrasenia

def test_almacenaContrasenia():
    assert almacenaContrasenia("Contrasenia123456") == "Contraseña correcta. ¡Bienvenido!"
    assert almacenaContrasenia("123") == "Contraseña incorrecta. Intentalo de nuevo."
    assert almacenaContrasenia("Contrasenia") == "Contraseña incorrecta. Intentalo de nuevo."
    assert almacenaContrasenia(" ") == "Contraseña incorrecta. Intentalo de nuevo."
    assert almacenaContrasenia("\n") == "Contraseña incorrecta. Intentalo de nuevo."