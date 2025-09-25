from datepicker import DatePicker
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager


questions_data = [
    {"type": "text", "question": "اسم شما چیه؟"},
    {"type": "date", "question": "تاریخ تولدتون چیه؟"},
    {"type": "single", "question": "جنسیت شما؟", "options": ["زن", "مرد", "ترجیح می‌دم نگم", "گزینه‌ی دیگر"]},
    {"type": "multi", "question": "هدف اصلی‌تون از استفاده از این برنامه چیه؟", "options": ["برنامه‌ریزی روزانه", "ایجاد عادت‌های مثبت", "ثبت خاطرات و احساسات", "مدیریت زمان", "حال خوب"]},
    {"type": "single", "question": "معمولاً چه ساعتی بیدار می‌شید؟", "options": ["قبل از ۶ صبح", "بین ۶ تا ۸ صبح", "بین ۸ تا ۱۰ صبح", "بعد از ۱۰ صبح"]},
    {"type": "single", "question": "معمولاً چه ساعتی می‌خوابید؟", "options": ["قبل از ۱۰ شب", "بین ۱۰ تا ۱۲ شب", "بعد از ۱۲ شب"]},
    {"type": "single", "question": "در حال حاضر بیشتر وقتت صرف چه کارهایی می‌شه؟", "options": ["کار یا تحصیل", "مراقبت از خانواده", "فعالیت‌های شخصی و تفریحی", "استراحت و ریکاوری", "ترکیبی از موارد بالا", "هنوز مشخص نیست، در حال کشف هستم"]},
    {"type": "single", "question": "چه چیزی بیشتر از همه بهت انگیزه می‌ده؟", "options": ["رسیدن به هدف‌های شخصی", "تأثیرگذاری روی دیگران", "حس پیشرفت و رشد", "تشویق و حمایت دیگران", "آرامش ذهنی و تعادل", "تجربه‌های جدید و هیجان‌انگیز", "نمی‌دونم، دنبالشم"]},
    {"type": "multi", "question": "به چه چیزهایی علاقه‌مند هستی؟", "options": ["ورزش", "هنرهای تجسمی", "موسیقی", "مطالعه و یادگیری", "طبیعت و سفر", "بازی‌های کامپیوتری", "فیلم و سریال", "آشپزی", "مد و استایل", "روابط اجتماعی", "نوشتن", "مراقبه", "فناوری", "کارآفرینی", "حیوانات", "کارهای داوطلبانه"]},
    {"type": "multi", "question": "معمولاً چه احساسی داری؟", "options": ["پرانرژی و مثبت", "خسته ولی امیدوار", "مضطرب یا نگران", "بی‌انگیزه", "متغیر", "آرام", "هیجان‌زده", "غمگین", "سردرگم", "راضی", "در حال رشد"]},
    {"type": "single", "question": "سبک زندگی‌ات رو چطور توصیف می‌کنی؟", "options": ["منظم", "پرمشغله", "آزاد", "وابسته به شرایط", "نیمه‌منظم", "در حال تلاش", "آرام", "فعال"]}
]

class QuestionsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opacity = 0
        self.answers = {}
        self.current_index = 0

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.add_widget(self.layout)

        self.show_question()

    def show_question(self):
        self.layout.clear_widgets()
        q = questions_data[self.current_index]

        self.layout.add_widget(Label(text=q["question"], font_size='20sp'))

        self.response_widgets = []

        if q["type"] == "text":
            input_box = TextInput(multiline=False)
            self.response_widgets.append(input_box)
            self.layout.add_widget(input_box)

        elif q["type"] == "date":
            input_box = TextInput(hint_text="مثلاً 1379/05/23")
            self.response_widgets.append(input_box)
            self.layout.add_widget(input_box)

        elif q["type"] == "single":
            for option in q["options"]:
                btn = ToggleButton(text=option, group="group"+str(self.current_index))
                self.response_widgets.append(btn)
                self.layout.add_widget(btn)

        elif q["type"] == "multi":
            for option in q["options"]:
                box = BoxLayout(orientation='horizontal')
                chk = CheckBox()
                lbl = Label(text=option)
                box.add_widget(chk)
                box.add_widget(lbl)
                self.response_widgets.append((chk, option))
                self.layout.add_widget(box)

        submit_btn = Button(text="بله", size_hint=(1, 0.2))
        submit_btn.bind(on_press=self.submit_answer)
        self.layout.add_widget(submit_btn)

    def submit_answer(self, instance):
        q = questions_data[self.current_index]
        if q["type"] == "text" or q["type"] == "date":
            self.answers[q["question"]] = self.response_widgets[0].text

        elif q["type"] == "single":
            for btn in self.response_widgets:
                if btn.state == 'down':
                    self.answers[q["question"]] = btn.text
                    break

        elif q["type"] == "multi":
            selected = [opt for chk, opt in self.response_widgets if chk.active]
            self.answers[q["question"]] = selected

        self.current_index += 1
        if self.current_index < len(questions_data):
            self.show_question()
        else:
            self.manager.current = 'main'  # رفتن به صفحه‌ی بعدی

