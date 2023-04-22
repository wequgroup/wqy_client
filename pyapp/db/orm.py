#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Mon
LastEditors: Mon
Date: 2023-03-12 20:08:30
LastEditTime: 2023-03-15 22:29:38
Description: 操作数据库类
usage:
    from pyapp.db.orm import ORM

    orm = ORM()    # 操作数据库类
    author = self.orm.getStorageVar('author')    # 获取储存变量
    print('author', author)
'''

from pyapp.db.models import StorageVar, Device, Record
from pyapp.db.db import DB
from sqlalchemy import select, update, insert, delete


class ORM:
    '''操作数据库类'''

    def getStorageVar(self, key):
        '''获取储存变量'''
        resVal = ''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = select(StorageVar.value).where(StorageVar.key == key)
            result = dbSession.execute(stmt)
            result = result.one_or_none()
            if result is None:
                # 新建
                stmt = insert(StorageVar).values(key=key)
                dbSession.execute(stmt)
            else:
                resVal = result[0]
        dbSession.close()
        return resVal

    def setStorageVar(self, key, val):
        '''更新储存变量'''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = update(StorageVar).where(StorageVar.key == key).values(value=val)
            dbSession.execute(stmt)
        dbSession.close()

    def update_device(self, device_name, device_id, device_password, auto_inline):
        db_session = DB.session()
        with db_session.begin():
            stmt = update(Device).values(device_id=device_id,
                                         device_password=device_password,
                                         auto_online=auto_inline,
                                         device_name=device_name)
            db_session.execute(stmt)
        db_session.close()

    def get_record(self):
        db_session = DB.session()
        record_list = []
        with db_session.begin():
            stmt = select(Record.record_id, Record.record_name)
            result = db_session.execute(stmt)
            resp = result.all()
            if resp is None:
                return None
            for r in resp:
                data = {"record_id": r[0], "record_name": r[1]}
                record_list.append(data)
        db_session.close()
        return record_list

    def get_record_one(self, id):
        db_session = DB.session()
        with db_session.begin():
            stmt = select(Record.record_content).where(Record.record_id == id)
            result = db_session.execute(stmt)
            result = result.one_or_none()
        db_session.close()
        return result[0]

    def delete_record(self, id):
        db_session = DB.session()
        with db_session.begin():
            stmt = delete(Record).where(Record.record_id == id)
            db_session.execute(stmt)
        db_session.close()

    def add_record(self, id, name, content):
        db_session = DB.session()
        with db_session.begin():
            stmt = insert(Record).values(record_id=id, record_name=name, record_content=content)
            db_session.execute(stmt)
        db_session.close()

    def get_device(self):
        """获取设备"""
        db_session = DB.session()
        with db_session.begin():
            stmt = select(Device.device_id, Device.device_password, Device.device_name, Device.auto_online)
            result = db_session.execute(stmt)
            resp = result.one_or_none()
            if resp is None:
                return None
            data = {"device_id": resp[0], "device_password": resp[1], "device_name": resp[2], "auto_online": resp[3]}
        db_session.close()
        return data

    def add_device(self, device_name, device_id, device_password, auto_inline):
        db_session = DB.session()
        with db_session.begin():
            stmt = insert(Device).values(device_id=device_id, device_password=device_password,
                                         auto_online=auto_inline, device_name=device_name)
            db_session.execute(stmt)
        db_session.close()
