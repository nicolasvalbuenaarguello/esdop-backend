from __init__ import *
import pymysql
import os
import shutil
from dotenv import load_dotenv

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')

class Databa_bases_2:
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
    
    def conexion_l(self, query):
        
        cursor  = self.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        print(row)
        self.cursor.close()
        return row
    
    def close(self):
        #self.cursor.close()
        self.connection.close()

    def conexion_directa():
        connection = pymysql.connect(

        host = 'localhost',
        user = 'root',
        password = 'NICval10**',
        db =  'dirop')

        cursor  = connection.cursor()
        # connection.close()
        return cursor

    

     