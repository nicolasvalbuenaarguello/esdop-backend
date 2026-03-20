import mysql.connector
def conecion():
    mydb = mysql.connector.connect(

        host = 'localhost',
        user = 'root',
        password = 'NICval10**',
        db =  'PLAZOS_SEGUNDO_CDTE'
    )
    return mydb

def seleciones(query):
    mydb = conecion()
    my_cursor = mydb.cursor()
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    return result
    
def close():

    mydb = conecion()
    my_cursor = mydb.cursor()
    my_cursor.close()
    mydb.close