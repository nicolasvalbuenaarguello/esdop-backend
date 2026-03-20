# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codecs import unicode_escape_decode
import psycopg2
import sys

class Databa_bases:

    def comando_query(self, seleccion):
        try:
            with psycopg2.connect(
                host='localhost',
                user='postgres',
                password='NICval10**',
                dbname='dirop'
            ) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(seleccion)
                    datos = cursor.fetchall()
            return datos
        except Exception as e:
            print(f"❌ Error en comando_query: {e}")
            return []
    def comando_ingreso(self, selecion):
        sql = selecion
        self.cursor.execute(sql)
        self.cursor.close()

    def close_conecion(self):
        self.cursor.close()
        self.connection.close()