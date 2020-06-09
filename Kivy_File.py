from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock


class MainWindow(Screen):
    pass

class SecondWindow(Screen):

    #Set the variable number as a numeric property
    number = NumericProperty()

    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        Clock.schedule_interval(self.increment_time, 0.1)

        self.increment_time(0)

    #Function which increments the time by 0.1
    def increment_time(self, interval):
        self.number += .1

    #Function which starts the incrementing time
    def start(self):
        #Removes a previously schedule event, hence the timer that is running right now
        Clock.unschedule(self.increment_time)
        #Starts a scheduled timer incrementing at an interval of 0.1
        Clock.schedule_interval(self.increment_time, 0.1)

    #Function which stops incrementing the time
    def stop(self):
        Clock.unschedule(self.increment_time)


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('screen.kv')

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyMainApp().run()