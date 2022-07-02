import  mysql.connector
def Conn():
    db=mysql.connector.connect(host="localhost",database="beta",user="Admin", password="1234" )
    print(db, "connected")
    return db

Conn()
