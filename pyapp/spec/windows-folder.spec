
# -*- mode: python ; coding: utf-8 -*-

import os

import PyInstaller.config

# 存放最终打包成app的相对路径
buildPath = 'build'
PyInstaller.config.CONF['distpath'] = buildPath

# 存放打包成app的中间文件的相对路径
cachePath = os.path.join(buildPath, 'cache')
if not os.path.exists(cachePath):
    os.makedirs(cachePath)
PyInstaller.config.CONF['workpath'] = cachePath

# icon相对路径
icoPath = os.path.join('..', 'icon', 'logo.ico')

# 项目名称
appName = '微趣鸭  v0.0.1'

# 版本号
version = '0.0.1'

# 对Python字节码加密
block_cipher = pyi_crypto.PyiBlockCipher(key='cck887356789123456')


a = Analysis(['../../main.py'],
            pathex=[],
            binaries=[],
            datas=[('../../gui/dist', 'web'), ('../../static', 'static')],
            hiddenimports=[],
            hookspath=[],
            hooksconfig={},
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)


exe = EXE(pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name=appName,
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=icoPath)
coll = COLLECT(exe,
            a.binaries,
            a.zipfiles,
            a.datas,
            strip=False,
            upx=True,
            upx_exclude=[],
            name=appName)

