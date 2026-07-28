# Awtly - php transpiller util
# Original file name: configuration.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from pathlib import Path
from gmodule import getConfig
from core.translations import getTranslation
from core.transpiler.gproject import index, assets

# Purpose: Load configuration from project file
# Created date: 28/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 28/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def loadprojConfiguration(projfile):
    
  success, cfg, errors = getConfig(projfile)
  
  if not success:

    for error in errors:
      print(error)

    return False
    
  else:
      
    index = cfg["index"]
    assets = cfg["assets"]

    return True;
