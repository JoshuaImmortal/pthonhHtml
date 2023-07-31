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
    if (cursor):
        cursor.execute("""
                        INSERT INTO `note_s` VALUES ('', 'Diary of a wimpy kid', 'The_immortal', 'Story of a kid as he goes through the lows and highs of middle school, navigates friendships, makes new enemies and overall writes into his diary on how his day went, this is the diary of a wimpy kid.', '29-07-2023', now())
                    """)
        db_con.commit()
        print('Entry Successful')
    else:
        print('Error, could not upload entry.')
except Error as error:
    print(error)