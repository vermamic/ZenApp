import kivy 

from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button 
from kivy.uix.screenmanager import ScreenManager, Screen


class Intro_Screen(App):
    
    def build(self):
        layout = FloatLayout(size = (1000,1000))
        button_start = Button(text = 'Enter Zen Mode', font_size = '20sp', background_color = (1,1,1,1), color = (1,1,1,1), size = (64,32), size_hint = (0.2, 0.1), pos = (800,700))
        button_profile = Button(text = 'User Profile', font_size = '20sp', background_color = (1,1,1,1), color = (1,1,1,1), size = (64,32), size_hint = (0.2, 0.1), pos = (800,500))
        layout.add_widget(button_start)
        layout.add_widget(button_profile)
        return layout
    
if __name__ == '__main__':
    Intro_Screen().run()