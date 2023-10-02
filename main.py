from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file("QuizPage.kv")
class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class Question1Screen(Screen):
    def answer(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "wrong"

class Question2Screen(Screen):
    pass

class CorrectScreen(Screen):
    def next(self):

class WrongScreen(Screen):
    pass

QuizPageApp().run()