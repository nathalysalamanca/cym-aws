import pymysql

db_host = 'db-nat1.c1ce2a2i2rvr.us-east-1.rds.amazonaws.com'
db_user = 'admin'
db_pass = '12345678'
db_name = 'db_users'

def connectionSQL():
    try:
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
        print("Conexión exitosa")
        return conn
    except Exception as err:
        print("Error conectando a la Base de Datos:", err)
        return None
           

def insert_user(id, name, lastname, birthday):
    conn = connectionSQL()
    with conn.cursor() as cursor:
        sql = "INSERT INTO users (id, name, lastname, birthday) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id, name, lastname, birthday))
    conn.commit()
    print("Usuario insertado correctamente.")
      

def consult_user(id):
    conn = connectionSQL()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                return "No se encontró ningún usuario con el ID proporcionado."
    except Exception as err:
        return f"Error al consultar usuario por ID: {err}"
    finally:
        if conn:
            conn.close()