import docx
import os
from PyInstaller.utils.hooks import collect_all

block_cipher = None

# Collect all resources for docx (data, binaries, hidden imports)
docx_datas, docx_binaries, docx_hiddenimports = collect_all('docx')

a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=docx_binaries,
    datas=[
        ('src/app/assets', 'app/assets'),
        ('src/app/data', 'app/data'),
    ] + docx_datas,
    hiddenimports=['backports'] + docx_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='psy-r',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
