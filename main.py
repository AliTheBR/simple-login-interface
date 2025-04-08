from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.1, 0.1, 0.2, 1)  # Dark Background Color
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        layout = RelativeLayout()

        # Background image
        background = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Login box container
        login_box = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint=(None, None), size=(350, 250),
                              pos_hint={'center_x': 0.5, 'center_y': 0.5})

        with login_box.canvas.before:
            Color(0, 0, 0, 0.7)  # Dark transparent box
            self.rounded_rect = RoundedRectangle(size=login_box.size, pos=login_box.pos, radius=[20])

        login_box.bind(size=self.update_rounded_rect, pos=self.update_rounded_rect)

        title = Label(text="Login", font_size=30, bold=True, color=(1, 1, 1, 1), size_hint=(1, 0.2))

        self.username = TextInput(hint_text='Email Address', multiline=False, size_hint=(1, 0.2))
        self.password = TextInput(hint_text='Password', password=True, multiline=False, size_hint=(1, 0.2))

        login_button = Button(text='LOG IN', size_hint=(1, 0.2), background_color=(0, 0.5, 1, 1))
        login_button.bind(on_press=self.validate_login)

        login_box.add_widget(title)
        login_box.add_widget(self.username)
        login_box.add_widget(self.password)
        login_box.add_widget(login_button)

        layout.add_widget(login_box)
        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def update_rounded_rect(self, instance, *args):
        self.rounded_rect.size = instance.size
        self.rounded_rect.pos = instance.pos

    def validate_login(self, instance):
        username = self.username.text
        password = self.password.text
        '''
        can be used for checking passwords
        '''

class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        return sm


if __name__ == '__main__':
    LoginApp().run()
