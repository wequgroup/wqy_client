#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Mon
LastEditors: Mon
Date: 2022-03-21 17:01:39
LastEditTime: 2023-03-12 21:44:44
Description: 本地API，供前端JS调用
usage: 调用window.pywebview.api.<methodname>(<parameters>)从Javascript执行
'''

import os
import random
import sys

from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item

from api import g
from api.mqtt import MQTT
from pyapp.db.orm import ORM
from pyapp.script.action_play import ActionPlay
from pyapp.script.action_record import ActionRecord


class API:
    """本地API，供前端JS调用"""

    window = None
    orm = ORM()  # 操作数据库类

    def __init__(self):
        self.win_show = True
        self.listen = False
        self.thread_mqtt = None
        self.start_mq = False
        self.tray = self.app_tray()
        self.tray.run_detached()

    def show_app(self, *args, **kwargs):
        self.window.show()
        self.window.restore()

    def app_tray(self):
        icoPath = os.path.join('.', 'static', 'logo.png')
        image = Image.open(icoPath)
        tray = icon('微趣鸭', image, menu=menu(
            item(
                '显示主界面',
                self.show_app),
            item(
                '退出程序',
                self.close)
        ))
        return tray

    def get_device(self):
        """获取所有的设备"""
        return self.orm.get_device()

    def add_device(self, data: dict):
        """添加设备或者更新设备"""
        self.start_mq = False
        if data.get("action") == "add":
            self.orm.add_device(data.get("device_name"), data.get("device_id"),
                                data.get("device_password"), data.get("auto_online"))
        else:
            self.orm.update_device(data.get("device_name"), data.get("device_id"),
                                   data.get("device_password"), data.get("auto_online"))
        return "ok"

    def connect(self, device_id, device_password):
        """连接服务端"""
        if self.start_mq is False:
            self.start_mq = True
            self.thread_mqtt = MQTT(device_id, device_password, "mqtt-hw.wequ.net", 1883, False, API.window)
            self.thread_mqtt.start()
        return "ok"

    def diss_connect(self):
        """断开服务端"""
        g.STOP_MQ = True
        self.start_mq = False
        return "ok"

    def get_record(self):
        return self.orm.get_record()

    def set_record(self, name):
        action = ActionRecord(self.orm, str(random.randint(100000, 999999)), name)
        self.window.minimize()
        action.run()
        self.window.show()
        self.window.restore()
        return "ok"

    def run_record(self, id):
        content = self.orm.get_record_one(id)
        self.hide()
        action = ActionPlay(content)
        action.run()
        self.window.minimize()
        self.window.restore()
        return "ok"

    def delete_record(self, id):
        self.orm.delete_record(id)
        return "ok"

    def hide(self):
        """隐藏"""
        self.window.hide()
        return "ok"

    def minisize(self):
        """最小化"""
        self.window.minimize()
        return "ok"

    def close(self):
        """退出"""
        g.STOP_MQ = True
        self.window.destroy()
        return "ok"
