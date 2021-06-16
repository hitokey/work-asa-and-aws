
class User:
    user = None
    email = None
    senha = None
    def __init__(self,user,email,senha):
        self.user = user
        self.email = email
        self.senha = senha

    def get_user(self):
        return self.user

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha

    def set_user(self,user):
        self.user = user

    def set_email(self,email):
        self.email = email

    def set_senha(self,senha):
        self.senha = senha

    

    
