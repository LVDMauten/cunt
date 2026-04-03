#!/usr/bin/env python
from setuptools import setup, find_packages
import sys
import os
try:
    import fastentrypoints  # noqa: F401
except ImportError:
    pass

try:
    import pkg_resources
except ImportError:
    pkg_resources = None

if pkg_resources is not None:
    try:
        if int(pkg_resources.get_distribution("pip").version.split('.')[0]) < 6:
            print('pip older than 6.0 not supported, please upgrade pip with:\n\n'
                  '    pip install -U pip')
            sys.exit(-1)
    except pkg_resources.DistributionNotFound:
        pass

if os.environ.get('CONVERT_README'):
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
else:
    long_description = ''

version = sys.version_info[:2]
if version < (2, 7):
    print('cunt requires Python version 2.7 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)
elif (3, 0) < version < (3, 5):
    print('cunt requires Python version 3.5 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

VERSION = '3.35'

install_requires = ['psutil', 'colorama', 'six']
extras_require = {':python_version<"3.4"': ['pathlib2'],
                  ':python_version<"3.3"': ['backports.shutil_get_terminal_size'],
                  ':python_version<="2.7"': ['decorator<5', 'pyte<0.8.1'],
                  ':python_version>"2.7"': ['decorator', 'pyte'],
                  ":sys_platform=='win32'": ['win_unicode_console']}

if sys.platform == "win32":
    scripts = ['scripts\\cunt.bat', 'scripts\\cunt.ps1']
    entry_points = {'console_scripts': [
                  'cunt = cunt.entrypoints.main:main',
                  'cunt_firstuse = cunt.entrypoints.not_configured:main']}
else:
    scripts = []
    entry_points = {'console_scripts': [
                  'cunt = cunt.entrypoints.main:main',
                  'cunt_firstuse = cunt.entrypoints.not_configured:main']}

setup(name='cunt',
      version=VERSION,
      description="Glorious app which corrects your previous console command by calling it a cunt",
      long_description=long_description,
      author='LVDMauten',
      author_email='lvdmauten@gmail.com',
      url='https://github.com/LVDMauten/cunt',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'tests.*', 'release']),
      include_package_data=True,
      zip_safe=False,
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
      install_requires=install_requires,
      extras_require=extras_require,
      scripts=scripts,
      entry_points=entry_points)
