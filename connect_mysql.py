import mysql.connector
from mysql.connector import Error

def read_data():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  
            password='rootpassword', # put password here 
            database='mydatabase' # put database name here
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM student") # put your sql query here
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    read_data()
