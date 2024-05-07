import bcrypt
from inicio_sesion import Login

# Crear una instancia de la clase Login
inicio_sesion = Login()

# Llamar al método login() de la instancia
contraseña = inicio_sesion.login()[1]
print(contraseña)

def hash_password(contraseña):
    hashed_password = bcrypt.hashpw(contraseña.encode("utf-8"), bcrypt.gensalt())
    return hashed_password
    
def verify_password(hashed_password, contraseña):
    return bcrypt.checkpw(contraseña.encode("utf-8"), hashed_password)
