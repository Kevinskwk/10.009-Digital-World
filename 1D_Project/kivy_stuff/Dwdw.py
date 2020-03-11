import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#get = GetList
#lst = get.floor1()

#def callback(instance):
  #  string = str(instance)

 #   lst = get.string

    #print('The button <%s> is being pressed' % instance.text)

#floor1 = Button(text='Floor 1')
#floor1.bind(on_press=callback)
#floor2 = Button(text='Floor 2')
#floor2.bind(on_press=callback)


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

