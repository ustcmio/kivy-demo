
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window


class Demo(App):
    def build(self):
        return Builder.load_file('login.kv',coding='utf-8')


Demo().run()
