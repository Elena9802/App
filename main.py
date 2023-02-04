from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.screenmanager import MDScreenManager

P1 = 0
P2 = 0
P3 = 0

class Screen1(Screen):
    """ Экран с инструкцией """
    def move_next(self):
        global P1
        P1 = int(self.ids["p1_field"].text)

class Screen2(Screen):
    """ Экран приседаний """
    pass

class Screen3(Screen):
    """ Экран измерения пульса """
    def move_next(self):
        global P2
        P2 = int(self.ids["p2_field"].text)

class Screen4(Screen):
    """ Экран отдыха """
    pass

class Screen5(Screen):
    """ Экран измерения пульса """
    def move_next(self):
        global P3
        P3 = int(self.ids["p3_field"].text)
        screen6 = self.parent.get_screen("Screen6")
        screen6.ids["result_label"].text = f"P1={P1} P2={P2} P3={P3}"

class Screen6(Screen):
    """ Экран результата """
    pass

class MyApp(MDApp):
    def build(self):
        self.sm = MDScreenManager()
        self.sm.add_widget(Screen1(name="Screen1"))
        self.sm.add_widget(Screen2(name="Screen2"))
        self.sm.add_widget(Screen3(name="Screen3"))
        self.sm.add_widget(Screen4(name="Screen4"))
        self.sm.add_widget(Screen5(name="Screen5"))
        self.sm.add_widget(Screen6(name="Screen6"))
        return self.sm

MyApp().run()