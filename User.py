class User():
    def __init__(self, Name, Password, Email):
        self.Name = Name
        self.Password = Password
        self.Email = Email

    def __repr__(self):
        ReturnString = "<Name: {}, Email: {}>".format(self.Name, self.Email)
        return  ReturnString

    def LogIn(self, Name, Password):
        pass
