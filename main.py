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
    def get_logged_in(self,password,username):
            with open(r"accInfo.txt","r") as accInfo:
                accounts=accInfo.read()
                pass_start=accounts.find(username)+len(username)+1
                pass_end=pass_start+len(password)
                if username in accounts:
                    if password == accounts[pass_start:pass_end]:
                        accInfo.close()
                        self.manager.current = "home"
                    else:
                        accInfo.close()
                      # self.manager.current = "wrong"

    def switch_screen(self): #Screen change function(s)?
        self.manager.current = "newaccount"


class NewAccountPage(Screen):
    def answer_question(self, password, password2, username):
        
        req_met=0
        if password == password2:
            req_code=req_handling(password_requirements(password,upper_letters))
            if req_code == -1:
                self.manager.current = "err2"
            else:
                for digit in req_code:
                    if digit == "1":
                        req_met += 1
                if req_met == len(req_code):
                    with open(r"accInfo.txt","a") as accInfo:
                        accInfo.write(" "+username+" "+password)
                        accInfo.close()
                    self.manager.current = "success"
                else:
                    self.manager.current = "err3"
                    print(req_code,req_met,len(req_code))
        else:
            self.manager.current = "err1"
    
    def switch_screen(self):
        self.manager.current = "login"

class HomePage(Screen):
    def switch_screen(self):
        self.manager.current = "login"


class WrongScreen(Screen):
    def next(self):
        self.manager.current = "newaccount"
class SpaceErr(Screen):
    def next(self):
        self.manager.current = "newaccount"
class UnmetRequirement(Screen):
    def next(self):
        self.manager.current = "newaccount"
class AccSuccess(Screen):
    def next(self):
        self.manager.current = "login"
LoginPageApp().run()

