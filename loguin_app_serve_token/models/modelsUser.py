from .entities.user import User
from mysql.connector import Error

class ModelUser:

    @classmethod
    def loguin(self, db, user):
        print(user.user_name)
        cursor = None
        try:
            cursor = db.connection.cursor()
            sql = """
                SELECT id, nombre, usuario, contrasenia 
                FROM usuarios_dirop 
                WHERE usuario = %s 
                LIMIT 1
            """
            cursor.execute(sql, (user.user_name,))
            row = cursor.fetchone()

            if row:
                user = User(
                    id=row[0],
                    user_name=row[2],
                    disabled=User.check_password(row[3], user.password),
                    password=row[3]
                )
                return user
            else:
                return None

        except Error as ex:
            raise Exception(f"Error en login: {ex}")
        finally:
            if cursor:
                cursor.close()
            db.connection.close()

    @classmethod
    def get_by_id(self, db, id):
        cursor = None
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM usuarios_dirop WHERE id = %s LIMIT 1"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()

            if row:
                return User(*row)  # solo si User admite todos los campos en orden
            else:
                return None

        except Error as ex:
            raise Exception(f"Error al obtener usuario por ID: {ex}")
        finally:
            if cursor:
                cursor.close()
            db.connection.close()
