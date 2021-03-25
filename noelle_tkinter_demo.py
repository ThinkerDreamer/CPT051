import tkinter as tk
import mysql.connector

from datetime import datetime
now = datetime.now()

#text_box.insert("1.0", "Hello")

def handle_click_showall(event):
    show_all(mycursor)

def show_all(mycursor):

    mycursor.execute("SELECT * FROM Patient")
    myresult = mycursor.fetchall()

    count = 0
    for x in myresult:
        count += 1
        #print(x)
        ind = str(count)
        ind = "0." + ind
        text_box.insert(ind, x)

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


button = tk.Button(
    text="Show All Students(button)",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

button.bind("<Button-1>", handle_click_showall)

text_box = tk.Text(height = 26, width = 200)
text_box.pack()



entry = tk.Entry()
entry.pack()

name = entry.get()

button2 = tk.Button(
    text="Submit",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button2.pack()

window.mainloop()

#label1 = tk.Label(text="Insert a student")

#label2 = tk.Label(text="Show All Students")



print("window closed")
