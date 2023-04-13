import threading

from loguru import logger
from pynput import mouse, keyboard


class ActionRecord:
    def __init__(self):
        self.thread_mouse = None
        self.thread_keyboard = None
        self.tag = 0  # 1就结束
        self.controller = keyboard.Controller()

    def run(self):
        self.thread_keyboard = threading.Thread(target=self.func_keyboard)
        self.thread_mouse = threading.Thread(target=self.func_mouse_click)
        self.thread_mouse.start()
        self.thread_keyboard.start()

    @staticmethod
    def on_mouse_click(x, y, click, pressed):
        if click == mouse.Button.left:
            logger.debug('鼠标左键按下了')
        elif click == mouse.Button.right:
            logger.debug('鼠标右键按下了')
            return False
        else:
            logger.debug('中间滚轮按下了')

    @staticmethod
    def on_keyboard_press(key):
        """
        按键时记录所按下的键
        :param key:
        :return:
        """
        logger.debug(f'{key} :被按下了')

    def on_keyboard_release(self, key):
        """
        释放按键处理函数
        :param key:
        :return:
        """
        if key == keyboard.Key.esc:
            self.tag = 1
            return False

    def func_keyboard(self):
        """
        键盘的按下/释放的监听
        :return:
        """
        with keyboard.Listener(on_press=self.on_keyboard_press,
                               on_release=self.on_keyboard_release) as keyboard_listener:
            keyboard_listener.join()

    def func_mouse_click(self):
        """
        监听鼠标
        :return:
        """
        with mouse.Listener(on_click=self.on_mouse_click) as mouse_listener:
            mouse_listener.join()


d = ActionRecord()
d.run()
