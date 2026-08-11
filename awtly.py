# Awtly - php transpiller util
# Original file name: awtly.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import sys
import importlib
import traceback

from pathlib import Path
from core.translations import getTranslation
from common.errorstracking import errortolog
from common.functions import getPath, getConfig
from core.cmd_actions.help_action import helpAction
from common.globals import awtlycfg, debugmode, debugfile
from core.commands import newProject, addPage, deleteProject, buildProject, help, version
   
# sys.argv[0] program name ("awtly.py")
# sys.argv[1] first parameter ("new/delete/build/help")
# sys.argv[2] second parameter (project name)

# Purpose: Main function
# Created date: 02/08/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 10/08/2026
# Last modified username: Juan Manuel Mar Hdz.
def main():
  #x = 1 / 0 #test debug system
  if len(sys.argv) <= 2:
    
    if len(sys.argv) <= 1:
      print(getTranslation("INVALIDPARAMSNUMBER"))
    
    else:
      
      cmd = sys.argv[1]
      
      if cmd.lower() == "help" or cmd.lower() == "/?" or cmd.lower() == "-h":
        help("")  
      elif cmd.lower() == "-v":
        version()        
      else:
        
        if cmd.lower() == "new" or cmd.lower() == "addpage" or cmd.lower() == "delete" or cmd.lower() == "build":
          msg = getTranslation("INCOMPLETECOMMAND")
        else:
          msg = getTranslation("UNKNOWNCOMMAND")
      
        print(msg)
  
  else:
    
    cmd = sys.argv[1]
    projname = sys.argv[2]

    if cmd.lower() == "new":
      
      #create a new project or another component
    
      if projname.strip().lower() == "/?":
        helpAction("new")
      elif projname.strip().lower() == "website":
       
        if len(sys.argv) == 4:
          newProject(sys.argv[3], "website", "templates/php/websites/blank") #use blank template
        else:
          newProject(sys.argv[3], "website", sys.argv[4]) #use this template
    
      else:
        
        if len(sys.argv) == 3:
          newProject(sys.argv[2], "website", "templates/php/websites/blank") #use blank template
        else:
          newProject(sys.argv[2], "website", sys.argv[3]) #use this template
    
      #create a new project or another component
    
    elif cmd.lower() == "addpage":
      
      #add blank page to project
    
      if projname.strip().lower() == "/?":
        helpAction("addpage")
      elif len(sys.argv) <= 3:
        print(getTranslation("INCOMPLETECOMMAND"))
      elif len(sys.argv) == 4:
        addPage(projname, sys.argv[3], "templates/php/websites/blank") #use blank template
      else:
        addPage(projname, sys.argv[3], sys.argv[4]) #use this template
    
      #add blank page to project
    
    elif cmd.lower() == "delete":
    
      if projname.strip().lower() == "/?":
        helpAction("delete")
      else:
        deleteProject(projname)    
  
    elif cmd.lower() == "build":
    
      if projname.strip().lower() == "/?":
        helpAction("build")
      elif len(sys.argv) <= 2:
        print(getTranslation("INCOMPLETECOMMAND"))  
      else:
          
        if len(sys.argv) == 3:
          buildProject(projname, "php")
        else:
            
          # clear target parameter
          
          target = sys.argv[3].strip()
          target = target.replace("'", "")
          target = target.replace('\"', "")
          
          # get target language
          
          if "target=" in target.lower():
              
            key, value = target.split("=", 1)
            key = key.strip()
            value = value.strip()
            
            if value.strip() == "":
              value = "php"
            
            buildProject(projname, value.strip())

          else:
            buildProject(projname, target.strip())
  
    elif cmd.lower() == "help" or cmd.lower() == "/?" or cmd.lower() == "-h":
      
      if cmd.lower() == "/?":
        help("")
      else:
        help(projname.replace("'", ""))    
  
    else:
      print(getTranslation("UNKNOWNCOMMAND"))

# Purpose: Start program
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 02/08/2026
# Last modified username: Juan Manuel Mar Hdz.
conffile = Path(getPath()) / "configuration.cfg"

# load Awtly's configuration from project's configuration file
if conffile.exists():

  success, cfg, errors = getConfig(conffile)
  
  if success:
      
    awtlycfg = cfg # save configuration as global
            
    if awtlycfg["debugmode"].strip().lower() == "true":
      debugmode = True
      
# enable debug mode
if debugmode ==  True:
    
  if awtlycfg["debugfile"].strip().lower() == "":
    debugfile = "debug.log"
  else:
    debugfile = awtlycfg["debugfile"].strip()

# start program
if debugmode == True:
  
  try:
    main()
  except Exception:

    errortolog(traceback.format_exc())
    print(getTranslation("ALREADYERRORSFOUND"))
    
else:
  main()
