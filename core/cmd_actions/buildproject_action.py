# Awtly - php transpiller util
# Original file name: buildproject_action.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from pathlib import Path
from common.globals import projcfg
from core.translations import getTranslation
from common.functions import getPath, getConfig

# Purpose: Build a project
# Created date: 28/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 02/08/2026
# Last modified username: Juan Manuel Mar Hdz.
def buildProjectAction(projname):
    
  path = getPath()
  projname_clean = projname.strip()
  candidate = Path(projname_clean)
  
  # clear global configuration
  projcfg = {}
  
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
        
          # load configuration from project's configuration file
          success, cfg, errors = getConfig(projfile)
          
          if not success:
              
            for error in errors:
              print(error)
              
          else:
              
            projcfg = cfg # save configuration as global
            
            if projcfg["language"].strip() == "":
              projcfg["language"] = "php"
            
            if projcfg["language"].strip().lower() == "php":
              print("compilar a php")
            else:
              print(getTranslation("UNKNOWNLANGUAGE"))
            
        else:
          print(getTranslation("PROJECTFILENOTFOUND"))
          
      else:
        print(getTranslation("INVALIDPROJECTNAME"))
        
    else:
      print(getTranslation("PROJECTFOLDERNOTFOUND"))
