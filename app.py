from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from widgets import MyFullLayout


class MyApp(App):
    layout = MyFullLayout()
    
    def build(self):
        
        self.layout = MyFullLayout()
        manager = ScreenManager()
        main_screen = Screen(name="main")
        main_screen.add_widget(self.layout)
        manager.add_widget(main_screen)
        
        
        return manager