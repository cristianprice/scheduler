
import contextlib
import io
from gui_dialogs import show_info_dialog
from kivymd.uix.navigationbar import MDNavigationItem, MDNavigationBar
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
import sys
from kivy import platform

if platform == "android":
        from android.permissions import request_permissions, Permission  # pylint: disable=import-error # type: ignore
        request_permissions([Permission.READ_EXTERNAL_STORAGE,
                            Permission.WRITE_EXTERNAL_STORAGE,
                            Permission.INTERNET,
                            Permission.ACCESS_NETWORK_STATE])



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


if __name__ == "__main__":
    app = SchedulerApp()
    app.run()
