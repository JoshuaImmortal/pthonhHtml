import mysql.connector
from mysql.connector import Error

try:
    db_con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
    )
    cursor = db_con.cursor()
    if(db_con.is_connected):
        cursor.execute("CREATE DATABASE IF NOT EXISTS `Note_db`")
        print('connected successfully')
except Error as e:
    print(e)