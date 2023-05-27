# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['AccessibleGamingKeypad_0.2.7.py'],
             pathex=['D:\\Python\\AGK\\AccessibleGamingKeypad-D'],
             binaries=[],
             datas=[],  # config.json has been removed here
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='AccessibleGamingKeypad_0.2.7',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='D:\\Python\\AGK\\AccessibleGamingKeypad-D\\icon.ico' ) 
