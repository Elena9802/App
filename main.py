from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from kivymd.uix.label import MDLabel
from  kivy.properties import BooleanProperty

P1 = 0
P2 = 0
P3 = 0
age = 0

class CountDown(MDLabel):
    is_done = BooleanProperty(False)

    def start(self):
        Clock.schedule_interval(self.tick, 1)

    def tick(self, tm):
        print(tm)
        t = int(self.text)
        if t > 0:
            self.text = str(t - 1)
        else:
            self.is_done = True 
            self.text = 'Готово'
            return False

class Screen0(Screen):
    def move_next(self):
        global age
        age_field = self.ids['age_field']
        try:
            P1 = int(self.ids["p1_field"].text)
            if age < 7:
                age_field.error = True
                age_field.helper_text = 'Минимальный возраст 7 лет'
            else:
                self.parent.transition.direction = "left"
                self.parent.current = "Screen1"
        except:
            age_field.error = True
            age_field.helper_text = 'Введите целое число'

class Screen1(Screen):
    """ Экран с инструкцией """
    def move_next(self):
        global P1
        p1_field = self.ids['p1_field']
        try:
            P1 = int(self.ids["p1_field"].text)
            if P1 <= 0:
                p1_field.error = True
                p1_field.helper_text = 'Введите число больше 0'
            else:
                self.parent.transition.direction = "left"
                self.parent.current = "Screen2"
        except:
            p1_field.error = True
            p1_field.helper_text = 'Введите целое число'

class Screen2(Screen):
    """ Экран приседаний """
    pass

class Screen3(Screen):
    """ Экран измерения пульса """
    def move_next(self):
        global P2
        p2_field = self.ids['p2_field']
        try:
            P2 = int(self.ids["p2_field"].text)
        except:
            p2_field.error = True
            p2_field.helper_text = 'Введите целое число'




class Screen4(Screen):
    """ Экран отдыха """
    pass

class Screen5(Screen):
    """ Экран измерения пульса """
    def move_next(self):
        global P3
        P3 = int(self.ids["p3_field"].text)
        screen6 = self.parent.get_screen('Screen6')
        kf = (4 * (P1 + P2 + P3) - 200 ) / 10
        n = (min(15, age) - 7) // 2
        x = 21 - 1.5 * n
        if kf >= x:
            res = 'низкий'
        elif kf >= x - 4 and kf < x:
            res = 'Удолетворительный'
        elif kf >= x - 9 and kf < x - F:
            res = 'Средний'
        elif kf >= x - 14.6 and kf < x - 9:
            res = 'Выше мреднего'
        else:
            res = 'Высокий'
        screen6.aids['results_label'].text = f'Ваш результат : {res} Ваш коэф. '
        



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