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
import sys

import psutil

import argparse

if __name__ == "__main__":
    i = 0
    pids = psutil.pids()
    list = []
    for pid in pids:
        p = psutil.Process(pid)
        list.append(p.name())
        service = str(p.name())
        if "WeDuck" in service:
            print(service)
            i += 1
    if i == 1:
        from init import app
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mini", dest="if_mini", help="is mini?")
        parser.add_argument("-c", "--cef", action="store_true", dest="if_cef", help="if_cef")
        args = parser.parse_args()
        ifCef = args.if_cef  # 是否开启cef模式
        if_mini = args.if_mini
        app(ifCef, if_mini)
    else:
        sys.exit()
