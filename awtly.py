# Awtly - php transpiller util
# Original file name: awtly.py
# Copyright (C) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import sys

from messages import MSG
from translations import getTranslation
from commands import newProject, deleteProject, buildProject
   
# sys.argv[0] program name ("awtly.py")
# sys.argv[1] first parameter ("new/delete/build")
# sys.argv[2] second parameter (project name)

if len(sys.argv) <= 2:

  msg = getTranslation(MSG.INVALIDPARAMSNUMBER)
  print(msg)
  
else:
    
  cmd = sys.argv[1]
  projname = sys.argv[2]
  
  if cmd.lower() == "new":
    newProject(projname)
  elif cmd.lower() == "delete":
    deleteProject(projname)    
  elif cmd.lower() == "build":
    buildProject(projname)    
  else:
    
    msg = getTranslation(MSG.INVALIDPARAMETER)
    print(msg)
  