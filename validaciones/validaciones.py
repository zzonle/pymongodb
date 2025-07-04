def nombre_valido(nombre: str):
    nombre = nombre.strip()
    if not nombre:
        return False
    if len(nombre) < 3:
        return False
    if not nombre.isalpha():
        return False
    return True

def email_valido(email: str):
    email = email.strip()
    if not email:
        return False
    if "@" not in email or "." not in email:
        return False
    if len(email) < 5:
        return False
    return True

def telefono_valido(telefono: str):
    telefono = telefono.strip()
    if not telefono:
        return False
    if len(telefono) < 9 or len(telefono) > 12:
        return False
    if not telefono.isdigit():
        return False
    return True



