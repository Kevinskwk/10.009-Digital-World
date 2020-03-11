import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass


class L10App(App):
    def build(self):
        return Widgets()

def show_popup():
    show = P()
    popupWindow = Popup(title = 'Popup Window', content=show, size_hint=(None,None), size=(400,400))
    popupWindow.open()
    
    
L10App().run()