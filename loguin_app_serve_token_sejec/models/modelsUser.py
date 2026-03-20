from models.conexion_mysql import Databa_bases_posgrest
from .entities.user import User

class ModelUser():
    
    @classmethod
    def loguin(self,  user):
        try:
           
            sql = """SELECT id, full_nombre, usuario, contrasenia FROM usuarios_sejec 
            WHERE usuario like '{}'""".format(user.user_name)
            row = Databa_bases_posgrest.comando_query(self, sql)

            for x in row:
                row = x
            
            if row != []:
                user = User(id =row[0], user_name =row[2], disabled = User.check_password(row[3], user.password), password = row[3])

                Databa_bases_posgrest.close(self)
                
                return user
            else:
                None 
        except Exception as ex:
            raise Exception(ex)
        
    def loguin_dos(user):

        try:
            
            sql = """SELECT id, nombre, usuario, contrasenia FROM usuarios_sejec 
            WHERE usuario like '{}'""".format(user.user_name)
            row = Databa_bases_posgrest.comando_query(sql)
            Databa_bases_posgrest.close()

            # return row

            for x in row:
                row = x
            
            if row != []:
                user = User(row[0], row[1], User.check_password(row[3], user.password), row[3])
                return user
            else:
                None 
        except Exception as ex:
            raise Exception(ex)
            
    @classmethod
    def get_by_id(self, id):
        try:
            
            sql = "SELECT * FROM usuarios_sejec WHERE id = {}".format(id)
            row = Databa_bases_posgrest.comando_query(self, sql)
            Databa_bases_posgrest.close()

            for x in row:
                row = x
            
            if row != []:
                return User(row[0],	row[1],	row[2],	row[3],	row[4],	row[5],	row[6],	row[7])#se coloca los elementos de la base de datos 
            else:
                return None
        except Exception as ex:
            raise Exception(ex)