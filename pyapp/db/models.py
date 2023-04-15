#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FilePath: /vue-pywebview-pyinstaller/pyapp/db/models.py
Author: Mon
LastEditors: Mon
Date: 2023-03-12 20:29:49
LastEditTime: 2023-03-14 23:35:35
Description: 创建数据表
usage: 更新数据表格式后，请按如下操作迁移数据库：
        m=备注更改内容 npm run alembic

        注意：上述命令仅能迁移打包程序自带数据库(Config.staticDir)。在程序运行初始化时，会自动检测并迁移本地电脑中保存的数据库(Config.storageDir)
'''

import json

from sqlalchemy import DateTime, Numeric, Column, Integer, String, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """基类"""
    __abstract__ = True

    def _gen_tuple(self):
        # 处理 日期 等无法正常序列化的对象
        def convert_datetime(value):
            if value:
                return value.strftime("%Y-%m-%d %H:%M:%S")
            else:
                return ""

        for col in self.__table__.columns:
            try:
                if isinstance(col.type, DateTime):
                    value = convert_datetime(getattr(self, col.name))
                elif isinstance(col.type, Numeric):
                    value = float(getattr(self, col.name))
                else:
                    value = getattr(self, col.name)
                yield (col.name, value)
            except Exception as e:
                print(e)
                pass

    def toDict(self):
        # 转化为 字典
        return dict(self._gen_tuple())

    def toJson(self):
        # 序列化为 JSON
        return json.dumps(self.toDict())


class StorageVar(BaseModel):
    """储存变量"""
    __tablename__ = "storage_var"
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(), doc='键', nullable=False, index=True)
    value = Column(String(), doc='值', server_default='', nullable=False)
    remark = Column(String(), doc='备注', server_default='', nullable=False)
    created_at = Column(DateTime(), doc='创建时间', comment='创建时间', server_default=func.now())
    updated_at = Column(DateTime(), doc='更新时间', comment='更新时间', server_default=func.now(), onupdate=func.now())

    def __str__(self):
        return self.key + ' => ' + self.value


class Device(BaseModel):
    """设备表"""
    __tablename__ = "device"
    device_id = Column(String(), primary_key=True)
    device_password = Column(String(), doc='值', server_default='', nullable=False)
    device_name = Column(String(), doc='值', server_default='', nullable=False)
    auto_online = Column(String(), doc='值', server_default='', nullable=False)
    def __str__(self):
        return self.device_id + ' => ' + self.device_password


class Record(BaseModel):
    """脚本记录表"""
    __tablename__ = "record"
    record_id = Column(String(), primary_key=True)
    record_content = Column(String(), doc='值', server_default='', nullable=False)
    record_name = Column(String(), doc='值', server_default='', nullable=False)

    def __str__(self):
        return self.record_id + ' => ' + self.record_content
