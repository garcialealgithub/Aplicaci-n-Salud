import SGBD.base_datos as BD


users = ["alexirius11", "tarontarantula", "gabrielichu", "manololotrap", "jotajordi", "pabpe54", "rociotrabaja5", "RocasSalvaje53"]
passwords = ["ajf", "ejfh847", "jehfv34", "dfhjg35-", "jghdu738", "jdfkhgvn34", "djkhhvneuir", "dkjfhkjncs"]

"""
BD.crear_tabla(tabla="security")
for i in range(len(users)):
    x = BD.hasher(password=passwords[i])
    BD.insert_user_info(user = users[i], password=x)
"""

for i in range(len(users)):
    BD.update_all_users_status(future_status=0)

