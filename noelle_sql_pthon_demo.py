#https://www.w3schools.com/sql/sql_insert.asp
#https://www.w3schools.com/python/python_mysql_select.asp
import mysql.connector

#connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="discord"
)

#insert
mycursor = mydb.cursor()

sql = "INSERT INTO firstnames(name) VALUES (%s)"
val = ("Taj", )

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

##selects

mycursor.execute("SELECT * FROM firstnames")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

