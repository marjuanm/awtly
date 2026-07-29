# Awtly - php transpiller util
# Original file name: buildproject_action.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import os
import shutil
import locale

from pathlib import Path
from common.functions import getPath
from core.translations import getTranslation
from core.transpiler.configuration import loadprojConfiguration

# Purpose: Build a project
# Created date: 28/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 28/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def buildProjectAction(projname):
    
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
        
        projfile = newpath / "project.cfg"
        
        if projfile.exists():
            
          print("----------------------------------------")
          
          if loadprojConfiguration(projfile) == True: # extract index, assets and templates vars from project and load in global module
            print(getTranslation("DONE"))  
              
        else:
          print(getTranslation("PROJECTFILENOTFOUND"))
          
      else:
        print(getTranslation("INVALIDPROJECTNAME"))
        
    else:
      print(getTranslation("PROJECTFOLDERNOTFOUND"))
