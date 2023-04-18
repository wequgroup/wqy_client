import os


class ShellPlay:
    def __init__(self, content):
        self.content = content

    def run(self):
        res = os.system(self.content)
        if res == 0:
            print("error")
        else:
            print("success")
