import tkinter as tk
import mysql.connector

from datetime import datetime
now = datetime.now()

#text_box.insert("1.0", "Hello")

def handle_click_showall(event):
    print("showall")
    show_all(mycursor)

def handle_click_submit():
    print("Submit")
    insert_student(mycursor)

def show_all(mycursor):

    mycursor.execute("SELECT * FROM Patient")
    myresult = mycursor.fetchall()

    count = 0
    for x in myresult:
        count += 1
        #print(x)
        y = str(x)
        ind = str(count)
        ind = "0." + ind
        text_box.insert(ind, y + "\n")

def insert_student(mycursor):

    name = entry.get()
    myname = name

    sql = "INSERT INTO PATIENT(first_name, last_name, date_added, doc_id) VALUES (%s, %s, %s, %s)"
    val = (myname, "Lastnameson", now, "1" )

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")



#connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="HospitalPython"
)

#define cursor
mycursor = mydb.cursor()

window = tk.Tk()

#b1
button = tk.Button(
    text="Show All Students(button)",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

button.bind("<Button-1>", handle_click_showall)
#end b1
#Tbox
text_box = tk.Text(height = 26, width = 200)
text_box.pack()
#endofTBOX


entry = tk.Entry()
entry.pack()



button2 = tk.Button(text="Submit", command=handle_click_submit)


button2.pack()




window.mainloop()

#label1 = tk.Label(text="Insert a student")

#label2 = tk.Label(text="Show All Students")



print("window closed")
