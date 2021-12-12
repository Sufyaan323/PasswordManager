import hashlib
import os
from pysqlcipher3 import dbapi2 as sqlite3

def start():
    os.system("clear")
    print("-"*50)
    print("-"*16,"Password Manager","-"*16)
    print("-"*50)


def pwm():
    print("Input the master password:")

    masterkey = str(input("> "))

    cursor.execute("PRAGMA key = '" + masterkey + "'")

    try:
        cursor.execute('''create table test (test text)''')
    except:
        print("PASSWORD IS INCORRECT")
        cursor.close
        exit()
    connection.execute("drop table test")

def newpwm():
    print("Input the master password you would like to use to access the password manager:")

    masterkey = str(input("> "))

    cursor.execute("PRAGMA key = '" + masterkey + "'")
    cursor.execute('''create table accounts (user text, password text, website text, name text)''')
    connection.commit()

def newAccount():
    print("User: ")
    user = input("> ")

    print("Password:")
    password = input("> ")

    print("Website: ")
    website = input("> ")

    print("Name: ")
    name = input("> ")

    cursor.execute("""insert into accounts (user, password, website, name) VALUES (?, ?, ?, ?)""",(user, password, website, name))

    connection.commit()

def searchAccount():
    print("Search by (1)User or (2)Name")

    try:
        choice = int(input("> "))


        if choice == 1:
            search = input("User: ")
            cursor.execute("select * from accounts where user = ?", (search,))

        else:
            search = input("Name: ")
            cursor.execute("select * from accounts where name = ?", (search,))
    except:
        print("Please enter a number from 1-2")
        input("Press ENTER to try again")
        os.system("clear")
        searchAccount()

    query = cursor.fetchall()

    for row in query:
        print(row)
    input("Press Enter to continue")

def exitPWM():
    cursor.close()
    exit()

def menu():
    os.system("clear")

    print("-"*50)
    print("-"*22,"Menu","-"*22)
    print("-"*50)

    print("1) Add New Account")
    print("2) Search Existing Account")
    print("3) Exit")

    choice = int(input("Option: "))
    if choice == 1:
        newAccount()
    elif choice == 2:
        searchAccount()
    else:
        exitPWM()


start()

directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(directory, "secret.db")

if os.path.exists(db_path) == False:
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor() 
    newpwm()
else:
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor() 
    start()
    pwm()

while True:
    menu()