#https://www.w3schools.com/sql/sql_insert.asp
#https://www.w3schools.com/python/python_mysql_select.asp
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

#insert
mycursor = mydb.cursor()

sql = "INSERT INTO PATIENT(first_name, last_name, date_added, doc_id) VALUES (%s, %s, %s, %)"
val = ("Taj", )

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

##selects

mycursor.execute("SELECT * FROM firstnames")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

