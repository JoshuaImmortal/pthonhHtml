import mysql.connector
from mysql.connector import Error
try:
    db_con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'Note_db'
    )
    cursor = db_con.cursor()
    if(db_con.is_connected):
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS `Note_S`(
                       `Serial_No` INT PRIMARY KEY AUTO_INCREMENT,
                       `Title` VARCHAR(50) NOT NULL,
                       `Author` VARCHAR(50) NOT NULL,
                       `Content` LONGTEXT NOT NULL,
                       `DATE_WRITTEN` VARCHAR(15),
                       `DATE_PUBLISHED` TIMESTAMP DEFAULT CURRENT_TIME
                        );
                       """)
except Error as e:
    print(e)