# Awtly - php transpiller util
# Original file name: deleteproject_action.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import shutil

from pathlib import Path
from common.functions import getPath
from core.translations import getTranslation

# Purpose: Delete a project
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 30/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def deleteProjectAction(projname):
    
  path = getPath()
  projname_clean = projname.strip()
  candidate = Path(projname_clean)
  
  # use the correct path
  newpath = candidate if candidate.is_absolute() else path / candidate  
  
  if newpath.suffix.strip() != "":
    print(getTranslation("INVALIDPROJECTNAME"))      
  else:
        
    if newpath.exists():
    
      if newpath.is_dir():
        
        reply = input(getTranslation("CONFIRMDELETEPROJECT")).strip().lower()
        
        if reply in ['s', 'y', 'j', 'o', 'e']:
        
          try:  
        
            # delete project folder
            
            shutil.rmtree(newpath)
            print(getTranslation("DONE"))
            
          except PermissionError:
              
            print("----------------------------------------")
            print(getTranslation("NOGRATSTODELETEFOLDER"))
          
      else:
        print(getTranslation("INVALIDPROJECTNAME"))
        
    else:
      print(getTranslation("PROJECTFOLDERNOTFOUND"))
