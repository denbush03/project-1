from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

class RandomNumberApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Random number will display here")
        self.layout.add_widget(self.label)
        
        self.button = Button(text="Generate Random Number")
        self.button.bind(on_press=self.generate_random_number)
        self.layout.add_widget(self.button)
        
        return self.layout
    
    def generate_random_number(self, instance):
        random_num = random.randint(1, 100)
        self.label.text = f"Random Number: {random_num}"

if __name__ == "__main__":
    RandomNumberApp().run()