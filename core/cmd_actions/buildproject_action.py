# Awtly - php transpiller util
# Original file name: buildproject_action.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.
import sys
import traceback

from pathlib import Path
from common.globals import projcfg
from core.translations import getTranslation
from common.functions import getPath, getConfig

# Purpose: Build a project
# Created date: 28/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 10/08/2026
# Last modified username: Juan Manuel Mar Hdz.
def buildProjectAction(projname, target):
    
  path = getPath()
  projname_clean = projname.strip()
  candidate = Path(projname_clean)
  
  if target.strip() == "":
    target = "php"
    
  if target.lower() != "php" and target.lower() != "elixir":
    print(getTranslation("UNKNOWNLANGUAGE"))
  else:
      
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
            
              if target.strip().lower() == "php":
                print("compilar a php")
              elif target.strip().lower() == "elixir":
                print("compilar a elixir")
              else:
                print(getTranslation("UNKNOWNLANGUAGE"))
            
          else:
            print(getTranslation("PROJECTFILENOTFOUND"))
          
        else:
          print(getTranslation("INVALIDPROJECTNAME"))
        
      else:
        print(getTranslation("PROJECTFOLDERNOTFOUND"))
