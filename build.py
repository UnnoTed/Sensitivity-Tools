from py2exe.build_exe import py2exe
from distutils.core import setup

setup(
  name        = 'Sensitivity Tools',
  version     = '0.2',
  author      = 'sk1LLb0X',
  windows     = ['main.pyw'],
  options     = {'py2exe': {'bundle_files': 1, 'compressed': True, 'includes':['sip']}},
  zipfile     = None
)