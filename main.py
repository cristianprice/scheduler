from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationItem, MDNavigationBar



class MainNavigationItem(MDNavigationItem):
    text = StringProperty()
    icon = StringProperty()

class AppScreen(MDScreen):
    image_size = StringProperty()

class SchedulerApp(MDApp):
    def build(self):
        return Builder.load_file("navigation_bar.kv")

    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        self.root.ids.screen_manager.current = item_text

    def run_code(self,text):
        print('Running', text)
        eval(text)

    def format_code(self, *args):
        print(args)


SchedulerApp().run()