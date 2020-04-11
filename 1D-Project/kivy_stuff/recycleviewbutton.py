from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
Builder.load_string('''
<RV>:
    viewclass: 'myView'
    RecycleBoxLayout:
        default_size: None, dp(200)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'


<myView@BoxLayout>:
    BoxLayout:
        orientation: 'horizontal'


        BoxLayout:
            orientation: 'vertical'
            on_release:

            Button:
                size_hint: (1,1)
                background_normal: 'C:/Users/Arsalan/Desktop/dummyImage2.jpg'
                background_down: 'C:/Users/Arsalan/Desktop/dummyImage1.png'
                text: 
                text_size: self.size
                halign: 
                valign: 'middle'

            Label:
                size_hint: (1,0.3)
                text: 'Product summary'
                text_size: self.size 
                halign:
                valign: 'middle'
                canvas.before:
                    Color:
                        rgba: (0.6, 0.7, 0.4, 1)
                    Rectangle:
                        size: self.size
                        pos: self.pos
            BoxLayout:
                size_hint :(1,0.01)

            Label:
                size_hint: (1,0.3)
                text: 'Rs 600'
                text_size: self.size 
                halign:
                valign: 'middle'




        BoxLayout:
            orientation: 'vertical'
            size_hint: (0.001,1)




        BoxLayout:
            orientation: 'vertical'
            on_release:

            Button:
                size_hint: (1,1)
                background_normal: 'C:/Users/Arsalan/Desktop/dummyImage2.jpg'
                background_down: 'C:/Users/Arsalan/Desktop/dummyImage1.png'
                text: 
                text_size: self.size
                halign: 
                valign: 'middle'

            Label:
                size_hint: (1,0.3)
                text: 'Product summary'
                text_size: self.size 
                halign:
                valign: 'middle'
                canvas.before:
                    Color:
                        rgba: (0.6, 0.7, 0.4, 1)
                    Rectangle:
                        size: self.size
                        pos: self.pos
            BoxLayout:
                size_hint :(1,0.01)

            Label:
                size_hint: (1,0.3)
                text: 'Rs 600'
                text_size: self.size 
                halign:
                valign: 'middle'




''')
class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]
class TestApp(App):
    def build(self):
        return RV()
if __name__ == '__main__':
    TestApp().run()