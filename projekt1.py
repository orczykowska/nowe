import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.button import Label
from kivy.graphics import Color
from kivy.uix.boxlayout import BoxLayout

class HellowordApp(App):
    def build(self):
        return BoxLayout()
        return Label()


Helloword = HellowordApp()
Helloword.run()
