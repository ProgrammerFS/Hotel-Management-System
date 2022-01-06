import mysql.connector as mysql
import datetime
#
def sign_up(name, email, password):
    db = mysql.connect(host="localhost", user="root", passwd="Fahad@786", database="hotelmngmnt")
    mycursor = db.cursor()
    t = datetime.datetime.now()
    mycursor.execute(f"INSERT INTO USERS (name, email, password,last_logged_in) Values (\'{name}\',\'{email}\',\'{password}\', \'{t}\')")
    db.commit()

def log_in(email):
    db = mysql.connect(host="localhost", user="root", passwd="Fahad@786", database="hotelmngmnt")
    mycursor = db.cursor()
    mycursor.execute(f"SELECT PASSWORD FROM USERS WHERE EMAIL = \'{email}\'")
    p = ""
    for x in mycursor:
        p = x[0]
    password = p
    return password
