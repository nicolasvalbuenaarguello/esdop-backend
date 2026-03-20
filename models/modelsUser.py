from .entities.user import User

class ModelUser():
    
    @classmethod
    def loguin(self, db,  user):
        # print(user.user_name)
        try:

            cursor=db.connection.cursor()
            
            sql = """SELECT id, nombre, usuario, contrasenia FROM usuarios_dirop 
            WHERE usuario like '{}'""".format(user.user_name)
            cursor.execute(sql)
            row = cursor.fetchone()
            #cursor.close()
            #db.connection.close()
            
            if row != None:
                user = User(id =row[0], user_name =row[2], disabled = User.check_password(row[3], user.password), password = row[3])
                return user
            else:
                None 
        except Exception as ex:
            raise Exception(ex)
        
    def loguin_dos(db, user):

        try:
            cursor=db.connection.cursor()
            sql = """SELECT id, nombre, usuario, contrasenia FROM usuarios_dirop 
            WHERE usuario like '{}'""".format(user.user_name)
            cursor.execute(sql)
            row = cursor.fetchone()

            # return row
            if row != None:
                user = User(row[0], row[1], User.check_password(row[3], user.password), row[3])
                return user
            else:
                None 
        except Exception as ex:
            raise Exception(ex)
            
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()

            sql = "SELECT * FROM usuarios_dirop WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                print()
                return User(row[0],	row[1],	row[2],	row[3],	row[4],	row[5],	row[6],	row[7],	row[8],	row[9],	row[10],	row[11],	row[12],	row[13],	row[14],	row[15],	row[16],	row[17],	row[18],	row[19],	row[20],	row[21],	row[22],	row[23],	row[24],	row[25],	row[26],	row[27],	row[28],	row[29],	row[30],	row[31],	row[32],	row[33],	row[34],	row[35],	row[36],	row[37],	row[38],	row[39],	row[40],	row[41],	row[42],	row[43],	row[44],	row[45],	row[46],	row[47],	row[48],	row[49],	row[50],	row[51],	row[52],	row[53],	row[54]
                
)#se coloca los elementos de la base de datos 
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
        