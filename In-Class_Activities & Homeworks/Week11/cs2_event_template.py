from kivy.app import App
from kivy.uix.label import Label


class SlideDetectApp(App):
    def build(self):
        self.label = Label(text='Slide Me')
        self.label.bind(on_touch_move=self.detect)
        return self.label

    def detect(self, instance, touch):
        if not instance.collide_point(touch.x, touch.y):
          return False

        if touch.dx < -40:
            self.label.text = 'Slide Left'
        if touch.dx > 40:
            self.label.text = 'Slide Right'
        if touch.dy < -40:
            self.label.text = 'Slide Down'
        if touch.dy > 40:
            self.label.text = 'Slide Up'
        return True


SlideDetectApp().run()
