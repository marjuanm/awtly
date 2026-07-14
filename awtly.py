# Awtly - php transpiller util
# Original file name: awtly.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import sys
import importlib

from core.translations import getTranslation
from core.commands import newProject, addPage, deleteProject, buildProject, help, version
   
# sys.argv[0] program name ("awtly.py")
# sys.argv[1] first parameter ("new/delete/build/help")
# sys.argv[2] second parameter (project name)

# Purpose: Main function
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 13/07/2026
# Last modified username: Juan Manuel Mar Hdz.
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
    
    if projname.strip().lower() == "website":
       
      if len(sys.argv) == 4:
        newProject(sys.argv[3], "website", "templates/websites/blank") #use blank template
      else:
        newProject(sys.argv[3], "website", sys.argv[4]) #use this template
    
    else:
        
      if len(sys.argv) == 3:
        newProject(sys.argv[2], "website", "templates/websites/blank") #use blank template
      else:
        newProject(sys.argv[2], "website", sys.argv[3]) #use this template
    
    #create a new project or another component
    
  elif cmd.lower() == "addpage":
      
    #add blank page to project
    
    if len(sys.argv) <= 3:
      print(getTranslation("INCOMPLETECOMMAND"))
    elif len(sys.argv) == 4:
      addPage(projname, sys.argv[3], "templates/websites/blank") #use blank template
    else:
      addPage(projname, sys.argv[3], sys.argv[4]) #use this template
    
    #add blank page to project
    
  elif cmd.lower() == "delete":
    deleteProject(projname)    
  elif cmd.lower() == "build":
    buildProject(projname)
  elif cmd.lower() == "help" or cmd.lower() == "/?" or cmd.lower() == "-h":
      
    if cmd.lower() == "/?":
      help("")
    else:
      help(projname.replace("'", ""))    
  
  else:
    print(getTranslation("UNKNOWNCOMMAND"))
  