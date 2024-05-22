import sqlite3, csv, bcrypt

# SET UP OF THE DATABASE

def setup_security_table_from_csv(csv_file,database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Create the table
    cursor.execute('''CREATE TABLE security(
                   user TEXT PRIMARY KEY, 
                   password TEXT NOT NULL,
                   age INT,
                   sex TEXT,
                   email TEXT,
                   everification BOOLEAN)''')
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            password = row['password']
            age = row['age']
            sex = row['sex']
            email = row['email']
            verified_email = row['verified_email']
            
            # Insert the values in a new row
            # (hashing the password before saving it in the database)
            cursor.execute('''INSERT INTO security 
                           (user, password, age, sex, email, everification)
                           VALUES (?, ?, ?, ?, ?, ?)''', 
                           (user, hasher(password), age, sex, email, verified_email))
    
    db.commit()
    db.close()
    
def setup_steps_table_from_csv(csv_file,database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Create the table
    cursor.execute('''CREATE TABLE IF NOT EXISTS steps(
                   user TEXT,
                   date TEXT,
                   steps INT,
                   PRIMARY KEY(user, date),
                   FOREIGN KEY(user) REFERENCES security(user))''')
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            date = row['date']
            steps = row['number_of_steps']
        
            # Insert the values in a new row
            cursor.execute('''INSERT INTO steps 
                           (user, date, steps) 
                           VALUES (?, ?, ?)''', 
                           (user, date, steps))
       
    db.commit()
    db.close()
    
def setup_weight_table_from_csv(csv_file,database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Create the table
    cursor.execute('''CREATE TABLE weight(
                   user TEXT,
                   date TEXT,
                   weight REAL,
                   PRIMARY KEY(user, date),
                   FOREIGN KEY(user) REFERENCES security(user))''')
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = row['user']
            date = row['date']
            weight = row['weight']
        
            # Insert the values in a new row
            cursor.execute('''INSERT INTO weight 
                           (user, date, weight) 
                           VALUES (?, ?, ?)''', 
                           (user, date, weight))
    
    db.commit()
    db.close()
    
def setup_training_table_from_csv(csv_file,database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Create the table
    cursor.execute('''CREATE TABLE training(
                   user TEXT,
                   date TEXT,
                   time TEXT,
                   duration TEXT,
                   calories INT,
                   mean_cardiac_frequency INT,
                   PRIMARY KEY(user, date, time),
                   FOREIGN KEY(user) REFERENCES security(user))''')
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            date = row['date']
            time = row['time']
            duration = row['duration']
            calories = int(row['calories_consumed']) 
            mean_cardiac_frequency = int(row['mean_cardiac_frequency'])
        
            # Insert the values in a new row
            cursor.execute('''INSERT INTO training 
                           (user, date, time, duration, calories, mean_cardiac_frequency) 
                           VALUES (?, ?, ?, ?, ?, ?)''', 
                           (user, date, time, duration, calories, mean_cardiac_frequency))
    
    db.commit()
    db.close()
    
def setup_cardiac_frequency_table_from_csv(csv_file,database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Create the table
    cursor.execute('''CREATE TABLE cardiac_frequency(
                   user TEXT,
                   date TEXT,
                   time TEXT,
                   cardiac_frequency INT,
                   PRIMARY KEY(user, date, time),
                   FOREIGN KEY(user) REFERENCES security(user))''')
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            cardiac_frequency = row['cardiac_frequency']
            date = row['date']
            time = row['time']
        
            # Insert the values in a new row
            cursor.execute('''INSERT INTO cardiac_frequency 
                           (user, date, time, cardiac_frequency) 
                           VALUES (?, ?, ?, ?)''', 
                           (user, date, time, cardiac_frequency))
    
    db.commit()
    db.close()
    
def setup_sleep_table_from_csv(csv_file,database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Create the table if it does not already exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS sleep(
                   user TEXT,
                   date TEXT,
                   quality INT,
                   duration TEXT,
                   duration_deep_sleep TEXT,
                   interruptions_counter INT,
                   PRIMARY KEY(user, date),
                   FOREIGN KEY(user) REFERENCES security(user))''')
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            date = row['date']
            quality = row['quality']
            duration = row['duration']
            duration_deep_sleep = row['duration_deep_sleep']
            interruptions_counter = row['interruptions_counter']
        
            # Insert the values in a new row
            cursor.execute('''INSERT INTO sleep 
                           (user, date, quality, duration, duration_deep_sleep, interruptions_counter) 
                           VALUES (?, ?, ?, ?, ?, ?)''', 
                           (user, date, quality, duration, duration_deep_sleep, interruptions_counter))
    
    db.commit()
    db.close()


# AUXILIARY FUNCTIONS

# Function that hashes the password of the users
def hasher(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
# Función que comprueba si el hash coincide con la contraseña (devuelve True o False)
def comprobar_hash(password, hashed_password):
    comprobacion = bcrypt.checkpw(password.encode(), hashed_password)
    return comprobacion

# Buscar que hace
def password_verification(usuario):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    consulta = f"SELECT password FROM security WHERE user = ?;"
    cursor.execute(consulta, (usuario,))
    resultado = cursor.fetchone()
    db.commit()
    db.close()

    if resultado:
        return resultado[0]
    else:
        return "Usuario no encontrado"


# WRITTING TO DATABASE FUNCTIONS

# update multiple rows of a table
# (update the database through csv files)
# Useful when a user is registrating, adding a lot of data at once...
def update_security_table_from_csv(csv_file, database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            password = row['password']
            age = row['age']
            sex = row['sex']
            email = row['email']
            verified_email = row['verified_email']
            
            # Verify that there is not already a row with the same primary key
            cursor.execute('''SELECT * FROM security WHERE user = ?''', (user))
            existing_row = cursor.fetchone()
            
            # Insert the values in a new row
            if existing_row is None:
                cursor.execute('''INSERT INTO security 
                               (user, password, age, sex, email, everification)
                               VALUES (?, ?, ?, ?, ?, ?)''', 
                               (user, hasher(password), age, sex, email, verified_email))
        
    db.commit()
    db.close()
    
def update_steps_table_from_csv(csv_file, database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            date = row['date']
            steps = row['number_of_steps']
        
            # Verify that there is not already a row with the same primary key
            cursor.execute('''SELECT * FROM steps WHERE user = ? AND date = ?''',
                           (user, date))
            existing_row = cursor.fetchone()
            
            # Insert the values in a new row
            if existing_row is None:
                cursor.execute('''INSERT INTO steps 
                               (user, date, steps) 
                               VALUES (?, ?, ?)''', 
                               (user, date, steps))
    
    db.commit()
    db.close()
    
def update_weight_table_from_csv(csv_file, database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = row['user']
            date = row['date']
            weight = row['weight']
        
            # Verify that there is not already a row with the same primary key
            cursor.execute('''SELECT * FROM weight WHERE user = ? AND date = ?''', 
                           (user, date))
            existing_row = cursor.fetchone()
            
            # Insert the values in a new row
            if existing_row is None:
                cursor.execute('''INSERT INTO weight 
                               (user, date, weight) 
                            VALUES (?, ?, ?)''', 
                                  (user, date, weight))
    
    db.commit()
    db.close()
    
def update_training_table_from_csv(csv_file, database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            date = row['date']
            time = row['time']
            duration = row['duration']
            calories = int(row['calories_consumed']) 
            mean_cardiac_frequency = int(row['mean_cardiac_frequency'])
        
            # Verify that there is not already a row with the same primary key
            cursor.execute('''SELECT * FROM training WHERE user = ? AND date = ? AND time = ?''', 
                           (user, date, time))
            existing_row = cursor.fetchone()
            
            # Insert the values in a new row
            if existing_row is None:
                cursor.execute('''INSERT INTO training 
                               (user, date, time, duration, calories, mean_cardiac_frequency) 
                               VALUES (?, ?, ?, ?, ?, ?)''', 
                               (user, date, time, duration, calories, mean_cardiac_frequency))
       
    db.commit()
    db.close()
    
def update_cardiac_frequency_table_from_csv(csv_file, database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            cardiac_frequency = row['cardiac_frequency']
            date = row['date']
            time = row['time']
        
             # Verify that there is not already a row with the same primary key
            cursor.execute('''SELECT * FROM cardiac_frequency WHERE user = ? AND date = ?''', 
                           (user, date))
            existing_row = cursor.fetchone()
            
            # Insert the values in a new row
            if existing_row is None:
                cursor.execute('''INSERT INTO cardiac_frequency 
                               (user, date, time, cardiac_frequency) 
                               VALUES (?, ?, ?, ?)''', 
                               (user, date, time, cardiac_frequency))
    
    db.commit()
    db.close()
    
def update_sleep_table_from_csv(csv_file, database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Open the csv file and copy the data to the database
    # We select the right encoding to fix some troubles reading accents
    with open(csv_file, 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Select the values of the csv
            user = row['user']
            date = row['date']
            quality = row['quality']
            duration = row['duration']
            duration_deep_sleep = row['duration_deep_sleep']
            interruptions_counter = row['interruptions_counter']
        
             # Verify that there is not already a row with the same primary key
            cursor.execute('''SELECT * FROM sleep WHERE user = ? and date = ?''', 
                           (user, date))
            existing_row = cursor.fetchone()
            
            # Insert the values in a new row
            if existing_row is None:
                cursor.execute('''INSERT INTO sleep 
                               (user, date, quality, duration, duration_deep_sleep, interruptions_counter)
                               VALUES (?, ?, ?, ?, ?, ?)''', 
                               (user, date, quality, duration, duration_deep_sleep, interruptions_counter))
    
    db.commit()
    db.close()


# update a row of a table
# (update some value(s) related to an user)
# Useful when a user wants to correct wrong data
def update_security_table_row(user, password=None, age=None, sex=None, email=None, verified_email=None, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Initialize lists to hold parts of the SQL query
    fields = []
    values = []

    # Fill the lists
    if password is not None:
        fields.append("password = ?")
        values.append(password)
    if age is not None:
        fields.append("age = ?")
        values.append(age)
    if sex is not None:
        fields.append("sex = ?")
        values.append(sex)
    if email is not None:
        fields.append("email = ?")
        values.append(email)
    if verified_email is not None:
        fields.append("everification = ?")
        values.append(verified_email)

    # Add the user to the end of the values list
    values.append(user)

    # Create the SQL query and execute it
    if fields:
        sql_query = f"UPDATE security SET {', '.join(fields)} WHERE user = ?"
        cursor.execute(sql_query, values)
        db.commit()

    db.close()

def update_steps_table_row(user, date, steps, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query and execute it
    sql_query = f"UPDATE steps SET steps = ? WHERE user = ? AND date = ?"
    cursor.execute(sql_query, (steps, user, date))
    db.commit()
    db.close()
    
def update_sleep_table_row(user, date, quality=None, duration=None, duration_deep_sleep=None, interruptions=None, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Initialize lists to hold parts of the SQL query
    fields = []
    values = []

    # Fill the lists
    if quality is not None:
        fields.append("quality = ?")
        values.append(quality)
    if duration is not None:
        fields.append("duration = ?")
        values.append(duration)
    if duration_deep_sleep is not None:
        fields.append("duration_deep_sleep = ?")
        values.append(duration_deep_sleep)
    if interruptions is not None:
        fields.append("interruptions = ?")
        values.append(interruptions)

    # Add the user and date to the end of the values list
    values.append(user)
    values.append(date)

    # Create the SQL query and execute it
    if fields:
        sql_query = f"UPDATE sleep SET {', '.join(fields)} WHERE user = ? AND date = ?"
        cursor.execute(sql_query, values)
        db.commit()

    db.close()

def update_training_table_row(user, date, time, duration=None, calories_consumed=None, mean_cardiac_frequency=None, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Initialize lists to hold parts of the SQL query
    fields = []
    values = []

    # Fill the lists
    if duration is not None:
        fields.append("duration = ?")
        values.append(duration)
    if calories_consumed is not None:
        fields.append("calories_consumed = ?")
        values.append(calories_consumed)
    if mean_cardiac_frequency is not None:
        fields.append("mean_cardiac_frequency = ?")
        values.append(mean_cardiac_frequency)

    # Add the user and date to the end of the values list
    values.append(user)
    values.append(date)
    values.append(time)

    # Create the SQL query and execute it
    if fields:
        sql_query = f"UPDATE training SET {', '.join(fields)} WHERE user = ? AND date = ? AND time = ?"
        cursor.execute(sql_query, values)
        db.commit()

    db.close()

def update_weight_table_row(user, date, weight, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query and execute it
    sql_query = f"UPDATE weight SET weight = ? WHERE user = ? AND date = ?"
    cursor.execute(sql_query, (weight, user, date))
    db.commit()
    db.close()
    
def update_cardiac_frequency_table_row(user, date, time, cardiac_frequency, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query and execute it
    sql_query = f"UPDATE cardiac_frequency SET cardiac_frequency = ? WHERE user = ? AND date = ? AND time = ?"
    cursor.execute(sql_query, (cardiac_frequency, user, date, time))
    db.commit()
    db.close()


# add a row to a table
# Useful when a user wants to add new data
def add_security_table_row(user, password=None, age=None, sex=None, email=None, verified_email=None, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Initialize lists to hold parts of the SQL query
    fields = []
    values = []

    # Fill the lists
    if password is not None:
        fields.append("password = ?")
        values.append(password)
    if age is not None:
        fields.append("age = ?")
        values.append(age)
    if sex is not None:
        fields.append("sex = ?")
        values.append(sex)
    if email is not None:
        fields.append("email = ?")
        values.append(email)
    if verified_email is not None:
        fields.append("everification = ?")
        values.append(verified_email)

    # Add the user to the end of the values list
    values.append(user)

    # Create the SQL query and execute it
    if fields:
        sql_query = f"UPDATE security SET {', '.join(fields)} WHERE user = ?"
        cursor.execute(sql_query, values)
        db.commit()

    db.close()

def add_steps_table_row(user, date, steps, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query and execute it
    sql_query = f"UPDATE steps SET steps = ? WHERE user = ? AND date = ?"
    cursor.execute(sql_query, (steps, user, date))
    db.commit()
    db.close()
    
def add_sleep_table_row(user, date, quality=None, duration=None, duration_deep_sleep=None, interruptions=None, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Initialize lists to hold parts of the SQL query
    fields = []
    values = []

    # Fill the lists
    if quality is not None:
        fields.append("quality = ?")
        values.append(quality)
    if duration is not None:
        fields.append("duration = ?")
        values.append(duration)
    if duration_deep_sleep is not None:
        fields.append("duration_deep_sleep = ?")
        values.append(duration_deep_sleep)
    if interruptions is not None:
        fields.append("interruptions = ?")
        values.append(interruptions)

    # Add the user and date to the end of the values list
    values.append(user)
    values.append(date)

    # Create the SQL query and execute it
    if fields:
        sql_query = f"UPDATE sleep SET {', '.join(fields)} WHERE user = ? AND date = ?"
        cursor.execute(sql_query, values)
        db.commit()

    db.close()

def add_training_table_row(user, date, time, duration=None, calories_consumed=None, mean_cardiac_frequency=None, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Initialize lists to hold parts of the SQL query
    fields = []
    values = []

    # Fill the lists
    if duration is not None:
        fields.append("duration = ?")
        values.append(duration)
    if calories_consumed is not None:
        fields.append("calories_consumed = ?")
        values.append(calories_consumed)
    if mean_cardiac_frequency is not None:
        fields.append("mean_cardiac_frequency = ?")
        values.append(mean_cardiac_frequency)

    # Add the user and date to the end of the values list
    values.append(user)
    values.append(date)
    values.append(time)

    # Create the SQL query and execute it
    if fields:
        sql_query = f"UPDATE training SET {', '.join(fields)} WHERE user = ? AND date = ? AND time = ?"
        cursor.execute(sql_query, values)
        db.commit()

    db.close()

def add_weight_table_row(user, date, weight, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query and execute it
    sql_query = f"UPDATE weight SET weight = ? WHERE user = ? AND date = ?"
    cursor.execute(sql_query, (weight, user, date))
    db.commit()
    db.close()
    
def add_cardiac_frequency_table_row(user, date, time, cardiac_frequency, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query and execute it
    sql_query = f"UPDATE cardiac_frequency SET cardiac_frequency = ? WHERE user = ? AND date = ? AND time = ?"
    cursor.execute(sql_query, (cardiac_frequency, user, date, time))
    db.commit()
    db.close()


# delete a row from a table
# Useful when a user wants to delete data
def delete_security_table_row(user, database='database.db'):
    db = sqlite3.connect(database.db)
    cursor = db.cursor()

    # Create the SQL query to delete the row based on the user (primary key)
    sql_query = f"DELETE FROM security WHERE user = ?"

    # Execute the query and commit the changes
    cursor.execute(sql_query,user)
    db.commit()
    db.close()

def delete_steps_table_row(user, date, database='database.db'):
    db = sqlite3.connect(database.db)
    cursor = db.cursor()

    # Create the SQL query to delete the row based on the user and date (primary key)
    sql_query = f"DELETE FROM steps WHERE user = ? AND date = ?"

    # Execute the query and commit the changes
    cursor.execute(sql_query,(user,date))
    db.commit()
    db.close()
    
def delete_sleep_table_row(user, date, database='database.db'):
    db = sqlite3.connect(database.db)
    cursor = db.cursor()

    # Create the SQL query to delete the row based on the user and date (primary key)
    sql_query = f"DELETE FROM sleep WHERE user = ? AND date = ?"

    # Execute the query and commit the changes
    cursor.execute(sql_query,(user,date))
    db.commit()
    db.close()

def delete_training_table_row(user, date, time, database='database.db'):
    db = sqlite3.connect(database.db)
    cursor = db.cursor()

    # Create the SQL query to delete the row based on the user, date and time (primary key)
    sql_query = f"DELETE FROM training WHERE user = ? AND date = ? AND time = ?"

    # Execute the query and commit the changes
    cursor.execute(sql_query,(user,date,time))
    db.commit()
    db.close()
    
def delete_weight_table_row(user, date, database='database.db'):
    db = sqlite3.connect(database.db)
    cursor = db.cursor()

    # Create the SQL query to delete the row based on the user and date (primary key)
    sql_query = f"DELETE FROM weight WHERE user = ? AND date = ?"

    # Execute the query and commit the changes
    cursor.execute(sql_query,(user,date))
    db.commit()
    db.close()
    
def delete_cardiac_frequency_table_row(user, date, time, database='database.db'):
    db = sqlite3.connect(database.db)
    cursor = db.cursor()

    # Create the SQL query to delete the row based on the user, date and time (primary key)
    sql_query = f"DELETE FROM cardiac_frequency WHERE user = ? AND date = ? AND time = ?"

    # Execute the query and commit the changes
    cursor.execute(sql_query,(user,date,time))
    db.commit()
    db.close()


# drop a table
def drop_table(table, database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Execute the sql query
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    db.commit()
    db.close()
    
    print(f"La tabla '{table}' ha sido eliminada")

# drop an user
def drop_user(user, database="database.db"):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    
    # Execute the sql query for every table
    cursor.execute("DELETE FROM security WHERE user = ?", (user))
    db.commit()
    db.close()
    
    try:
        cursor.execute("DELETE FROM steps WHERE user = ?", (user))
        db.commit()
        db.close()
    
    except:
        print("El usuario no tiene pasos registrados")   
     
    try:
        cursor.execute("DELETE FROM training WHERE user = ?", (user))
        db.commit()
        db.close()
    
    except:
        print("El usuario no tiene entrenamientos registrados")
        
    try:
        cursor.execute("DELETE FROM weight WHERE user = ?", (user))
        db.commit()
        db.close()
    
    except:
        print("El usuario no tiene pesos registrados")
    try:
        cursor.execute("DELETE FROM cardiac_frequency WHERE user = ?", (user))
        db.commit()
        db.close()
    
    except:
        print("El usuario no tiene frecuencias cardíacas registradas")
    try:
        cursor.execute("DELETE FROM sleep WHERE user = ?", (user))
        db.commit()
        db.close()
    
    except:
        print("El usuario no tiene datos de sueño registrados")
        

# READING FROM THE DATABASE

def get_security_table_row(user, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query to select row based on the primary key
    sql_query = "SELECT * FROM security WHERE user = ?"
    cursor.execute(sql_query, (user,))
    row = cursor.fetchone()  # Fetch the first row
    db.close()

    return row  # Return the fetched row

def get_steps_table_row(user, date, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query to select row based on the primary key
    sql_query = "SELECT * FROM steps WHERE user = ? AND date = ?"
    cursor.execute(sql_query, (user,date))
    row = cursor.fetchone()  # Fetch the first row
    db.close()

    return row  # Return the fetched row
    
def get_sleep_table_row(user, date, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query to select row based on the primary key
    sql_query = "SELECT * FROM sleep WHERE user = ? AND date = ?"
    cursor.execute(sql_query, (user, date))
    row = cursor.fetchone()  # Fetch the first row
    db.close()

    return row  # Return the fetched row

def get_training_table_row(user, date, time, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query to select row based on the primary key
    sql_query = "SELECT * FROM training WHERE user = ? AND date = ? AND time = ?"
    cursor.execute(sql_query, (user, date, time))
    row = cursor.fetchone()  # Fetch the first row
    db.close()

    return row  # Return the fetched row

def get_weight_table_row(user, date, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query to select row based on the primary key
    sql_query = "SELECT * FROM weight WHERE user = ? AND date = ?"
    cursor.execute(sql_query, (user, date))
    row = cursor.fetchone()  # Fetch the first row
    db.close()

    return row  # Return the fetched row
    
def get_cardiac_frequency_table_row(user, date, time, database='database.db'):
    db = sqlite3.connect(database)
    cursor = db.cursor()

    # Create the SQL query to select row based on the primary key
    sql_query = "SELECT * FROM cardiac_frequency WHERE user = ? AND date = ? AND time = ?"
    cursor.execute(sql_query, (user, date, time))
    row = cursor.fetchone()  # Fetch the first row
    db.close()

    return row  # Return the fetched row