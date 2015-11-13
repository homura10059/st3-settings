import sublime, sublime_plugin
import ctypes

class DisabledImeCommand(sublime_plugin.EventListener):
    def on_text_command(self, view, command_name, args):
        name = command_name.lower()
        # _enter_normal_modeはesc、exit_insert_modeはCtrl + [
        # Ctrl + [ も処理したいけど何だか挙動がおかしいのでやらない
        if (name == '_enter_normal_mode' or name == 'exit_insert_mode'):
            ctypes.windll.user32.keybd_event(17, 0, 0x2, 0)
            ctypes.windll.user32.keybd_event(29, 0, 0, 0)
