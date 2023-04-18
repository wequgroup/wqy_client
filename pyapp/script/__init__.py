import json
import time

from pyapp.script.action_play import ActionPlay
from pyapp.script.shell_play import ShellPlay


class Play:
    def __init__(self, msg, win):
        self.shellType = msg["shellType"]
        self.shellContent = msg["shellContent"]
        self.win = win

    def run(self):
        if self.shellType == 0:
            self.shell()
        if self.shellType == 1:
            self.action()

    def shell(self):
        self.write_log("开始执行脚本命令:" + self.shellContent)
        s = ShellPlay(self.shellContent)
        s.run()
        self.write_log("脚本命令执行结束")

    def action(self):
        self.write_log("开始执行操作回放:" + self.shellContent)
        a = ActionPlay(self.shellContent)
        a.run()
        self.write_log("操作回放执行结束")

    def write_log(self, msg):
        log = {"msg": msg, "time": time.strftime('%H:%M:%S')}
        self.win.evaluate_js(f"writeLog('{json.dumps(log)}')")
