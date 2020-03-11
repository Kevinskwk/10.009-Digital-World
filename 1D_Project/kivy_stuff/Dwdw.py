import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

#get = GetList
#lst = get.floor1()

<<<<<<< HEAD
class Widgets(Widget):
    def btn(self):
        show_popup()
=======
#def callback(instance):
  #  string = str(instance)

 #   lst = get.string

    #print('The button <%s> is being pressed' % instance.text)

#floor1 = Button(text='Floor 1')
#floor1.bind(on_press=callback)
#floor2 = Button(text='Floor 2')
#floor2.bind(on_press=callback)
>>>>>>> d5f0cdbe6b3d693556653947d8e437247c53bf8a

class P(FloatLayout):
    pass

class MainWindow(Screen):
    pass

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

