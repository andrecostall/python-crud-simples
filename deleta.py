import mysql.connector
from mysql.connector import Error
from conecta import config_connector

try:
    con = mysql.connector.connect(**config_connector)

    if con.is_connected:
        sql = "delete from aluno where id = %s"
                        
        valores=(7,)
        cursor = con.cursor()
        cursor.execute(sql,valores)
        con.commit()
        
        print("\nregistro(s) deletado(s): ", cursor.rowcount)

except Error as e:
    print("Erro ao acessar a tabela aluno", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("\nConexão encerrada com o MySQL")