from ..controller.login_controller import LoginController
from sigin_view import SiginView

class LoginView(LoginController):
    def __init__(self):
        super().__init__()

    def login_system(self):
        sigin = SiginView()
        print("======Login View======\n")
        try:
            while True:
                ask = input("I don't have an account! Go SigIn? (Y/N): ")[0].lower()
                if ask == "y":
                    sigin.sigin()
                elif ask == "n":
                    bi = input("Unique ID: ")
                    password = input("Password: ")
                    customer = self.login(bi, password)
                    if customer:
                        pass
                else:
                    print("Just answer with Y/N!")
        except(ValueError):
            print(f"Erro: {ValueError}")
