import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen




class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass
    
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('Dwdw.kv')

class DwdwApp(App):
    def build(self):
        return kv

DwdwApp().run()

