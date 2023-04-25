import subprocess


class ShellPlay:
    def __init__(self, content):
        self.content = content

    def run(self):
        subprocess.run(self.content, shell=True)
