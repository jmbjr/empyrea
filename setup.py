from distutils.core import setup
import pygame
import py2exe
import sys
import os
import glob, shutil
import libtcodpy

REMOVE_BUILD_ON_EXIT = True
PYGAMEDIR = os.path.split(pygame.base.__file__)[0]
SDL_DLLS = glob.glob(os.path.join(PYGAMEDIR,'*.dll'))
VERSION = '0.2'
AUTHOR_NAME = 'David Hagar'
AUTHOR_EMAIL = 'dm.hagar@gmail.com'
AUTHOR_URL = "http://cultrl.wordpress.com"
PRODUCT_NAME = "Cult"
SCRIPT_MAIN = 'C:\\Cult\\cult.py' 
VERSIONSTRING = PRODUCT_NAME + " ALPHA " + VERSION + ' by D.M. Hagar'
ICONFILE = 'C:\\Cult\\image\\ico\\cult.ico'


MODULE_EXCLUDES =[
'email',
'AppKit',
'Foundation',
'bdb',
'difflib',
'tcl',
'Tkinter',
'Tkconstants',
'curses',
'distutils',
'setuptools',
'urllib',
'urllib2',
'urlparse',
'BaseHTTPServer',
'_LWPCookieJar',
'_MozillaCookieJar',
'ftplib',
'gopherlib',
'_ssl',
'htmllib',
'httplib',
'mimetools',
'mimetypes',
'rfc822',
'tty',
'webbrowser',
'socket',
'hashlib',
'base64',
'compiler',
'pydoc']

INCLUDE_STUFF = ['numpy']

setup(windows=[
             {'script': SCRIPT_MAIN,
               'other_resources': [(u"VERSIONTAG",1,VERSIONSTRING)],
               'icon_resources': [(1,ICONFILE)]}],
         options = {"py2exe": {
                             "includes": INCLUDE_STUFF,
                             "optimize": 0,
                             "compressed": 1,
                             "ascii": 1,
                             "bundle_files": 3,
                             "ignores": ['tcl','AppKit','Numeric','Foundation'],
                             "excludes": MODULE_EXCLUDES} },
          name = PRODUCT_NAME,
          version = VERSION,
          zipfile = None,
          author = AUTHOR_NAME,
          author_email = AUTHOR_EMAIL,
          url = AUTHOR_URL)

extra_files = [("image",glob.glob(os.path.join('gfx','*.bmp'))), \
               ("image",glob.glob(os.path.join('txt','*.txt'))), \
               ("image",glob.glob(os.path.join('ico','*.ico'))), \
               ("image",glob.glob(os.path.join('cursor','*.ani'))), \
               ("image",glob.glob(os.path.join('cursor','*.cur'))), \
               ("data",glob.glob(os.path.join('name','*.txt'))), \
               ("data",glob.glob(os.path.join('build','*.txt'))), \
               ("data",glob.glob(os.path.join('struct','*.txt'))), \
               ("fonts",glob.glob(os.path.join('fonts','*.png'))), \
               ("sound",glob.glob(os.path.join('ogg','*.ogg'))), \
               ("music",glob.glob(os.path.join('wav','*.wav'))), \
               ("music",glob.glob(os.path.join('ogg','*.ogg')))]
 
if os.path.exists('dist/tcl'): shutil.rmtree('dist/tcl') 
 
# Remove the build tree
if REMOVE_BUILD_ON_EXIT:
     shutil.rmtree('build/')
 
if os.path.exists('dist/tcl84.dll'): os.unlink('dist/tcl84.dll')
if os.path.exists('dist/tk84.dll'): os.unlink('dist/tk84.dll')
 
for f in SDL_DLLS:
    fname = os.path.basename(f)
    try:
        shutil.copyfile(f,os.path.join('dist',fname))
    except: pass
