import os
from py2exe.build_exe import py2exe
from distutils.core import setup

setup(
  name        = 'Sensitivity Tools',
  version     = '0.4',
  author      = 'sk1LLb0X',
  windows     = [{ 
    'script' : 'main.pyw',
    'icon_resources' : [(1, 'mouse.ico')]
  }],
  options     = {
    'py2exe': {
      'bundle_files': 3, 
      'compressed': True,
      'includes': [
        'sip', 
        'PyQt4.QtCore', 
        'PyQt4.QtGui', 
        'PyQt4.QtNetwork'
      ]
    }
  },
  zipfile     = None,
  data_files  = ['history.html', 'history.css']
)

os.remove('dist/SensitivityTools.exe')
os.rename('dist/main.exe', 'dist/SensitivityTools.exe')