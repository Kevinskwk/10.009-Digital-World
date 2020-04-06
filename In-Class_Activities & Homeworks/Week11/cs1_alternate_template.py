from kivy.app import App
from kivy.uix.label import Label


class AlternateApp(App):

    def build(self):
        self.my_label = Label(text='Programming is fun')
        self.my_label.bind(on_touch_down=self.alternate)
        self.state = 0
        return self.my_label

    def alternate(self, instance, touch):
        if self.state == 0:
            self.my_label.text = 'It is fun to program'
            self.state = 1
        else:
            self.my_label.text = 'Programming is fun'
            self.state = 0
            
        print('Excuted callback')


myapp = AlternateApp()
myapp.run()
