import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #Initialize infinite keywords
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        # Set columns
        self.cols = 2
        
        # Add widgets
        self.name_label = Label(text="Name: ")
        self.add_widget(self.name_label) 
        
        #Add input boxes
        self.name_input = TextInput(multiline = False)
        self.add_widget(self.name_input)
        
        self.pizza_label = Label(text="Favourite pizza: ")
        self.add_widget(self.pizza_label) 
        
        self.pizza_input = TextInput(multiline = False)
        self.add_widget(self.pizza_input)
        
        self.color_label = Label(text="Favourite color: ")
        self.add_widget(self.color_label) 
        
        self.color_input = TextInput(multiline = False)
        self.add_widget(self.color_input)
        
        #Create submit button
        self.submit = Button(text = "Submit", font_size = 32)
        

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()