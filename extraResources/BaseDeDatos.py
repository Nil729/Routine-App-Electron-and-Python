import sqlite3
from sqlite3 import Error
import sys

#---------------------------------------------------Conexion sql------------------------------------------------------.

def sql_connection():

    try:
        con = sqlite3.connect('mydatabase.db')
        print ("Conectat")
        return con

    except Error:

        print(Error)
con = sql_connection()


#-------------------------------------------------Crea una tabala sql i afeguir el nom corresponent--------------------------------------------------.
nomTaula = sys.argv[1]

print (nomTaula)

cursorObj = con.cursor()

def sql_table(con,nomTaula,cursorObj): 
    #print ("La taula a sigut creada")

    #Posa el nom de la taula.

    nomR = '''SELECT name
            FROM sqlite_master
            WHERE TYPE='table'
              AND name=?'''
    cursorObj.execute(nomR, (nomTaula, ))

    nomR = f'''CREATE TABLE IF NOT EXISTS {nomTaula}
                ( App text, direccion text, horas integer, minutos integer, segundos integer)'''
    cursorObj.execute(nomR)

    #cursorObj.execute("CREATE TABLE IF NOT EXISTS nomTaula ( name text, direccion text, horas integer, minutos integer, segundos integer)")
    con.commit()
sql_table(con, nomTaula,cursorObj)

