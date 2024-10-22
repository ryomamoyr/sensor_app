# run_main.spec

# -*- mode: python ; coding: utf-8 -*-

import sys
import os
import site

block_cipher = None

# プロジェクトのルートディレクトリを取得
project_root = os.getcwd()

# site-packagesのパスを取得
site_packages = site.getsitepackages()[0]

a = Analysis(
    ['run_main.py'],
    pathex=[project_root],
    binaries=[],
    datas=[
        # Streamlitの静的ファイルとランタイムファイルを含める
        (os.path.join(site_packages, "streamlit", "static"), "streamlit/static"),
        (os.path.join(site_packages, "streamlit", "runtime"), "streamlit/runtime"),
        # アプリケーションのソースコードを含める
        (os.path.join(project_root, "src"), "src"),
    ],
    hiddenimports=[
        'dataloader.toilet',
        'analyser.toilet',
        'visualizer.toilet',
        # 必要に応じて他のモジュールを追加
    ],
    hookspath=['./hooks'],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # GUIアプリの場合はFalse
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='app',
)
