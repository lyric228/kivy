from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class MyApp(App):
    def build(self):
        manager = ScreenManager(transition=WipeTransition())
        manager.add_widget(FirstScreen(name="1"))
        manager.add_widget(SecondScreen(name="2"))
        return manager


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(
            cols=1,
            padding=10,
            spacing=10,
        )
        note_layout = GridLayout(
            cols=2,
            spacing=10,
            size_hint=(1, None),
            height="32px",
            pos_hint={"top": 1},
        )
        button = Button(
            text="Редактировать",
            size_hint=(None, 1),
            width="128px",
        )
        label = Label(
            text="Заметка",
            size_hint=(1, 1),
            valign="middle",
            halign="left",
            text_size=(64, 16),
            bold=1,
        )
        layout.add_widget(note_layout)
        note_layout.add_widget(label)
        note_layout.add_widget(button)
        button.on_press = self.next_scr
        self.add_widget(layout)

    def next_scr(self):
        self.manager.current = "2"


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(
            orientation="vertical",
            padding=100,
            spacing=10,
        )
        button = Button(
            text="Кнопка",
            size_hint=(0, 0),
            pos_hint={"center_x": .5},
            background_color=(1.0, 0.7, 0.2, 1.0),
        )
        layout.add_widget(button)
        button.on_press = self.next_scr
        self.add_widget(layout)

    def next_scr(self):
        self.manager.current = "1"


app = MyApp()
app.run()
