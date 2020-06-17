# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['GUI_Kim.py'],
             pathex=['C:\\Users\\이우창\\Documents\\PyCharm\\sea-your-info-master\\client'],
             binaries=[],
             datas=[("./imagefile", "./imagefile"), ("./fontfile", "./fontfile")],
             hiddenimports=["Create_User", "Find_User", "Getalluser", "GUI_get_posts", "Login", "Post_ch", "Update_User"],
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
          name='Seayourinfo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='icon.ico'
           )
