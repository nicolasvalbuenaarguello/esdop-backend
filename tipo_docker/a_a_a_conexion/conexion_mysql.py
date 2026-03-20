from __init__ import *

class Databa_bases:
    def __init__(self):
        self.connection = pymysql.connect(

        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        db =  MYSQL_DB)

    def conexion_comi(self, sql):
        self.cursor  = self.connection.cursor()
        self.cursor.execute(sql)
        self.connection.commit()
        self.cursor.close()
        # self.connection.close()

    def conexion(self, query):
        cursor  = self.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        self.cursor.close()
        return row
    
    def close(self):
        # self.cursor.close()
        self.connection.close()