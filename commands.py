# Awtly - php transpiller util
# Original file name: commands.py
# Copyright (C) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import os
import shutil
import locale

from pathlib import Path
from messages import MSG
from gmodule import getPath
from translations import getTranslation
from structures import NEWPROJECT
from constants import PROJECT_NAME, PROJECT_SHORT_NAME, PROJECT_VERSION, PROJECT_YEAR, TEAM_NAME

# Purpose: Create a new project
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 24/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def newProject(projname):
    
  path = getPath()
  createproject = True  
  projname_clean = projname.strip()
  
  # use the correct path
  if "\\" in projname_clean or "/" in projname_clean:
    newpath = Path(projname_clean)
  else:  
    newpath = Path(path.strip() + "/" + projname_clean.strip())
    
  if newpath.suffix.strip() != "":
        
    createproject = False
    print(getTranslation(MSG.INVALIDPROJECTNAME))
        
  else:
        
    if newpath.exists():
    
      if newpath.is_dir():
        
        reply = input(getTranslation(MSG.CONFIRMOVERWRITEPROJECT)).strip().lower()
        
        if reply in ['s', 'y']:
        
          # delete project folder first
          
          try:  
            shutil.rmtree(newpath)
          except PermissionError:
              
            print("----------------------------------------")
            print(getTranslation(MSG.NOGRATSTOOVERWRITEORDELETEFOLDER))
            createproject = False
            
        else:  
          createproject = False
          
      else:
        
        print(getTranslation(MSG.INVALIDPROJECTNAME))
        createproject = False
        
  if createproject ==  True:
    
    try:
          
      newpath.mkdir(parents=True, exist_ok=True)
        
      #create basic files to current project
        
      print("----------------------------------------")
      print(getTranslation(MSG.CREATINGPROJECTFILES))

      folder = newpath / "templates" #User templates folder
      folder.mkdir(parents=True, exist_ok=True)
        
      folder = newpath / "assets/css" #Assets css folder
      folder.mkdir(parents=True, exist_ok=True)
        
      folder = newpath / "assets/js" #Assets javascripts folder
      folder.mkdir(parents=True, exist_ok=True)
        
      folder = newpath / "assets/images" #Assets images folder
      folder.mkdir(parents=True, exist_ok=True)
        
      file = newpath / "project.cfg" #Main project
      file.write_text(NEWPROJECT.PROJECT, encoding="utf-8")
        
      file = newpath / "pages/index.awui" #Awtly user interfaz
      file.parent.mkdir(parents=True, exist_ok=True)
      file.write_text(NEWPROJECT.DOCUMENT, encoding="utf-8")
        
      file = newpath / "pages/index.awcp" #Awtly control properties
      file.parent.mkdir(parents=True, exist_ok=True)
      file.write_text("/* TO DO: Add control properties here */\n\n", encoding="utf-8")
        
      file = newpath / "logic/index.awsc" #Awtly source code
      file.parent.mkdir(parents=True, exist_ok=True)
      file.write_text("/* TO DO: Add logic and events here */\n\n", encoding="utf-8")
        
      file = newpath / "config/routes.awrt" #Awtly routes
      file.parent.mkdir(parents=True, exist_ok=True)
      file.write_text("/* TO DO: Add pages routes and redirections here */\n\n", encoding="utf-8")
        
      file = newpath / "config/db.cfg" #Database configuration
      file.parent.mkdir(parents=True, exist_ok=True)
      file.write_text(NEWPROJECT.DB, encoding="utf-8")
        
      file = newpath / "config/cache.cfg" #Cache configuration
      file.parent.mkdir(parents=True, exist_ok=True)
      file.write_text(NEWPROJECT.CACHE, encoding="utf-8")
        
      file = newpath / "assets/css/styles.css" #Project styles
      file.write_text(NEWPROJECT.STYLES, encoding="utf-8")
        
      print(getTranslation(MSG.DONE))
        
    except PermissionError:
      
      print("----------------------------------------")
      print(getTranslation(MSG.NOGRATSTOOVERWRITEORDELETEFOLDER))
      
# Purpose: Add a new page to project structure
# Created date: 29/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 29/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def addPage(projname, page):
    
  path = getPath()
  updateproject = True  
  projname_clean = projname.strip()
  
  # use the correct path
  if "\\" in projname_clean or "/" in projname_clean:
    newpath = Path(projname_clean)
  else:  
    newpath = Path(path.strip() + "/" + projname_clean.strip())
    
  if newpath.suffix.strip() != "":
        
    updateproject = False
    print(getTranslation(MSG.INVALIDPROJECTNAME))
        
  else:
        
    if not newpath.exists():
    
      updateproject = False
      print(getTranslation(MSG.FOLDERPROJECTNAMENOTFOUND))
      
    else:
        
      filename, filext = os.path.splitext(page.strip())
      
      if filext != "":
          
        print(getTranslation(MSG.INVALIDPAGENAME))
        updateproject = False

      else:
          
        base = Path(newpath)
        file = page.strip()
        
        awsc = base / "logic" / f"{file}.awsc"
        awcp = base / "pages" / f"{file}.awcp"
        awui = base / "pages" / f"{file}.awui"
        
        if awsc.exists() or awcp.exists() or awui.exists():
          reply = input(getTranslation(MSG.CONFIRMOVERWRITEPAGE)).strip().lower()
        else:
          reply = "y"
          
        if reply in ['s', 'y']:
        
          # delete new page files first
          
          try:  
              
            if awsc.exists():
              awsc.unlink()
              
            if awcp.exists():
              awcp.unlink()
              
            if awui.exists():
              awui.unlink()
          
          except PermissionError:
              
            print("----------------------------------------")
            print(getTranslation(MSG.NOGRATSTOOVERWRITEORDELETEFOLDER))
            updateproject = False
            
        else:  
          updateproject = False
        
  if updateproject ==  True:
    
    try:
          
      #add page basic files to current project
        
      print("----------------------------------------")
      print(getTranslation(MSG.CREATINGPAGEFILES))

      file_ui = base / "pages" / f"{page.strip()}.awui"
      file_ui.parent.mkdir(parents=True, exist_ok=True)
      file_ui.write_text(NEWPROJECT.DOCUMENT, encoding="utf-8")
  
      file_cp = base / "pages" / f"{page.strip()}.awcp"
      file_cp.parent.mkdir(parents=True, exist_ok=True)
      file_cp.write_text("/* TO DO: Add control properties here */\n\n", encoding="utf-8")
      
      file_sc = base / "logic" / f"{page.strip()}.awsc"
      file_sc.parent.mkdir(parents=True, exist_ok=True)
      file_sc.write_text("/* TO DO: Add logic and events here */\n\n", encoding="utf-8")
      
      print(getTranslation(MSG.DONE))
        
    except PermissionError:
      
      print("----------------------------------------")
      print(getTranslation(MSG.NOGRATSTOOVERWRITEORDELETEFOLDER))
            
# Purpose: Delete a project
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 24/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def deleteProject(projname):
    
  path = getPath()
  projname_clean = projname.strip()
  
  # use the correct path
  if "\\" in projname_clean or "/" in projname_clean:
    newpath = Path(projname_clean)
  else:  
    newpath = Path(path.strip() + "/" + projname_clean.strip())
    
  if newpath.suffix.strip() != "":
    print(getTranslation(MSG.INVALIDPROJECTNAME))      
  else:
        
    if newpath.exists():
    
      if newpath.is_dir():
        
        reply = input(getTranslation(MSG.CONFIRMDELETEPROJECT)).strip().lower()
        
        if reply in ['s', 'y']:
        
          try:  
        
            # delete project folder
            
            shutil.rmtree(newpath)
            print(getTranslation(MSG.DONE))
            
          except PermissionError:
              
            print("----------------------------------------")
            print(getTranslation(MSG.NOGRATSTODELETEFOLDER))
          
      else:
        print(getTranslation(MSG.INVALIDPROJECTNAME))
        
    else:
      print(getTranslation(MSG.PROJECTFOLDERNOTFOUND))
            
# Purpose: Build a project (transpiler action)
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 12/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def buildProject(projname):
  print("Convertiré el proyecto '" + projname + "' en su equivalente php\nLa ruta actual es: " + getPath())
  
# Purpose: Show version
# Created date: 10/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 10/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def version():
  print(PROJECT_NAME + " version " + PROJECT_VERSION + "\n(C)" + PROJECT_YEAR + " " + TEAM_NAME)
  
# Purpose: Show help
# Created date: 10/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 29/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def help(cmd):
    
  if cmd.strip() == "":  
      
    lang, encoding = locale.getlocale()

    if lang and (lang.lower().startswith("es") or lang.lower().startswith("spanish")):
    
      str = PROJECT_SHORT_NAME + " reconoce los siguientes comandos:\n\n"
      str = str + "new (nombre del proyecto):\n" + getTranslation(MSG.NEWCOMMAND) + "\n\n"
      str = str + "addpage (nombre del proyecto) (nombre de la pagina):\n" + getTranslation(MSG.ADDPAGECOMMAND) + "\n\n"
      str = str + "delete (nombre del proyecto):\n" + getTranslation(MSG.DELETECOMMAND) + "\n\n"
      str = str + "build (nombre del proyecto):\n" + getTranslation(MSG.BUILDCOMMAND) + "\n\n"
      str = str + "-v: " + getTranslation(MSG.VERSION)
    
    else:
        
      str = PROJECT_SHORT_NAME + " recognizes the following commands:\n\n"
      str = str + "new (project name):\n" + getTranslation(MSG.NEWCOMMAND) + "\n\n"
      str = str + "addpage (project name) (page name):\n" + getTranslation(MSG.ADDPAGECOMMAND) + "\n\n"
      str = str + "delete (project name):\n" + getTranslation(MSG.DELETECOMMAND) + "\n\n"
      str = str + "build (project name):\n" + getTranslation(MSG.BUILDCOMMAND) + "\n\n"
      str = str + "-v: " + getTranslation(MSG.VERSION)
        
    print(str)
  
  else:

    if cmd.lower() == "new":
        
      msg = getTranslation(MSG.NEWCOMMAND)
      print(msg)  
    
    elif cmd.lower() == "addpage":
      
      msg = getTranslation(MSG.ADDPAGECOMMAND)
      print(msg)  
        
    elif cmd.lower() == "delete":
      
      msg = getTranslation(MSG.DELETECOMMAND)
      print(msg)  
      
    elif cmd.lower() == "build":
        
      msg = getTranslation(MSG.BUILDCOMMAND)
      print(msg)  
      
    else:
    
      msg = getTranslation(MSG.UNKNOWNCOMMAND)
      print(msg)
