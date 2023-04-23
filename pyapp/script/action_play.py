from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import json, time

special_keys = {"Key.shift": Key.shift, "Key.tab": Key.tab, "Key.caps_lock": Key.caps_lock, "Key.ctrl": Key.ctrl,
                "Key.ctrl_l": Key.ctrl_l,
                "Key.alt": Key.alt, "Key.cmd": Key.cmd, "Key.cmd_r": Key.cmd_r, "Key.alt_r": Key.alt_r,
                "Key.ctrl_r": Key.ctrl_r, "Key.shift_r": Key.shift_r, "Key.enter": Key.enter,
                "Key.backspace": Key.backspace, "Key.f19": Key.f19, "Key.f18": Key.f18, "Key.f17": Key.f17,
                "Key.f16": Key.f16, "Key.f15": Key.f15, "Key.f14": Key.f14, "Key.f13": Key.f13,
                "Key.media_volume_up": Key.media_volume_up, "Key.media_volume_down": Key.media_volume_down,
                "Key.media_volume_mute": Key.media_volume_mute, "Key.media_play_pause": Key.media_play_pause,
                "Key.f6": Key.f6, "Key.f5": Key.f5, "Key.right": Key.right, "Key.down": Key.down, "Key.left": Key.left,
                "Key.up": Key.up, "Key.page_up": Key.page_up, "Key.page_down": Key.page_down, "Key.home": Key.home,
                "Key.end": Key.end, "Key.delete": Key.delete, "Key.space": Key.space}


class ActionPlay:
    def __init__(self, content, run_count=1, sleep_time=None):
        self.content = content
        self.script_data = None
        self.mouse = MouseController()
        self.keyboard = KeyboardController()
        self.run_count = run_count
        self.sleep_time = sleep_time

    def load_script(self):
        self.script_data = json.loads(self.content)

    def run(self):
        self.load_script()
        for loop in range(self.run_count):
            for index, obj in enumerate(self.script_data):
                action, _time = obj['action'], obj['_time']
                try:
                    next_movement = self.script_data[index + 1]['_time']
                    pause_time = next_movement - _time
                except IndexError as e:
                    pause_time = 1

                if action == "pressed_key" or action == "released_key":
                    key = obj['key'] if 'Key.' not in obj['key'] else special_keys[obj['key']]
                    if action == "pressed_key":
                        self.keyboard.press(key)
                    else:
                        self.keyboard.release(key)
                    time.sleep(pause_time)
                else:
                    move_for_scroll = True
                    x, y = obj['x'], obj['y']
                    if action == "scroll" and index > 0 and (
                            self.script_data[index - 1]['action'] == "pressed" or
                            self.script_data[index - 1]['action'] == "released"):
                        if x == self.script_data[index - 1]['x'] and y == self.script_data[index - 1]['y']:
                            move_for_scroll = False
                    self.mouse.position = (x, y)
                    if action == "pressed" or action == "released" or action == "scroll" and move_for_scroll is True:
                        time.sleep(0.1)
                    if action == "pressed":
                        self.mouse.press(Button.left if obj['button'] == "Button.left" else Button.right)
                    elif action == "released":
                        self.mouse.release(Button.left if obj['button'] == "Button.left" else Button.right)
                    elif action == "scroll":
                        horizontal_direction, vertical_direction = obj['horizontal_direction'], obj[
                            'vertical_direction']
                        self.mouse.scroll(horizontal_direction, vertical_direction)
                    if self.sleep_time:
                        time.sleep(self.sleep_time)
                    else:
                        time.sleep(pause_time)
