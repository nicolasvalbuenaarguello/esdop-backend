# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codecs import unicode_escape_decode
import psycopg2
import sys

class Databa_bases_posgrest:
    def __init__(self):
        self.connection = psycopg2.connect(
            host = 'localhost', 
            user = 'postgres' ,
            password = 'NICval10**' ,
            database = 'dirop' 

       )
        self.cursor = self.connection.cursor()


    def comando_query(self, selecion):

        sql = selecion
        self.cursor.execute(sql)
        dato = self.cursor.fetchall()
        # self.cursor.close()
    
        return dato
    def comando_ingreso(self, selecion):
        sql = selecion
        self.cursor.execute(sql)
        self.cursor.close()