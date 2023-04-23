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

from init import app

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cef", action="store_true", dest="if_cef", help="if_cef")
    args = parser.parse_args()
    ifCef = args.if_cef  # 是否开启cef模式
    app(ifCef)
