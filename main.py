from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import os

from questions import QuestionsScreen  # صفحه‌ی سوالات

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
        layout.add_widget(Label(text="صفحه‌ی اصلی برنامه", font_size='24sp'))
        self.add_widget(layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())

        first_run = not os.path.exists("user_data.txt")
        if first_run:
            sm.add_widget(QuestionsScreen(name='questions'))
        sm.add_widget(MainScreen(name='main'))

        sm.current = 'questions' if first_run else 'main'
        return sm

if __name__ == '__main__':
    MyApp().run()
