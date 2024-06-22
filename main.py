from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationItem, MDNavigationBar
from gui_dialogs import show_info_dialog

import io
import contextlib


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

    def run_code(self, text):
        print('Running', text)

        output: io.StringIO = io.StringIO()
        with contextlib.redirect_stdout(output):
            try:
                exec(text)
            except Exception as e:
                output.write(str(e))
                show_info_dialog(output.getvalue(), 'error')
                return

        output_value = output.getvalue()
        show_info_dialog(output_value)

    def format_code(self, *args):
        print(args)


SchedulerApp().run()
