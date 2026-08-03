# Awtly - php transpiller util
# Original file name: addpage_action.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import os
import shutil

from pathlib import Path
from common.functions import getPath
from core.translations import getTranslation

# Purpose: Add a new page to project structure
# Created date: 29/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 13/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def addPageAction(projname, page, template):
    
  if template.strip() == "":
    template = "blank"
    
  path = getPath()
  cancontinue = True
  updateproject = True  
  projname_clean = projname.strip()
  projectcandidate = Path(projname_clean)
  template_clean = template.strip()
  templatecandidate = Path(template_clean)
  
  # use the correct path
  pnewpath = projectcandidate if projectcandidate.is_absolute() else path / projectcandidate  
  tnewpath = templatecandidate if templatecandidate.is_absolute() else path / templatecandidate  
  
  if pnewpath.suffix.strip() != "" or tnewpath.suffix.strip() != "":
        
    updateproject = False
    cancontinue = False
    
    if pnewpath.suffix.strip() != "":
      
      print("----------------------------------------")
      print(getTranslation("INVALIDPROJECTNAME"))
    
    if tnewpath.suffix.strip() != "":
      
      print("----------------------------------------")
      print(getTranslation("INVALIDTEMPLATENAME"))
      
  else:
      
    # check if project folder exists
    if not pnewpath.exists():

      cancontinue = False
      updateproject = False
      print("----------------------------------------")
      print(getTranslation("FOLDERPROJECTNAMENOTFOUND"))
  
    else:
        
      if not pnewpath.is_dir():
      
        updateproject = False
        cancontinue = False
        print("----------------------------------------")
        print(getTranslation("INVALIDPROJECTNAME"))
    
    # check if template folder exists
    if not tnewpath.exists():
    
      updateproject = False
      cancontinue = False
      print("----------------------------------------")
      print(getTranslation("TEMPLATENOTFOUND"))
    
    else:
        
      if not tnewpath.is_dir():
      
        updateproject = False
        cancontinue = False
        print("----------------------------------------")
        print(getTranslation("INVALIDTEMPLATENAME"))
  
  if cancontinue == True:
      
    # check if new page is not blank and not contain subfixes
    if page.strip() == "":
      
      updateproject = False
      cancontinue = False
      print("----------------------------------------")
      print(getTranslation("INVALIDPAGENAME"))
    
    else:
        
      filename, filext = os.path.splitext(page.strip())
      
      if filext != "":
          
        updateproject = False
        cancontinue = False
        print("----------------------------------------")
        print(getTranslation("INVALIDPAGENAME"))
    
  # copy structure from template by object type
  if cancontinue == True:
  
    file = page.strip()
    
    sawsc = tnewpath / "logic" / f"index.awsc"
    sawcp = tnewpath / "pages" / f"index.awcp"
    sawui = tnewpath / "pages" / f"index.awui"
    
    dawsc = pnewpath / "logic" / f"{file}.awsc"
    dawcp = pnewpath / "pages" / f"{file}.awcp"
    dawui = pnewpath / "pages" / f"{file}.awui"
    
    if dawsc.exists() or dawcp.exists() or dawui.exists():
      reply = input(getTranslation("CONFIRMOVERWRITEPAGE")).strip().lower()
    else:
      reply = "y"
          
    if reply in ['s', 'y', 'j', 'o', 'e']:
        
      # delete new page files first
          
      try:  
              
        if dawsc.exists():
          dawsc.unlink()
              
        if dawcp.exists():
          dawcp.unlink()
              
        if dawui.exists():
          dawui.unlink()
          
      except PermissionError:
              
        print("----------------------------------------")
        print(getTranslation("NOGRATSTOOVERWRITEORDELETEFOLDER"))
        updateproject = False
            
    else:  
      updateproject = False
        
  if updateproject ==  True:
    
    try:
          
      #add page basic files to project
        
      print("----------------------------------------")
      print(getTranslation("CREATINGPAGEFILES"))

      dawsc.parent.mkdir(parents=True, exist_ok=True)
      shutil.copy(sawsc, dawsc)
      
      dawcp.parent.mkdir(parents=True, exist_ok=True)
      shutil.copy(sawcp, dawcp)
      
      dawui.parent.mkdir(parents=True, exist_ok=True)
      shutil.copy(sawui, dawui)
      
      print(getTranslation("DONE"))
        
    except PermissionError:

      print("----------------------------------------")
      print(getTranslation("NOGRATSTOOVERWRITEORDELETEFOLDER"))
