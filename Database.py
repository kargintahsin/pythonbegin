import sqlite3
import time
import datetime
import random

con = sqlite3.connect("lessons.db")
cursor = con.cursor()


def createTable():
    cursor.execute('CREATE TABLE IF NOT EXISTS Membership(MemberName TEXT, MemberSurname TEXT,PhoneNumber INT, AccountNumber INT,MemberDate REAL)')


def addMember():
    atime = time.time()
    name = input("Enter Name")
    surname = input("Enter Surname")
    phoneNumber = input("Enter Number")
    accountNumber = random.randrange(0, 100)
    memberDate = str(datetime.datetime.fromtimestamp(atime).strftime('%Y-%m-%d %H:%M:%S'))

    try:
        phoneNumber = int(phoneNumber)
    except ValueError:
        print("Error: Number must be an integer.")
        return
    cursor.execute("INSERT INTO Membership(MemberName,MemberSurname,phoneNumber,AccountNumber,MemberDate) VALUES (?, ?, ?, ?, ?)", (name, surname, phoneNumber, accountNumber, memberDate))


def start():  # Start everything
    print("Press 1 to add a new member \nPress 2 to see data \nPress 0 to close")
    choice1 = int(input())
    return choice1


def question(choice):
    if choice == 1:  # Create a table if table is not exist, and add member!
        createTable()
        addMember()
        con.commit()
        question(start())
    elif choice == 2:  # Take data from table
        takeIt()
        question(start())
    elif choice == 0:  # Close the database
        return 0
    else:  # For undefined numbers
        print("Just 1 or 0!")
        question(start())


def takeIt():
    cursor.execute("SELECT * FROM Membership")  # Use WHERE for take data what you want
    data = cursor.fetchall()
    for i in data:
        print(i)


choice0 = start()

question(choice0)
