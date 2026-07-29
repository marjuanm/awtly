# Awtly - php transpiller util
# Original file name: newwebsite.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import os
import shutil
import locale

from pathlib import Path
from common.functions import getPath
from core.translations import getTranslation

# Purpose: Create a new website
# Created date: 06/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 06/07/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to chatgpt
# Thanks to https://stackoverflow.com/questions/12683834/how-to-copy-directory-recursively-in-python-and-overwrite-all
def newWebsite(pnewpath, tnewpath, createproject):

  if pnewpath.exists():
    
    if pnewpath.is_dir():
        
      reply = input(getTranslation("CONFIRMOVERWRITEPROJECT")).strip().lower()
        
      if reply in ['s', 'y', 'j', 'o', 'e']:
        
        # delete project folder first
          
        try:  
          shutil.rmtree(pnewpath)
        except PermissionError:
              
          print("----------------------------------------")
          print(getTranslation("NOGRATSTOOVERWRITEORDELETEFOLDER"))
          createproject = False
            
      else:  
        createproject = False
          
    else:
        
      print(getTranslation("INVALIDPROJECTNAME"))
      createproject = False
        
  if createproject ==  True:
    
    try:
          
      pnewpath.mkdir(parents=True, exist_ok=True)
        
      #copy all files from template folder
        
      print("----------------------------------------")
      print(getTranslation("CREATINGPROJECTFILES"))
      shutil.copytree(tnewpath, pnewpath, dirs_exist_ok=True)
      print(getTranslation("DONE"))
        
    except PermissionError:
      
      print("----------------------------------------")
      print(getTranslation("NOGRATSTOOVERWRITEORDELETEFOLDER"))
