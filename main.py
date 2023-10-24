from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

upper_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print("why")
Builder.load_file("LoginPage.kv")
class LoginPageApp(App):
    def build(self):
        return PageManager()
print("why")
class PageManager(ScreenManager):
    pass
print("why")
def password_requirements(password,upper_letters):
    cap_check=False
    num_check=False
    low_check=False
    spe_check=False
    len_check=False
    num_list=["0","1","2","3","4","5","6","7","8","9"]
    lower_letters=[]
    check_list=[]
    if len(password) >= 8:
        len_check=True
        if not " " in password:
            for character in password: #Number check
                if character in num_list:
                    num_check=True
            for letter in upper_letters: # Capital letter check
                if letter in password:
                    cap_check=True
                if letter.lower() in password:
                    low_check=True
                lower_letters.append(letter.lower()) #compiling lower_letters
            for letter in password:
                if not letter in lower_letters and not letter in upper_letters and not letter in num_list:
                    spe_check=True
                    
        else:
            len_check=False
            spe_check=True
    check_list=[len_check,num_check,cap_check,low_check,spe_check]
    return check_list
print("why")
    
def req_handling(check_list):
    #len_check=index0, num_check=index1, cap_check=index2, low_check=index3, spe_check=inde4
    code_handle=""
    for boolen_val in check_list:
        if boolen_val == True:
            code_handle+="1"
        else:
            code_handle+="0"
    if code_handle == "00001":
        return -1
    else:
        return code_handle
print("why")
class LoginPage(Screen):
    def get_logged_in(self,username,password):
        code_var = req_handling(password_requirements(password,upper_letters))
        print(code_var)

    def switch_screen(self): #Screen change function(s)?
        self.manager.current = "newaccount"
print("why")

class NewAccountPage(Screen):
   
    def answer_question(self, password, password2, username):
        if password == password2:
            check_list=password_requirements(password,upper_letters)
            print(req_handling(check_list))
        else:
            print("Make sure they are the same.")
    
    def switch_screen(self):
        self.manager.current = "login"
print("why")
class HomePage(Screen):
    def switch_screen(self):
        self.manager.current = "login"

print("why")
class WrongScreen(Screen):
    def next(self):
        self.manager.current = "newaccount"


LoginPageApp().run()

