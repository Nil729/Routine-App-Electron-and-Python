import sqlite3
from sqlite3 import Error
import sys



direccion = sys.argv[1]
segundos = sys.argv[2]
nomTaula = sys.argv[3]
minutos = sys.argv[4]
horsa = sys.argv[5]

def sql_connection():
    
    try:
        con = sqlite3.connect('mydatabase.db')
        print ("Conectat")
        return con

    except Error:

        print(Error)
con = sql_connection()

cursorObj = con.cursor()



def sql_insert(con, entities, direccion, horsa, minutos, segundos, nomTaula):

    cursorObj.execute(f'INSERT INTO {nomTaula} (App, direccion, horas, minutos, segundos) VALUES(?, ?, ?, ?, ?)', entities)
        
    con.commit()
    print ("Se ha selecionado e insertado en ",nomTaula )
    
entities = ( 'Youtube', direccion, horsa, minutos, segundos )

sql_insert(con, entities, direccion, horsa, minutos, segundos, nomTaula)