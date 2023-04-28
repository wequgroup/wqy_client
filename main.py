#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Mon
LastEditors: Mon
Date: 2022-03-23 15:41:46
LastEditTime: 2023-03-15 22:28:20
Description: 生成客户端主程序
usage: 运行前，请确保本机已经搭建Python3开发环境，且已经安装 pywebview 模块。
"""
import argparse
import sys

import psutil

i = 0


def check_duck_pid():
    try:
        global i
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            service = str(p.name())
            if "WeDuck" in service:
                i += 1
    except:
        pass


if __name__ == "__main__":
    check_duck_pid()
    if i <= 1:
        from init import app

        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mini", dest="if_mini", help="is mini?")
        parser.add_argument("-c", "--cef", action="store_true", dest="if_cef", help="if_cef")
        args = parser.parse_args()
        ifCef = args.if_cef
        if_mini = args.if_mini
        app(ifCef, if_mini)
    else:
        sys.exit()
