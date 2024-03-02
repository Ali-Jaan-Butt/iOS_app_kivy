from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from mydb import Mydb
import requests
import json


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
        self.my_db = Mydb()
        return GUI
    
    def on_start(self):
        res = requests.get('https://med-care-35b0f-default-rtdb.firebaseio.com/1.json')
        print('Is it ok???', res.ok)
        data = json.loads(res.content.decode())
        print(data)

    def change_screen(self, screen):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen


MainApp().run()
