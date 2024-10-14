from database_logic import create_db
from database_logic import use_db
from database_logic import show_db
from database_logic import list_tbl
from database_logic import create_tbl
from database_logic import show_table_data
from database_logic import insert_into_table
from database_logic import update_table
from database_logic import delete_table
from database_logic import add_column
from database_logic import drop_column
from database_logic import drop_table

db = 1
while db == 1:
    db_choice = int(input("Select a database you want to use\n"
                          "1)  MySQL\n"
                          "2)  PostgreSQL\n"
                          "0)  Exit\n"))

    if db_choice == 1 or db_choice == 2:
        choice = 1
        while choice != 0:
            choice = int(input("Select an operation\n"
                        "1) Create Database\n"
                        "2) Open Existing Database\n"
                        "3) List All the Existing Database\n"
                        "4) List All the Tables of specific Database\n"
                        "5) Create New Table into Database\n"
                        "6) Display Data of Table\n"
                        "7) Insert Records into Table\n"
                        "8) Update Records of Table\n"
                        "9) Delete Records from Table\n"
                        "10) Add New Column into Table\n"
                        "11) Delete Existing column from Table\n"
                        "12) Drop the Table\n"
                        "0) Exit\n"
                        ))


            if choice == 1:
                db_name = input("Enter database name:\n")
                create_db(db_name,db_choice)

            if choice == 2:
                db_name = input("Enter database name:\n")
                use_db(db_name,db_choice)

            if choice == 3:
                show_db(db_choice)

            if choice == 4:
                db_name = input("Enter database name:\n")
                list_tbl(db_name,db_choice)

            if choice == 5:
                db_name = input("Enter database name:\n")
                tbl_name = input("Enter table name:\n")
                tbl_row = input("Enter column in the format column_name, datatype, constraint\n").split(",")
                col_val_list = []
                for values in tbl_row:
                    col_val_list.append(f"{values}")
                column_values = []
                column_values.append(col_val_list)
                col = True
                while col == True:
                    col_choice = int(input("1)  to enter column\n"
                                    "0)  Exit \n"))
                    if col_choice == True:
                        tbl_row = input("Enter column in the format column_name, datatype, constraint\n").split(",")
                        col_val_list2 = []
                        for values in tbl_row:
                            col_val_list2.append(f"{values}")
                        column_values.append(col_val_list2)
                        print(column_values)
                    if col_choice == 0:
                        col = False
                create_tbl(db_name,tbl_name,column_values,db_choice)

            if choice == 6:
                db_name = input("Enter database name\n")
                tbl_name = input("Enter table name\n")
                show_table_data(db_name,tbl_name,db_choice)

            if choice == 7:
                db_name = input("Enter database name\n")
                tbl_name = input("Enter table name\n")
                col_names = input("Enter column names in the format col_1, col_2, col_3...\n").split(",")
                row_val_list = input("Enter row values in appropriate format separated by ','\n").split(",")
                row_values = []
                row_values.append(row_val_list)
                row_val = True
                while row_val == True:
                    row_choice = int(input("1)  to enter row values\n"
                                        "0)  Exit\n"))
                    if row_choice == True:
                        row_val_list2 = input("Enter column in the format column_name, datatype, constraint\n").split(",")
                        row_values.append(row_val_list2)
                    if row_choice == 0:
                        row_val = False
                print(row_values)
                insert_into_table(db_name,tbl_name,col_names,row_values,db_choice)

            if choice == 8:
                db_name = input("Enter database name\n")
                tbl_name = input("Enter table name\n")
                set_statement = input("Write the set condition without the set keyword\n")
                where_statement = input("Write the where condition without the where keyword\n")
                update_table(db_name,tbl_name,set_statement,where_statement,db_choice)

            if choice == 9:
                db_name = input("Enter database name\n")
                tbl_name = input("Enter table name\n")
                where_statement = input("Write the where condition without the where keyword\n")
                delete_table(db_name,tbl_name,where_statement,db_choice)

            if choice == 10:
                db_name = input("Enter database name\n")
                tbl_name = input("Enter table name\n")
                column_data = input("Enter column data in the format column_name datatype constraint\n"
                                    "NOTE:  The data must be separated by space/' '\n")
                add_column(db_name,tbl_name,column_data,db_choice)

            if choice == 11:
                db_name = input("Enter database name\n")
                tbl_name = input("Enter table name\n")
                column_name = input("Enter column name\n")
                drop_column(db_name,tbl_name,column_name,db_choice)

            if choice == 12:
                db_name = input("Enter database name\n")
                tbl_name = input("Enter table name\n")
                drop_table(db_name,tbl_name,db_choice)


    if db_choice == 0:
        db = 0