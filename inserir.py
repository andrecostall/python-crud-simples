import mysql.connector
from mysql.connector import Error
from conecta import config_connector

try:
    con = mysql.connector.connect(**config_connector)

    if con.is_connected:
        sql = "insert into aluno (nome,sobrenome) values (%s,%s)"
        #valores=("Fulano", "Beltrano")
        valores = [
                ("Fulano", "Silva"),
                ("Ciclano", "Lima"),
                ("Beltrano", "Costa")
        ]

        cursor = con.cursor()
        #cursor.execute(sql,valores)
        cursor.executemany(sql,valores)
        con.commit()
        print("\nregistro(s) inserido(s): ", cursor.rowcount)

except Error as e:
    print("Erro ao acessar a tabela aluno", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("\nConexão encerrada com o MySQL")