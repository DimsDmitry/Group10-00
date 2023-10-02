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
    # зависимость от количества сделанных приседаний
    value = NumericProperty(0)
    # сделаны ли все перемещения
    finished = BooleanProperty(False)

    def __init__(self,
                 total=10, steptime=1, autorepeat=True,
                 bcolor=(.65, .24, .76, 1), btext_inprogress='Приседание',
                 **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.autorepeat = autorepeat
        self.btext_inprogress = btext_inprogress
        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime / 2)
                          + Animation(pos_hint={'top': 1.0}, duration=steptime / 2))
        self.animation.on_progress = self.next
        self.btn = Button(size_hint=(1, 0.1), pos_hint={'top': 1.0}, background_color=bcolor)
        self.add_widget(self.btn)

    def start(self):
        self.value = 0
        self.finished = False
        self.btn.text = self.btext_inprogress
        if self.autorepeat:
            self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step):
        if step == 1.0:
            self.value += 1
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True
