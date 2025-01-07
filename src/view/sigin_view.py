from ..controller.login_controller import LoginController
from login_view import LoginView

class SiginView:
    def __init__(self, new_customer:LoginController) -> None:
        self._new_customer = new_customer

    def sigin(self):
        print("=========Sing In=========\n")
        login_view = LoginView()
        while True:
            ask = input("Already an account! Login? (Y/N): ")[0].lower()
            if ask == "y":
                login_view.login_system()
                break
            elif ask == "n":
                name = input("\nName: ")
                password = input("Create a Password: ")
                bi = input("Create a Unique ID: ")
                age = int(input("Age: "))
                living = input("Endress: ")
                job = input("Job: ")  

                new_customer = self._new_customer.singIn(name, password, bi, 0, living,
                                        age, job, False)
                
                if new_customer:
                    login_view.login_system()
            else:
                print("Just answer with Y/N!")
