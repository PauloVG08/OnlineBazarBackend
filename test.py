import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Cargar las credenciales desde el archivo .env
MYSQL_ADDON_HOST = os.getenv("MYSQL_ADDON_HOST")
MYSQL_ADDON_USER = os.getenv("MYSQL_ADDON_USER")
MYSQL_ADDON_PASSWORD = os.getenv("MYSQL_ADDON_PASSWORD")
MYSQL_ADDON_DB = os.getenv("MYSQL_ADDON_DB")
MYSQL_ADDON_PORT = int(os.getenv("MYSQL_ADDON_PORT"))

try:
    connection = pymysql.connect(
        host=MYSQL_ADDON_HOST,
        user=MYSQL_ADDON_USER,
        password=MYSQL_ADDON_PASSWORD,
        database=MYSQL_ADDON_DB,
        port=MYSQL_ADDON_PORT
    )
    print("Conexión exitosa a la base de datos")
    connection.close()
except pymysql.MySQLError as e:
    print("Error en la conexión:", e)
