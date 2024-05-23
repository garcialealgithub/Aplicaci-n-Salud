import database_functions as BD

#Setup of all the tables
try:
    BD.setup_security_table_from_csv("app_salud/data_csv/security.csv")
    BD.setup_steps_table_from_csv("app_salud/data_csv/steps.csv")
    BD.setup_training_table_from_csv("app_salud/data_csv/training.csv")
    BD.setup_sleep_table_from_csv("app_salud/data_csv/sleep.csv")
    BD.setup_weight_table_from_csv("app_salud/data_csv/weight.csv")
    BD.setup_cardiac_frequency_table_from_csv("app_salud/data_csv/cardiac_frequency.csv")

except:
    print("Base de datos ya iniciada anteriormente")

else:
    print("Base de datos iniciada con éxito")


