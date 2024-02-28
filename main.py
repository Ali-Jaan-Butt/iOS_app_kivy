from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class StartScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


GUI = Builder.load_file('main.kv')


class MainApp(App):
    def build(self):
        return GUI
    
    def change_screen(self, screen):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen


MainApp().run()
