# -*- mode: python ; coding: utf-8 -*-

import os

import PyInstaller.config

buildPath = 'build'
PyInstaller.config.CONF['distpath'] = buildPath

cachePath = os.path.join(buildPath, 'cache')
if not os.path.exists(cachePath):
    os.makedirs(cachePath)
PyInstaller.config.CONF['workpath'] = cachePath

icoPath = os.path.join('..', 'icon', 'logo.icns')

appName = 'WeDuck'

version = '0.0.1'

block_cipher = pyi_crypto.PyiBlockCipher(key='weduck889378294')

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
        codesign_identity=None,
        entitlements_file=None)
coll = COLLECT(exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=False,
                upx_exclude=[],
                name=appName)

app = coll
