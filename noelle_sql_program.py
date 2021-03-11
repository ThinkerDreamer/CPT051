import mysql.connector

#connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="discord"
)


def take_input():
    print("Enter your selection here")
    menuSelection = input()
    menuSelection = menuSelection.upper()
    menuSelection = menuSelection[0]
    return menuSelection

def show_menu():
    print("[A] Show all students")
    print("[B] Insert a student")

def show_all():

    mycursor.execute("SELECT * FROM firstnames")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def insert_student():
    mycursor = mydb.cursor()

    sql = "INSERT INTO firstnames(name) VALUES (%s)"
    val = ("Taj", )

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


menu_select = ' '

while(menu_select != 'Q'):
    show_menu()
    menu_select = take_input()

    if(menu_select == 'A'):
        show_all()
    elif(menu_select == 'Q'):
        print("Goodbye")
    elif(menu_select == 'B'):
        insert_student()
    else:
        print("How did you get here? Error 1")
