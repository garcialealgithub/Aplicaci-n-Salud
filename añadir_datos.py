import SGBD.base_datos as BD
import sqlite3


users = ["alexirius11", "tarontarantula", "gabrielichu", "manololotrap", "jotajordi", "pabpe54", "rociotrabaja5", "RocasSalvaje53", "a"]
passwords = ["ajf", "ejfh847", "jehfv34", "dfhjg35-", "jghdu738", "jdfkhgvn34", "djkhhvneuir", "dkjfhkjncs", "a"]


def poner_datos(users, passwords):
    BD.crear_tabla(tabla="security")
    for i in range(len(users)):
        x = BD.hasher(password=passwords[i])
        BD.insert_user_info(user=users[i], password=x, edad = i, sexo = "Hombre")
    BD.update_all_email_status(future_status=0)
    print("Datos añadidos correctamente")




