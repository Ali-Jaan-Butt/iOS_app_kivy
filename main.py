from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
import json


class StartScreen(Screen):
    pass


class HomeScreen(Screen):
    image_width = NumericProperty(50)
    image_height = NumericProperty(50)
    pass


class SignScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class DoctorsList(Screen):
    pass


GUI = Builder.load_file('main.kv')


class MainApp(App):
    cred = credentials.Certificate("doctors-72cd1-firebase-adminsdk-pf7qv-7ca42b4bcf.json")
    firebase_admin.initialize_app(cred, {'databaseURL':'https://doctors-72cd1-default-rtdb.firebaseio.com'})
    ref = db.reference('/')
    screen_manager = ScreenManager()
    def build(self):
        return GUI
    
    def create_patch(self, namee, email, passw):
        data = {'name':namee, 'email':email, 'password':passw}
        new_data_ref = self.ref.push(data)
    
    def get_sign(self, email, password):
        data = self.ref.get()
        self.error_label = Label(text='', color=(1, 0, 0, 1))
        self.error_label.text = "Invalid username or password"
        popup = Popup(title='Login Error', content=self.error_label, size_hint=(None, None), size=(400, 200))
        x = 1
        for i in data:
            if data[i]['email']==email and data[i]['password']==password:
                app = App.get_running_app()
                app.change_screen('home_screen')
                x+=1
                break
            else:
                popup = popup
        if x==1:
            popup.open()
        else:
            pass
    
    def change_screen(self, screen):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen


MainApp().run()
