import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs): #Initiliaze keywords
        super(MyGrid, self).__init__(**kwargs)
        self.cols=1
        self.add_widget(Label(text="Enter Zen Mode"))

        self.add_widget(Label(text="Visit Garden"))

        self.add_widget(Label(text="Profile"))
        self.profile = TextInput(multiline=False)
        self.add_widget(self.profile)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
