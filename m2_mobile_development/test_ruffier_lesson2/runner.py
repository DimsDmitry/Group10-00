# напиши модуль для работы с анимацией
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.properties import *


class Runner(BoxLayout):
    #зависимость от количества сделанных приседаний
    value = NumericProperty(0)
    #сделаны ли все перемещения
    finished = BooleanProperty(False)

    def __init__(self,
                 total, steptime, autorepeat,
                 bcolor=(.65, .24, .76, 1), btext_inprogress='Приседание',
                 **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.autorepeat = autorepeat
        self.btext_inprogress = btext_inprogress
        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime/2
                        + Animation(pos_hint={'top': 1.0}, duration=steptime/2)

    def start(self):
        pass

    def next(self, widget, step):
        pass