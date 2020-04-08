from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 

class MyLabel(Label):

    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)

class FloatInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = 'input value'
        self.input_filter = 'float'

class Investment(App):

    def build(self):
        layout = GridLayout(cols=2)
        self.l1 = MyLabel(text="Investment Ammount",
                     font_size=24, halign='left', valign='middle')
        layout.add_widget(self.l1)

        self.r1 = FloatInput(text='')
        layout.add_widget(self.r1)
        
        self.l2 = MyLabel(text="Years",
                     font_size=24, halign='left', valign='middle')
        layout.add_widget(self.l2)

        self.r2 = FloatInput(text='')
        layout.add_widget(self.r2)

        self.l3 = MyLabel(text="Annual Interest Rate",
                     font_size=24, halign='left', valign='middle')
        layout.add_widget(self.l3)

        self.r3 = FloatInput(text='')
        layout.add_widget(self.r3)

        self.l4 = MyLabel(text="Future Value",
                     font_size=24, halign='left', valign='middle')
        layout.add_widget(self.l4)

        self.future_val = MyLabel(text="",
                     font_size=24, halign='left', valign='middle')
        layout.add_widget(self.future_val)

        self.btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
        layout.add_widget(self.btn)
        return layout

    def calculate(self, instance):
        try:
            inv_amt = float(self.r1.text)
        except:
            inv_amt = 0
        try:
            years = float(self.r2.text)
        except:
            years = 0
        try:
            mth_int_rate = float(self.r3.text)
        except:
            mth_int_rate = 0
            
        self.future_val.text = str(round(inv_amt*(1 + mth_int_rate/1200)**(12*years),2))



Investment().run()
