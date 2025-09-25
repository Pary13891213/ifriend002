from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from datetime import datetime

class DatePicker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='horizontal', spacing=10, **kwargs)

        current_year = datetime.now().year
        years = [str(y) for y in range(current_year - 100, current_year + 1)]
        months = [str(m).zfill(2) for m in range(1, 13)]
        days = [str(d).zfill(2) for d in range(1, 32)]

        self.year_spinner = Spinner(text=str(current_year), values=years, size_hint=(0.3, 1))
        self.month_spinner = Spinner(text='01', values=months, size_hint=(0.3, 1))
        self.day_spinner = Spinner(text='01', values=days, size_hint=(0.3, 1))

        self.add_widget(Label(text="روز:"))
        self.add_widget(self.day_spinner)
        self.add_widget(Label(text="ماه:"))
        self.add_widget(self.month_spinner)
        self.add_widget(Label(text="سال:"))
        self.add_widget(self.year_spinner)

    def get_date(self):
        return f"{self.year_spinner.text}/{self.month_spinner.text}/{self.day_spinner.text}"
