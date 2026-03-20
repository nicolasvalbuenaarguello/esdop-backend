from werkzeug.security import check_password_hash, generate_password_hash

class User:
    def __init__(self, id=0, user_name="", password="", nombre=None, disabled=False):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.nombre = nombre
        self.disabled = disabled

    @staticmethod
    def check_password(hashed_password: str, plain_password: str) -> bool:
        try:
            return check_password_hash(hashed_password, plain_password)
        except Exception as e:
            print(f"Error al verificar contraseña: {e}")
            return False

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            user_name=data.get("user_name", ""),
            password=data.get("password", ""),
            nombre=data.get("nombre", None),
            disabled=data.get("disabled", False),
        )

    def __repr__(self):
        return f"User(id={self.id}, user_name='{self.user_name}', disabled={self.disabled})"
