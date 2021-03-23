import mysql.connector

from datetime import datetime
now = datetime.now()

#connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="HospitalPython"
)

'''
CREATE TABLE PATIENT (
    pat_id integer AUTO_INCREMENT PRIMARY KEY, 
    first_name varchar(20) NOT NULL,
    last_name varchar(20) NOT NULL,
    phone varchar(15) ,
    email varchar(50),
    st_address varchar(100), 
    city_state varchar(50) , 
    date_added timestamp NOT NULL,
    doc_id integer NOT NULL,
    FOREIGN KEY (doc_id) REFERENCES DOCTOR(doc_id)
    );
'''

mycursor = mydb.cursor()

def take_input():
    print("Enter your selection here")
    menuSelection = input()
    menuSelection = menuSelection.upper()
    menuSelection = menuSelection[0]
    return menuSelection

def take_string(whatis):
    print("Please give me a " + str(whatis))
    mystring = input()

    return mystring

def show_menu():
    print("[A] Show all students")
    print("[B] Insert a student")

def show_all(mycursor):

    mycursor.execute("SELECT * FROM Patient")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def insert_student(mycursor):

    
    myname = take_string("name")

    sql = "INSERT INTO PATIENT(first_name, last_name, date_added, doc_id) VALUES (%s, %s, %s, %s)"
    val = (myname, "Lastnameson", now, "1" )

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


menu_select = ' '

while(menu_select != 'Q'):
    show_menu()
    menu_select = take_input()

    if(menu_select == 'A'):
        show_all(mycursor)
    elif(menu_select == 'Q'):
        print("Goodbye")
    elif(menu_select == 'B'):
        insert_student(mycursor)
    else:
        print("How did you get here? Error 1")
