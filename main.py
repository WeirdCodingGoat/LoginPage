from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("LoginPage.kv")


class QuizPageApp(App):
    def build(self):
        return QuizManager()


class QuizManager(ScreenManager):
    pass


QuizPageApp().run()
