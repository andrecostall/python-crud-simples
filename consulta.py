import mysql.connector
from mysql.connector import Error
from conecta import config_connector

try:
    con = mysql.connector.connect(**config_connector)

    if con.is_connected:
        consulta = "select * from aluno"
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        print("\nNÚmero de alunos matriculados: ", cursor.rowcount)

        print("\n=== Lista de alunos matriculados ===")
        for registro in linhas:
            print("Id:", registro[0])
            print("Nome:", registro[1])
            print("Sobrenome:", registro[2])

except Error as e:
    print("Erro ao acessar a tabela aluno", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("\nConexão encerrada com o MySQL")