from questions import QuestionsScreen

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, NoTransition

Window.clearcolor = (204/255, 236/255, 255/255, 1)
Window.size = (360, 640) 

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.word = "ifriend"
        self.delay = 0.2

        self.word_box = BoxLayout(
            orientation='horizontal',
            spacing=5,
            size_hint=(None, None),
            height=50,
            width=len(self.word) * 30,
            pos_hint={'center_x': 0.465, 'center_y': 0.5}
        )

        self.add_widget(self.word_box)
        Clock.schedule_once(self.show_letters, 0)

    def show_letters(self, dt):
        for i, char in enumerate(self.word):
            lbl = Label(
                text=char,
                font_size='40sp',
                color=(0.470, 0.564, 0.611, 0),
                size_hint=(None, None),
                size=(30, 50)
            )
            self.word_box.add_widget(lbl)

            anim = Animation(color=(0.470, 0.564, 0.611, 1), duration=0.3)
            Clock.schedule_once(lambda dt, a=anim, l=lbl: a.start(l), i * self.delay)

        total_time = len(self.word) * self.delay + 0.5
        Clock.schedule_once(self.go_to_next_screen, total_time)

    def go_to_next_screen(self, dt):
        # گرفتن صفحه دوم از ScreenManager
        next_screen = self.manager.get_screen('questions')

        # انیمیشن محو شدن صفحه اول
        anim_out = Animation(opacity=0, duration=0.6)

        # انیمیشن ظاهر شدن صفحه دوم
        anim_in = Animation(opacity=1, duration=0.6)

        # قبل از شروع انیمیشن، صفحه دوم رو فعال کنیم
        self.manager.current = 'questions'

        # شروع انیمیشن روی صفحه دوم
        anim_in.start(next_screen)

        # شروع انیمیشن روی صفحه اول
        anim_out.start(self)

    def switch_to_questions(self, *args):
        self.manager.current = 'questions'

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())  # بدون افکت ورق زدن
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(QuestionsScreen(name='questions'))
        return sm

MyApp().run()
