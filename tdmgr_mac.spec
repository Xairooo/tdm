# -*- mode: python -*-

from get_version import get_version

block_cipher = None

a = Analysis(['tdmgr.py'],
             binaries=None,
             datas=[('GUI', 'GUI'), ('Util', 'Util')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=f'tdmgr_{get_version()}',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='tdmgr.icns')
app = BUNDLE(exe,
             name=f'tdmgr_{get_version()}',
             icon='tdmgr.icns',
             bundle_identifier='com.tasmota.tdmgr')
