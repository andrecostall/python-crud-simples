import mysql.connector
from mysql.connector import Error

config_connector = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'db_test',
  'raise_on_warnings': True
}
try:
    con = mysql.connector.connect(**config_connector)
    
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
        cursor = con.cursor()
        cursor.execute("select database()")
        linha = cursor.fetchone()
        print("Conectado ao banco de doados ",linha)
except Error as e:
    print("Error conexão ao MySQL", e)
finally:    
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")
