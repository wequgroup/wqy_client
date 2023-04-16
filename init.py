import os
import sys

import webview
import json
from api.api import API
from pyapp.config.config import Config
from pyapp.db.db import DB

api = API()  # 本地接口
cfg = Config()  # 配置
db = DB()  # 数据库类
cfg.init()


def on_minimized():
    pass


def on_shown():
    # print('程序启动')
    db.init()  # 初始化数据库


def on_loaded():
    # print('DOM加载完毕')
    pass


def on_closing():
    # print('程序关闭')
    pass


def on_resized(width, height):
    pass

def app(ifCef=False):
    # 是否为开发环境
    Config.devEnv = sys.flags.dev_mode

    # 前端页面目录
    if Config.devEnv:
        # 开发环境
        MAIN_DIR = f'http://localhost:{Config.devPort}/'
        template = os.path.join(MAIN_DIR, "")  # 设置页面，指向远程
    else:
        # 生产环境
        MAIN_DIR = os.path.join(".", "web")
        template = os.path.join(MAIN_DIR, "index.html")  # 设置页面，指向本地

    # 创建窗口
    window = webview.create_window(title=Config.appName, url=template, js_api=api, width=590, height=600,
                                   min_size=(600, 500), resizable=False, frameless=True, easy_drag=True)

    # 获取窗口实例
    API.window = window
    # 绑定事件
    window.events.shown += on_shown
    window.events.loaded += on_loaded
    window.events.closing += on_closing
    window.events.minimized += on_minimized
    window.events.resized += on_resized

    # CEF模式
    guiCEF = 'cef' if ifCef else None
    # 启动窗口
    webview.start(debug=Config.devEnv, http_server=True, gui=guiCEF)