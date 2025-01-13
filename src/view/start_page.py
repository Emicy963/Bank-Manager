from ..controller.login_controller import LoginController

class LoginView:
    def __init__(self, customer:LoginController):
        self._customer = customer

    def sing(self):
        try:
            name = input("Name: ")

            while True:
                password = input("Password:")
                password2 = input("Writing password again: ")
                if password == password2:
                    break
            
            bi = input("")
