import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
'''class Color_btn(Widget):
    def __init__(self, in_color):
        self.btn.color = in_color'''


class P(FloatLayout):
    pass

class MainWindow(Screen):
    '''def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.btn_1.background_color = in_color'''
    def btn(self):
        show_popup()

class SecondWindow(Screen):
    pass
    
class WindowManager(ScreenManager):
    pass


def show_popup():
    show = P()
    popupWindow = Popup(title = 'Popup Window', content=show, size_hint=(None,None), size=(400,400))
    popupWindow.open()




kv = Builder.load_file('Dwdw.kv')
class DwdwApp(App):
    def build(self):
        return kv

DwdwApp().run()

