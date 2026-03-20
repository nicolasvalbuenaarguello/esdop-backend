# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codecs import unicode_escape_decode
import psycopg2
import sys

class Databa_bases:
    def comando_query(self, selecion):
        self.connection = psycopg2.connect(
            host = 'localhost', 
            user = 'postgres' ,
            password = 'NICval10**' ,
            database = 'dirop' 
       )
        self.cursor = self.connection.cursor()
        sql = selecion
        self.cursor.execute(sql)
        dato = self.cursor.fetchall()

        self.cursor.close()
        self.connection.close()

        return dato
    def comando_ingreso(self, selecion):
        sql = selecion
        self.cursor.execute(sql)
        self.cursor.close()

    def close_conecion(self):
        self.cursor.close()
        self.connection.close()