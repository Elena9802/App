# App
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.screenmanager import MDScreenManager

sm = MDScreenManager()

def next(button):
    sm.transition.direction = "left"
    sm.current = 'Screen2'

def back(button):
    sm.transition.direction = "right"
    sm.current = 'Screen1'

class Screen1(Screen):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        main_layout = BoxLayout(
            orientation = "vertical"
        )

        btn = MDRaisedButton(text = "Далее", font_size = "40sp", on_press = next, size_hint=(.5, None), pos_hint={'center_x': 0.5})
        main_layout.add_widget(btn)
        self.add_widget(main_layout)

class Screen2(Screen):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        main_layout = BoxLayout(
            orientation = "vertical"
        )

        btn2 = MDRaisedButton(text = "Назад", font_size = "40sp", on_press = back)
        main_layout.add_widget(btn2)
        self.add_widget(main_layout)

class myApp(MDApp):
    def build(self):
      sm.add_widget(Screen1(name='Screen1'))
      sm.add_widget(Screen2(name='Screen2'))
      sm.current = "Screen1"
      return sm


myApp().run()
