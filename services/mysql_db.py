from config import Config
import mysql.connector as mysql


def create_table(cursor):
    sql = """
        CREATE TABLE IF NOT EXISTS weather (
            id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            timestamp DATE NOT NULL,
            name VARCHAR(255) NOT NULL,
            temp FLOAT NOT NULL,
            feels_like FLOAT NOT NULL,
            humidity INT NOT NULL,
            wind_speed FLOAT NOT NULL
        )
    """
    cursor.execute(sql)

def save_to_mysql(weather):
    mysql_config = {
        "user": Config.MYSQL_USER,
        "password": Config.MYSQL_PASS,
        "host": Config.MYSQL_HOST,
        "database": Config.MYSQL_DB
    }
    try:
        conn = mysql.connect(**mysql_config)
        cursor = conn.cursor()
        create_table(cursor)

        insert_sql = """
            INSERT INTO weather (timestamp,name,temp,feels_like,humidity,wind_speed)
            VALUES (%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_sql, tuple(weather.values()))
        conn.commit()
        print("Zapisano dane pogodowe w MySQL")


    except Exception as e:
        print(e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Zamknięto połączenie")

def get_from_mysql(weather):
    mysql_config = {
        "user": Config.MYSQL_USER,
        "password": Config.MYSQL_PASS,
        "host": Config.MYSQL_HOST,
        "database": Config.MYSQL_DB
    }
    try:
        conn = mysql.connect(**mysql_config)
        cursor = conn.cursor()
        select_sql = """
            SELECT * FROM weather
            ORDER BY id DESC
            LIMIT 10
        """
        cursor.execute(select_sql)
        results = cursor.fetchall()

        print("Ostatnie 10 zapisanych danych pogodowych:")
        for row in results:
            print(row)


    except Exception as e:
        print(e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Zamknięto połączenie")