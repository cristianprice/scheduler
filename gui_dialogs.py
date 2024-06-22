from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (MDDialog, MDDialogHeadlineText,
                               MDDialogSupportingText,
                               MDDialogButtonContainer, MDDialogIcon)
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from functools import partial


class Ref:
    def __init__(self):
        self.dlg = None


def close_dialog(btn: MDButton) -> None:
    potential_dlg = btn.parent
    while(potential_dlg):
        if isinstance(potential_dlg, MDDialog):
            potential_dlg.dismiss()
            return
        potential_dlg = potential_dlg.parent


def show_info_dialog(text: str, type_of_dialog: str = "information"):

    dlg: MDDialog = MDDialog(
        MDDialogIcon(
            icon=type_of_dialog,
        ),
        MDDialogHeadlineText(
            text=type_of_dialog.title(),
            halign="left",
        ),
        MDDialogSupportingText(
            text=text,
            halign="left",
        ),
        MDDialogButtonContainer(
            Widget(),
            MDButton(
                MDButtonText(text="Ok"),
                style="text",
                on_release=close_dialog,
            ),
            spacing="8dp",
        ),
    )

    dlg.open()
