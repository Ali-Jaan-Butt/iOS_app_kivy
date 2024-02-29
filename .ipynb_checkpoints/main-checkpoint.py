from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout


class StartScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class SignScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


GUI = Builder.load_file('main.kv')


class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen


MainApp().run()
