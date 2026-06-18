import shutil
import locale

from pathlib import Path
from messages import MSG
from gmodule import getPath
from translations import getTranslation
from newprojectstructure import NPRJSTRUCT
from constants import PROJECT_NAME, PROJECT_SHORT_NAME, PROJECT_VERSION, PROJECT_YEAR, TEAM_NAME

# Purpose: Create a new project
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 13/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def newProject(projname):
    
  path = getPath()
  createproject = True  
  projname_clean = projname.strip()
  
  if "\\" in projname_clean or "/" in projname_clean:
    
    newpath = Path(projname_clean)
    
    if newpath.suffix.strip() != "":
        
      createproject = False
      print(getTranslation(MSG.INVALIDPROJECTNAME))
        
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
        
            try:  
              shutil.rmtree(newpath)
            except PermissionError:
              
              print("----------------------------------------" + getTranslation(MSG.NOGRATSTOOVERWRITEORDELETEFOLDER))
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
        
        folder = newpath / "templates" #User templates folder
        folder.mkdir(parents=True, exist_ok=True)
        
        folder = newpath / "assets/css" #Assets css folder
        folder.mkdir(parents=True, exist_ok=True)
        
        folder = newpath / "assets/js" #Assets javascripts folder
        folder.mkdir(parents=True, exist_ok=True)
        
        folder = newpath / "assets/images" #Assets images folder
        folder.mkdir(parents=True, exist_ok=True)
        
        file = newpath / "project.cfg" #Main project
        file.write_text(NPRJSTRUCT.PROJECT, encoding="utf-8")
        
        file = newpath / "pages/index.awui" #Awtly user interfaz
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(NPRJSTRUCT.DOCUMENT, encoding="utf-8")
        
        file = newpath / "pages/index.awcp" #Awtly control properties
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text("/* TODO: Add control properties here */\n\n", encoding="utf-8")
        
        file = newpath / "logic/index.awsc" #Awtly source code
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text("/* TODO: Add logic and events here */\n\n", encoding="utf-8")
        
        file = newpath / "config/routes.awrt" #Awtly routes
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text("/* TODO: Add pages routes and redirections here */\n\n", encoding="utf-8")
        
        file = newpath / "config/db.cfg" #Database configuration
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(NPRJSTRUCT.DB, encoding="utf-8")
        
        file = newpath / "config/cache.cfg" #Cache configuration
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(NPRJSTRUCT.CACHE, encoding="utf-8")
        
        file = newpath / "assets/css/styles.css" #Project styles
        file.write_text(NPRJSTRUCT.STYLES, encoding="utf-8")
        
        print("----------------------------------------\n" + getTranslation(MSG.CREATINGPROJECTFILES) + "\n" + getTranslation(MSG.DONE))
        
      except PermissionError:
        print("----------------------------------------" + getTranslation(MSG.NOGRATSTOOVERWRITEORDELETEFOLDER))
            
# Purpose: Delete a project
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 12/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def deleteProject(projname):
  print("Borraré el proyecto '" + projname + "\nLa ruta actual es: " + getPath())
  
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
# Last modified date: 10/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def help(cmd):
    
  if cmd.strip() == "":  
      
    lang, encoding = locale.getlocale()

    if lang and (lang.lower().startswith("es") or lang.lower().startswith("spanish")):
    
      str = PROJECT_SHORT_NAME + " reconoce los siguientes comandos:\n\n"
      str = str + "new (nombre del proyecto):\n" + getTranslation(MSG.NEWCOMMAND) + "\n\n"
      str = str + "delete (nombre del proyecto):\n" + getTranslation(MSG.DELETECOMMAND) + "\n\n"
      str = str + "build (nombre del proyecto):\n" + getTranslation(MSG.BUILDCOMMAND) + "\n\n"
      str = str + "-v: " + getTranslation(MSG.VERSION)
    
    else:
        
      str = PROJECT_SHORT_NAME + " recognizes the following commands:\n\n"
      str = str + "new (project name):\n" + getTranslation(MSG.NEWCOMMAND) + "\n\n"
      str = str + "delete (project name):\n" + getTranslation(MSG.DELETECOMMAND) + "\n\n"
      str = str + "build (project name):\n" + getTranslation(MSG.BUILDCOMMAND) + "\n\n"
      str = str + "-v: " + getTranslation(MSG.VERSION)
        
    print(str)
  
  else:
      
    if cmd.lower() == "new":
        
      msg = getTranslation(MSG.NEWCOMMAND)
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
