# -*- coding: utf-8 -*-
import pymysql

class Databa_bases:
    def __init__(self):
        self.connection = pymysql.connect(

        host = 'localhost',
        user = 'root',
        password = 'NICval10**',
        db =  'dirop')

  
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
        # self.cursor.close()
        return row
    
    def conexion_2(self, query):
        cursor  = self.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        # self.cursor.close()
        return row
    
    def close(self):
        # self.cursor.close()
        self.connection.close()