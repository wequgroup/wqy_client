#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Mon
LastEditors: Mon
Date: 2023-03-12 20:08:30
LastEditTime: 2023-03-15 22:40:34
Description: 数据库类
usage: 运行前，请确保本机已经搭建Python3开发环境，且已经安装 sqlalchemy 模块。
'''

import os
import sys
from shutil import copyfile
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import Config


class DB:
    '''数据库操作类'''

    session = None    # sqlalchemy用于操作数据库的管理器
    dbPath = ''    # 数据库路径

    def init(self):
        '''初始化数据库'''
        # 迁移数据库到本地电脑
        dbStorageDir = os.path.join(Config.storageDir, 'static', 'db')    # 本地电脑
        if not os.path.isdir(dbStorageDir):
            # 新建本地电脑文件夹
            os.makedirs(dbStorageDir)
        DB.dbPath = os.path.join(dbStorageDir, 'base.db')
        if not os.path.exists(DB.dbPath) or Config.ifCoverDB:
            # 数据库不存在时，新建数据库；或者配置信息为强制覆盖时，覆盖数据库
            dbStaticPath = os.path.join(Config.staticDir, 'db', 'base.db')    # 程序包
            copyfile(dbStaticPath, DB.dbPath)

        # 数据库连接
        self.connect()

        # 迁移数据库结构
        self.migration()

    def connect(self):
        '''数据库连接'''
        engine = create_engine(f'sqlite:///{DB.dbPath}?check_same_thread=False', echo=Config.devEnv)
        DB.session = sessionmaker(bind=engine)

    def close(self):
        '''关闭数据库连接'''
        if DB.session is not None:
            DB.session.close()

    def migration(self):
        '''迁移数据库结构'''
        currentVersion = ''    # 当前最新数据库版本
        currentVersionPath = os.path.join(Config.staticDir, 'db', 'version')    # 存放当前最新数据库版本号的路径
        with open(currentVersionPath, 'r') as f1:
            list1 = f1.readlines()
        for i in range(len(list1)-1, -1, -1):
            row = list1[i].rstrip('\n')
            if row == '':
                continue
            currentVersion = row.split(' ')[0]
            break

        dbSession = DB.session()
        with dbSession.begin():
            stmt = text('SELECT version_num FROM alembic_version')
            res = dbSession.execute(stmt)
            oldVersion = res.all()[0][0]    # 正在使用的数据库版本

            # 更新数据库结构
            version2migrationDict = dict()
            if currentVersion != oldVersion:
                # 获取历史结构
                migrationPath = os.path.join(Config.staticDir, 'db', 'migration.sql')
                with open(migrationPath, 'r') as f1:
                    migrationList = f1.readlines()
                version = ''
                versionUpdate = ''    # 要更新的数据库版本
                migration = ''
                for i in range(0, len(migrationList)):
                    row = migrationList[i].rstrip('\n')
                    if row.find('Running upgrade') > -1:
                        version2migrationDict[version] = migration
                        versionLast = row.split(' -> ')[-1]
                        if version == oldVersion:
                            versionUpdate = versionLast
                        version = versionLast
                        migration = ''
                    else:
                        migration += row
                version2migrationDict[version] = migration

                # 更新数据库结构
                if versionUpdate != '':
                    migrationList = version2migrationDict[versionUpdate].replace('\n', '').split(';')
                    for migration in migrationList:
                        migration = migration.replace('\n', '')
                        if migration != '':
                            stmt = text(migration)
                            dbSession.execute(stmt)
        dbSession.close()
