import datos
from inicio_sesion import Login


users = datos.usuarios
 

def user_verification(users):
    login_verfication = Login()
    users_info = login_verfication.login_info()
    print(users_info)


user_verification(users)