import pymysql
def conexion_comi(sql):
    connection = pymysql.connect(

        host = 'localhost',
        user = 'root',
        password = 'NICval10**',
        db =  'dirop'

    )

    cursor  = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def conexion():
    connection = pymysql.connect(

        host = 'localhost',
        user = 'root',
        password = 'NICval10**',
        db =  'dirop'

    )

    cursor  = connection.cursor()
    connection.close()
    return cursor



