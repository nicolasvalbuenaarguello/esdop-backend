from werkzeug.security import check_password_hash, generate_password_hash

from pydantic import BaseModel


class User():
    def __init__(self, **kwargs) -> None:
        self.id = 0
        self.user_name  = ""
        self.password  = ""
        self.disabled  = ""

        for c in kwargs.items():
            if c[0]=="user_name":
                self.user_name = c[1]
            elif c[0]=="password":
                self.password = c[1]
            elif c[0]=="disabled":
                self.disabled = c[1]
            elif c[0]=="id":
                self.id = c[1]




    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)
    
    
# print(generate_password_hash("JEMOP"))
# 