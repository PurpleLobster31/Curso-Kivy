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
        self.cols = 1
        
        #Create second grid layout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        
        # Add widgets and input boxes
        self.name_label = Label(text="Name: ")
        self.top_grid.add_widget(self.name_label) 

        self.name_input = TextInput(multiline = False)
        self.top_grid.add_widget(self.name_input)
        
        self.pizza_label = Label(text="Favourite pizza: ")
        self.top_grid.add_widget(self.pizza_label) 
        
        self.pizza_input = TextInput(multiline = False)
        self.top_grid.add_widget(self.pizza_input)
        
        self.color_label = Label(text="Favourite color: ")
        self.top_grid.add_widget(self.color_label) 
        
        self.color_input = TextInput(multiline = False)
        self.top_grid.add_widget(self.color_input)
        
        #Add top_grid to app
        self.add_widget(self.top_grid)
        
        #Create submit button
        self.submit = Button(text = "Submit", font_size = 32)
        #Bind the button
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)
    
    def press(self, instance):
        name = self.name_input.text
        pizza = self.pizza_input.text
        color = self.color_input.text
        
        #print(f'Hello, my name is {name}; I like {pizza} pizza. Also, my favourite color is {color}!')
        #Printing on the screen!
        self.add_widget(Label(text = f"Hey {name}! I know your favourite pizza is {pizza}, and your favourite color is {color}! Got ya!"))
        
        #Clear the input boxes
        self.name_input.text = ''
        self.pizza_input.text = ''
        self.color_input.text = ''
        

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()