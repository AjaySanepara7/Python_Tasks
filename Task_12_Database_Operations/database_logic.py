from database_connections import connect_sql, connect_postgres
from psycopg2 import connect


mydb = connect_sql()
conn = connect_postgres()

mycursor = mydb.cursor()
cursor = conn.cursor()

def create_db(name,db_choice):
    try:
        if db_choice == 1:
            mycursor.execute(f"CREATE DATABASE {name}")
        else:
            conn.autocommit = True
            cursor.execute(f"CREATE DATABASE {name}")
        print("Database created\n")
    except Exception as e:
        print(f"{e}\n")

def use_db(db_name,db_choice):
    try:
        if db_choice == 1:
            mycursor.execute(f"USE {db_name}")
        else:
            try:
                conn = connect(
                dbname=db_name,
                user='postgres',
                password='ajay',
                host='localhost'
                )

                cursor = conn.cursor()

                cursor.execute("SELECT current_database();")
                current_db = cursor.fetchone()
                print(f"Connected to database: {current_db[0]}")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
        print("Database changed\n")
    except Exception as e:
        print(f"{e}\n")

def show_db(db_choice):
    if db_choice == 1:
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)
    else:
        cursor.execute("SELECT datname FROM pg_database;")
        for x in cursor:
            print(x)

def list_tbl(db_name,db_choice):
    if db_choice == 1:
        mycursor.execute(f"USE {db_name}")
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
            print(x)
    else:
        try:
            conn = connect(
                dbname=db_name,
                user='postgres',
                password='ajay',
                host='localhost'
            )

            cursor = conn.cursor()

            cursor.execute("SELECT current_database();")
            current_db = cursor.fetchone()
            print(f"Connected to database: {current_db[0]}")
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            for x in cursor:
                print(x)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


def create_tbl(db_name,tbl_name,column_values,db_choice):
    col_str = ""
    for individual_col in column_values:
        for col_detail in individual_col:
            col_str += col_detail + " "
        col_str += ","
    try:
        if db_choice == 1:
            mycursor.execute(f"USE {db_name}")
            mycursor.execute(f"CREATE TABLE {tbl_name}({col_str[:-2]})")
            print("Table created successfully\n")
        else:
            try:
                conn = connect(
                    dbname=db_name,
                    user='postgres',
                    password='ajay',
                    host='localhost'
                )

                cursor = conn.cursor()

                cursor.execute("SELECT current_database();")
                current_db = cursor.fetchone()
                print(f"Connected to database: {current_db[0]}")
                cursor.execute(f"CREATE TABLE {tbl_name}({col_str[:-2]})")
                print("Table created successfully\n")
                conn.commit() 
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
    except Exception as e:
        print(f"{e}\n")

def show_table_data(db_name,tbl_name,db_choice):
    try:
        if db_choice == 1:
            mycursor.execute(f"USE {db_name}")
            mycursor.execute(f"SELECT * FROM {tbl_name}")
            for x in mycursor:
                print(x)
        else:
            try:
                conn = connect(
                    dbname=db_name,
                    user='postgres',
                    password='ajay',
                    host='localhost'
                )

                cursor = conn.cursor()

                cursor.execute("SELECT current_database();")
                current_db = cursor.fetchone()
                print(f"Connected to database: {current_db[0]}")
                cursor.execute(f"SELECT * FROM {tbl_name}")
                for x in cursor:
                    print(x)
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
    except Exception as e:
        print(f"{e}")

def insert_into_table(db_name,tbl_name,col_names,row_values,db_choice):
    column_names = ""
    for col in col_names:
        column_names += col + ", "

    row_str = ""
    for individual_row in row_values:
        row_str += "("
        for row_index,row_val in enumerate(individual_row):
            if row_index != len(individual_row)-1:
                row_str += str(row_val) + ", "
            else:
                row_str += str(row_val)
        row_str += "),"

    try:
        if db_choice == 1:
            mycursor.execute(f"USE {db_name}")
            mycursor.execute(f"INSERT INTO {tbl_name} ({column_names[:-2]}) VALUES {row_str[:-1]}")
            mydb.commit()
            print(f"INSERT INTO {tbl_name} ({column_names[:-2]}) VALUES {row_str[:-1]}")
        else:
            try:
                conn = connect(
                    dbname=db_name,
                    user='postgres',
                    password='ajay',
                    host='localhost'
                )

                cursor = conn.cursor()

                cursor.execute("SELECT current_database();")
                current_db = cursor.fetchone()
                print(f"Connected to database: {current_db[0]}")
                cursor.execute(f"INSERT INTO {tbl_name} ({column_names[:-2]}) VALUES {row_str[:-1]}")
                conn.commit()
                print(f"INSERT INTO {tbl_name} ({column_names[:-2]}) VALUES {row_str[:-1]}")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
    except Exception as e:
        print(f"{e}\n")

def update_table(db_name,tbl_name,set_statement,where_statement,db_choice):
    try:
        if db_choice == 1:
            mycursor.execute(f"USE {db_name}")
            mycursor.execute(f"UPDATE {tbl_name} SET {set_statement} WHERE {where_statement}")
            print("Table updated successfully\n")
            mydb.commit()
        else:
            try:
                conn = connect(
                    dbname=db_name,
                    user='postgres',
                    password='ajay',
                    host='localhost'
                )

                cursor = conn.cursor()

                cursor.execute("SELECT current_database();")
                current_db = cursor.fetchone()
                print(f"Connected to database: {current_db[0]}")
                cursor.execute(f"UPDATE {tbl_name} SET {set_statement} WHERE {where_statement}")
                print("Table updated successfully\n")
                conn.commit()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
    except Exception as e:
        print(f"{e}\n")

def delete_table(db_name,tbl_name,where_statement,db_choice):
    if db_choice == 1:
        mycursor.execute(f"USE {db_name}")
        mycursor.execute(f"DELETE FROM {tbl_name} WHERE {where_statement}")
        mydb.commit()
    else:
        try:
            conn = connect(
                dbname=db_name,
                user='postgres',
                password='ajay',
                host='localhost'
            )

            cursor = conn.cursor()

            cursor.execute("SELECT current_database();")
            current_db = cursor.fetchone()
            print(f"Connected to database: {current_db[0]}")
            cursor.execute(f"DELETE FROM {tbl_name} WHERE {where_statement}")
            conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

def add_column(db_name,tbl_name,column_data,db_choice):
    try:
        if db_choice == 1:
            mycursor.execute(f"USE {db_name}")
            mycursor.execute(f"ALTER TABLE {tbl_name} ADD COLUMN {column_data}")
            print("Column added successfully\n")
        else:
            try:
                conn = connect(
                    dbname=db_name,
                    user='postgres',
                    password='ajay',
                    host='localhost'
                )

                cursor = conn.cursor()

                cursor.execute("SELECT current_database();")
                current_db = cursor.fetchone()
                print(f"Connected to database: {current_db[0]}")
                cursor.execute(f"ALTER TABLE {tbl_name} ADD COLUMN {column_data}")
                print("Column added successfully\n")
                conn.commit()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
    except Exception as e:
        print(f"{e}\n")

def drop_column(db_name,tbl_name,column_name,db_choice):
    try:
        if db_choice == 1:
            mycursor.execute(f"USE {db_name}")
            mycursor.execute(f"ALTER TABLE {tbl_name} DROP COLUMN {column_name}")
            print("Column deleted successfully\n")
        else:
            try:
                conn = connect(
                    dbname=db_name,
                    user='postgres',
                    password='ajay',
                    host='localhost'
                )

                cursor = conn.cursor()

                cursor.execute("SELECT current_database();")
                current_db = cursor.fetchone()
                print(f"Connected to database: {current_db[0]}")
                cursor.execute(f"ALTER TABLE {tbl_name} DROP COLUMN {column_name}")
                print("Column deleted successfully\n")
                conn.commit()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
    except Exception as e:
        print(f"{e}\n")

def drop_table(db_name,tbl_name,db_choice):
    try:
        if db_choice == 1:
            mycursor.execute(f"USE {db_name}")
            mycursor.execute(f"DROP TABLE {tbl_name}")
            print("Table deleted successfully\n")
        else:
            try:
                conn = connect(
                    dbname=db_name,
                    user='postgres',
                    password='ajay',
                    host='localhost'
                )

                cursor = conn.cursor()

                cursor.execute("SELECT current_database();")
                current_db = cursor.fetchone()
                print(f"Connected to database: {current_db[0]}")
                cursor.execute(f"DROP TABLE {tbl_name}")
                print("Table deleted successfully\n")
                conn.commit()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
    except Exception as e:
        print(f"{e}\n")