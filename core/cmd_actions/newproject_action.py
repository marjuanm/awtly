# Awtly - php transpiller util
# Original file name: newproject_action.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from pathlib import Path
from common.functions import getPath
from core.translations import getTranslation
from core.cmd_templates.newwebsite import newWebsite

# Purpose: Create a new project
# Created date: 07/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 02/08/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to chatgpt
def newProjectAction(projname, projtype, template):
    
  if template.strip() == "":
    template = "templates/php/websites/blank"
    
  if projtype.strip() == "":
    projtype = "website"
    
  path = getPath()
  cancontinue = True
  createproject = True  
  projname_clean = projname.strip()
  projectcandidate = Path(projname_clean)
  template_clean = template.strip()
  templatecandidate = Path(template_clean)
  
  # use the correct path
  pnewpath = projectcandidate if projectcandidate.is_absolute() else path / projectcandidate  
  tnewpath = templatecandidate if templatecandidate.is_absolute() else path / templatecandidate  
  
  if pnewpath.suffix.strip() != "" or tnewpath.suffix.strip() != "":
        
    createproject = False
    cancontinue = False
    
    if pnewpath.suffix.strip() != "":
      
      print("----------------------------------------")
      print(getTranslation("INVALIDPROJECTNAME"))
    
    if tnewpath.suffix.strip() != "":
      
      print("----------------------------------------")
      print(getTranslation("INVALIDTEMPLATENAME"))
      
  else:
      
    # check if project folder exists
    if pnewpath.exists():
        
      if not pnewpath.is_dir():
      
        createproject = False
        cancontinue = False
        print("----------------------------------------")
        print(getTranslation("INVALIDPROJECTNAME"))
    
    # check if template folder exists
    if not tnewpath.exists():
      
      createproject = False
      cancontinue = False
      print("----------------------------------------")
      print(getTranslation("TEMPLATENOTFOUND"))
    
    else:
        
      if not tnewpath.is_dir():
      
        createproject = False
        cancontinue = False
        print("----------------------------------------")
        print(getTranslation("INVALIDTEMPLATENAME"))
      
  # copy structure from template by object type
  if cancontinue == True:
    
    if projtype.strip().lower() == "website":
      newWebsite(pnewpath, tnewpath, createproject)
    else:
      newWebsite(pnewpath, tnewpath, createproject)
