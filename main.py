from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

upper_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

Builder.load_file("LoginPage.kv")
class LoginPageApp(App):
    def build(self):
        return PageManager()

class PageManager(ScreenManager):
    pass

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
            
class LoginPage(Screen):
    def get_logged_in(self,username,password):
        code_var = req_handling(password_requirements(password,upper_letters))
        print(code_var)

    def switch_screen(self): #Screen change function(s)?
        self.manager.current = "newaccount"


class NewAccountPage(Screen):
    #req1 = Label(text="You don't have at least 8 characters.")
    #req2 = Label(text="You don't have at least 1 number.")
    #req3 = Label(text="You don't have at least 1 uppercase letter.")
    #req4 = Label(text="You don't have at least 1 lowercase letter.")
    #req5 = Label(text='You don't have at least 1 "special" character.')
    #err1 = Label(text="You have a space in your password.")
    #err2 = Label(text="Make sure you didn't make a new line and they are exactly the same.")
    def answer_question(self, password, password2):
        if password == password2:
            check_list=password_requirements(password,upper_letters)
            print(req_handling(check_list))
        else:
            print("Make sure they are the same.")
    
    def place_holder(self): #Screen change function(s)?
        print("You need a function, put 'root.' here")
        

class CorrectScreen(Screen):
    def next(self):
        self.manager.current = "newaccount"

class WrongScreen(Screen):
    def next(self):
        self.manager.current = "newaccount"


LoginPageApp().run()

