import pyodbc as p 
import prettytable as pretty
def Pretty_table(lst):
    newTable = pretty.PrettyTable(["Id","Products_Name","Products_Price","Products_Count"]) 
    for i in lst:
        newTable.add_row(i)
    print(newTable)
def Pretty_table_for_usernames(lst):
    newTable = pretty.PrettyTable(["usernames"]) 
    for i in lst:
        newTable.add_row(i)
    print(newTable)

def Select_All_products():
    cursor = Creating_conn_string()
    cursor.execute("select * from products")
    Pretty_table(cursor)

def Creating_conn_string_1():
    connect = p.connect('Driver={SQL Server};'
    'Server=DESKTOP-OJ10FUF;'
    'Trusted_Connection=yes;',autocommit=True)
    cursor = connect.cursor()  
    return cursor

def Creating_conn_string():
    connect = p.connect('Driver={SQL Server};'
    'Server=DESKTOP-OJ10FUF;'
    'DataBase=STORE;'
    'Trusted_Connection=yes;',autocommit=True)
    cursor = connect.cursor()  
    return cursor

def Check_database():
    cursore = Creating_conn_string()
    cursore.execute("select count(*) from sys.databases where name = 'STORE'")
    for i in cursore:
        pass
    return i[0]

def Create_database():
    cursor = Creating_conn_string_1()
    if Check_database() == 1 :
        pass
    else:
        cursor.execute("create database STORE")
    cursor.close()

def Check_table():
    cursore = Creating_conn_string()
    cursore.execute(f"select count(*) from INFORMATION_SCHEMA.TABLES where TABLE_name = 'products'")
    for i in cursore:
        pass
    return i[0] 

def Create_table():
    cursor = Creating_conn_string()
    if Check_table() == 1 :
        pass
    else:
        cursor.execute("CREATE TABLE Products (ID int NOT NULL,Products_Name varchar(255),Products_Price int,Products_Count int,PRIMARY KEY (ID))")
    cursor.close()

def Buy_by_Id(Id,username):
    cursor = Creating_conn_string()
    cursor.execute(f"select * from products where Id = {Id} ")
    lst=[]
    for i in cursor:
        lst.append(i)
    cursor.execute(f"INSERT INTO {username}(ID,Products_Name,Products_Price,Products_Count) Values({lst[0][0]},'{lst[0][1]}',{lst[0][2]},{lst[0][3]})") 

def Buy_by_name(name,username):
    cursor = Creating_conn_string()
    cursor.execute(f"select * from products where products_name = '{name}' ")
    lst=[]
    for i in cursor:
        lst.append(i)
    print(cursor)
    print(lst)
    cursor.execute(f"INSERT INTO {username}(ID,Products_Name,Products_Price,Products_Count) Values({lst[0][0]},'{lst[0][1]}',{lst[0][2]},{lst[0][3]})")

def Buy_by_price(price,username):
    cursor = Creating_conn_string()
    cursor.execute(f"select * from products where products_price = {price} ")
    lst=[]
    for i in cursor:
        lst.append(i)
    cursor.execute(f"INSERT INTO {username}(ID,Products_Name,Products_Price,Products_Count) Values({lst[0][0]},'{lst[0][1]}',{lst[0][2]},{lst[0][3]})")

def Buy_by_count(count,username):
    cursor = Creating_conn_string()
    cursor.execute(f"select * from products where products_count = {count} ")
    lst=[]
    for i in cursor:
        lst.append(i)
    print(lst)
    cursor.execute(f"INSERT INTO {username}(ID,Products_Name,Products_Price,Products_Count) Values({lst[0][0]},'{lst[0][1]}',{lst[0][2]},{lst[0][3]})")

def Create_table_by_user_name(username):
    if Check_table_by_username(username) == 1 :
        pass
    else:
        cursor = Creating_conn_string()
        cursor.execute(f"CREATE TABLE {username} (ID int NOT NULL,Products_Name varchar(255),Products_Price int,Products_Count int,PRIMARY KEY (ID))")
        cursor.close()
    
def Check_table_by_username(username):
    cursore = Creating_conn_string()
    cursore.execute(f"select count(*) from INFORMATION_SCHEMA.TABLES where TABLE_name = '{username}'")
    for i in cursore:
        print(i)
    return i[0] 

def Select_All_by_username(username):
    cursor = Creating_conn_string()
    cursor.execute(f"select * from {username}")
    Pretty_table(cursor)
    
def Buy(username):    
    print("STORE:")
    Select_All_products()
    print("YOR CART:")
    Select_All_by_username(username)
    flag = True
    while flag:
        choice = input("enter a eterbuit to buy(Id,name,count,price):")
        value = input(f"enter a {choice} to buy:")
        if choice == "Id":
            Buy_by_Id(value,username)
            flag = False
        elif choice =="name":
            Buy_by_name(value,username)
            flag = False
        elif choice =="count":
            Buy_by_count(value,username)
            flag = False
        elif choice =="price":
            Buy_by_price(value,username)
            flag = False
        else:
            "error in typing"
        Select_All_by_username(username)
        if input("Do you want to continue(y/n)?") == "n" :flag = False 
        else : pass        
    
def Show_all_usernames():
    cursor = Creating_conn_string()
    cursor.execute("SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_name != 'products'")
    Pretty_table_for_usernames(cursor)
 
def Factors():
    cursor = Creating_conn_string()
    Show_all_usernames()
    choice = input("enter a username to show factor:")
    print("FACTOR:")
    Select_All_by_username(choice)
    cursor.close()
     
def Insert_to_table():    
    Select_All_products()
    cursor = Creating_conn_string()
    ID,name,price,count = int(input("enter an Id:")),input("enter a name:"),int(input("enter a price:")),int(input("enter a count:"))
    cursor.execute(f"INSERT INTO Products(ID,Products_Name,Products_Price,Products_Count) Values({ID},'{name}',{price},{count})") 
    Select_All_products()
    cursor.close()  
     
def Delete():
    Select_All_products()
    cursor = Creating_conn_string()
    choice = input("delete with wich one (Id,products_name,products_price,products_count):")
    if choice == "Id" :
        delete = int(input(f"Enter an Id for delete:"))
        cursor.execute(f"Delete from products where {choice}={delete}")
    elif choice == "product_name":
        delete = input(f"Enter a product_name for delete:")
        cursor.execute(f"Delete from products where {choice}='{delete}'")
    else:
        delete = int(input(f"Enter a {choice} for delete:"))
        cursor.execute(f"Delete from products where {choice}={delete}")
    Select_All_products()
    cursor.close()

def Update_by_id():
    Select_All_products()
    crusor = Creating_conn_string()
    id = int(input("enter a id to update:"))
    new_name,new_price,new_count = input("enter a new name to update:"),int(input("enter a new price to update:")),int(input("enter a new count to update:"))
    crusor.execute(f"Update products set Products_name='{new_name}',Products_price={new_price},Products_count={new_count} where ID={id}")
    Select_All_products()
    crusor.close()

def Update_by_name():
    Select_All_products()
    crusor = Creating_conn_string()
    name = input("enter a name to update:")
    new_name = input("enter a  new name to update:")
    crusor.execute(f"Update products set Products_name='{new_name}' where Products_name='{name}'")
    Select_All_products()
    crusor.close()

def Update_by_count():
    Select_All_products()
    crusor = Creating_conn_string()
    count = input("enter a count to update:")
    new_count = input("enter a new count to update:")
    crusor.execute(f"Update products set Products_count={new_count} where Products_count={count}")
    Select_All_products()
    crusor.close()

def Update_by_price():
    Select_All_products()
    crusor = Creating_conn_string()
    price = input("enter a price to update:")
    new_price = input("enter a new price to update:")
    crusor.execute(f"Update products set Products_price={new_price} where Products_price={price}")
    Select_All_products()
    crusor.close()

def Edit():
    flag = True
    while flag:
        choice = input("enter a etterbuite to edit(Id,name,count,price):")
        if choice == "Id":
            Update_by_id()
            flag = False
        elif choice =="name":
            Update_by_name()
            flag = False
        elif choice =="count":
            Update_by_count()
            flag = False
        elif choice =="price":
            Update_by_price()
            flag = False
        else:
            "error in typing"
        if input("Do you want to continue(y/n)?") == "n" :flag = False 
        else : pass        
        
Create_database()
Create_table()
print("        _                            _                 \n       | |                          | |                \n  _ __ | |__   ___  _ __   ___   ___| |_ ___  _ __ ___ \n | '_ \| '_ \ / _ \| '_ \ / _ \ / __| __/ _ \| '__/ _ \ \n | |_) | | | | (_) | | | |  __/ \__ \ || (_) | | |  __/\n | .__/|_| |_|\___/|_| |_|\___| |___/\__\___/|_|  \___|\n | |                                                   \n |_|                                                   ")
print("                 choose to contiue:\n                   1-admin 2-user")
flag = True
choice = input("                      (1/2)?")
while flag:
    if choice == "1" :
        if input("                 Type password:") == "1234":
            flag = True
            print("Welcome admin")
            while flag:
                admin_work = input("What you want to do (add,delete,edit,factors)?")
                if admin_work == "add":
                    Insert_to_table()
                elif admin_work == "delete":
                    Delete()
                elif admin_work == "edit":
                    Edit()
                elif admin_work == "factors":
                    Factors()
                else:
                    pass
            if input("Do you want to continue(y/n)?") == "n" :flag = False 
            else : pass        
    elif choice == "2":
        username = input("Type you username:")
        Create_table_by_user_name(username)
        Select_All_by_username(username)
        Buy(username)
        print("thanks for shopping :)\n bye bye! ")
        flag = False
        
        



























