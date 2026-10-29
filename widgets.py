from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from config import QUANTITIES
from core import calc_total_intake


class MyLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
class MyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyFullLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        self.calc_layouts = []
        
        for quantity in QUANTITIES:
        
            calc_layout = MyCalcLayout(quantity["name"], "Apports (pour 100 g)", quantity["unit"], "Quantité", "g", "Apports (total)", quantity["unit"], calc_total_intake)
            self.calc_layouts.append(calc_layout)
            self.add_widget(calc_layout)
            
        self.calculate_btn = MyButton(text="Calculer")
        self.calculate_btn.bind(on_press=self.on_calculate)
        self.add_widget(self.calculate_btn)
        
    def on_calculate(self):
        for calc_layout in self.calc_layouts:
            calc_layout.update()
            

class MyCalcLayout(BoxLayout):
    def __init__(self, title, quantity_1, unit_1, quantity_2, unit_2, quantity_3, unit_3, callback, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "horizontal"
        
        self.callback = callback
        self.title_label = MyLabel(text=title)
        self.first = MyAmountInput(quantity_1, unit_1)
        self.second = MyAmountInput(quantity_2, unit_2)
        self.result = MyAmountLabel(quantity_3, unit_3)
        
    @property
    def value(self):
        return self.callback(self.first.value, self.second.value)
    
    def update(self):
        self.result.update(value=self.value)


class MyAmountLabel(BoxLayout):
    def __init__(self, title, unit, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        
        self.title_label = MyLabel(text=title)
        self.text_label = MyLabel(text="")
        self.unit_label = MyLabel(text=unit)
        
        frame = BoxLayout(
            orientation="horizontal",
        )
        
        self.add_widget(self.title_label)
        self.add_widget(frame)
        frame.add_widget(self.text_label)
        frame.add_widget(self.unit_label)
    
    @property
    def value(self):
        return self.text_label.value
    
    def update(self, value):
        self.text_label.value = value


class MyAmountInput(BoxLayout):
    def __init__(self, title, unit, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        
        self.title_label = MyLabel(text=title)
        self.text_input = MyTextInput()
        self.unit_label = MyLabel(text=unit)
        
        frame = BoxLayout(
            orientation="horizontal",
        )
        
        self.add_widget(self.title_label)
        self.add_widget(frame)
        frame.add_widget(self.text_input)
        frame.add_widget(self.unit_label)
        
    @property
    def value(self):
        return self.text_input.value

    def reset(self):
        self.text_input.value = ""
