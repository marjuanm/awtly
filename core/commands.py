# Awtly - php transpiller util
# Original file name: commands.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import os
import shutil
import locale

from pathlib import Path
from gmodule import getPath
from core.translations import getTranslation
from core.cmd_actions.newproject_action import newProjectAction
from core.cmd_actions.addpage_action import addPageAction
from constants import PROJECT_NAME, PROJECT_SHORT_NAME, PROJECT_VERSION, PROJECT_YEAR, TEAM_NAME

# Purpose: Create a new project
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 07/07/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to chatgpt
def newProject(projname, projtype, template):
  newProjectAction(projname, projtype, template)

# Purpose: Add a new page to project structure
# Created date: 29/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 13/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def addPage(projname, page, template):
  addPageAction(projname, page, template) 
    
# Purpose: Delete a project
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 30/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def deleteProject(projname):
    
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
        
        reply = input(getTranslation("CONFIRMDELETEPROJECT")).strip().lower()
        
        if reply in ['s', 'y', 'j', 'o', 'e']:
        
          try:  
        
            # delete project folder
            
            shutil.rmtree(newpath)
            print(getTranslation("DONE"))
            
          except PermissionError:
              
            print("----------------------------------------")
            print(getTranslation("NOGRATSTODELETEFOLDER"))
          
      else:
        print(getTranslation("INVALIDPROJECTNAME"))
        
    else:
      print(getTranslation("PROJECTFOLDERNOTFOUND"))
            
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
# Last modified date: 30/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def version():
  print(PROJECT_NAME + " version " + PROJECT_VERSION + "\n(c) " + PROJECT_YEAR + " " + TEAM_NAME)
  
# Purpose: Show help
# Created date: 10/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 02/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def help(cmd):
    
  if cmd.strip() == "":  
      
    lang, encoding = locale.getlocale()
    #lang = "zh"
    
    if lang and (lang.lower().startswith("es") or lang.lower().startswith("spanish")):
    
      str = PROJECT_SHORT_NAME + " reconoce los siguientes comandos:\n\n"
      str = str + "new (nombre del proyecto):\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (nombre del proyecto) (nombre de la pagina):\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (nombre del proyecto):\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (nombre del proyecto):\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v: " + getTranslation("VERSION")
      
    elif lang and (lang.lower().startswith("ar") or lang.lower().startswith("arab")):
    
      str = PROJECT_SHORT_NAME + " يتعرف على الأوامر التالية:\n\n"
      str = str + "new (اسم المشروع):\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (اسم المشروع) (اسم الصفحة):\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (اسم المشروع):\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (اسم المشروع):\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v: " + getTranslation("VERSION")
      
    elif lang.lower().startswith("de") or lang.lower().startswith("ger") or lang.lower().startswith("deuts"):
      
      str = PROJECT_SHORT_NAME + " erkennt die folgenden Befehle:\n\n"
      str = str + "new (Projektname):\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (Projektname) (Seitenname):\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (Projektname):\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (Projektname):\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v: " + getTranslation("VERSION")      
    
    elif lang and (lang.lower().startswith("fr") or lang.lower().startswith("french")):
        
      str = PROJECT_SHORT_NAME + " reconnaît les commandes suivantes :\n\n"
      str = str + "new (nom du projet) :\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (nom du projet) (nom de la page) :\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (nom du projet) :\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (nom du projet) :\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v : " + getTranslation("VERSION")
      
    elif lang and (lang.lower().startswith("pt") or lang.lower().startswith("portuguese")):
        
      str = PROJECT_SHORT_NAME + " reconhece os seguintes comandos:\n\n"
      str = str + "new (nome do projeto):\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (nome do projeto) (nome da página):\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (nome do projeto):\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (nome do projeto):\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v: " + getTranslation("VERSION")
      
    elif lang and (lang.lower().startswith("ru") or lang.lower().startswith("russian")):
        
      str = PROJECT_SHORT_NAME + " повторите следующие команды:\n\n"
      str = str + "new (имя проекта):\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (имя проекта) (имя страницы):\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (имя проекта):\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (имя проекта):\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v: " + getTranslation("VERSION")
      
    elif lang and (lang.lower().startswith("tr") or lang.lower().startswith("turkish")):
        
      str = PROJECT_SHORT_NAME + " şu komutları çalıştırın:\n\n"
      str = str + "new (proje adı):\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (proje adı) (sayfa adı):\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (proje adı):\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (proje adı):\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v: " + getTranslation("VERSION")
      
    elif lang and (lang.lower().startswith("zh") or lang.lower().startswith("chinese") or lang.lower().startswith("ch")):  
      
      str = PROJECT_SHORT_NAME + " 识别以下命令：\n\n"
      str = str + "new (项目名称)：\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (项目名称) (页面名称)：\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (项目名称)：\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (项目名称)：\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v: " + getTranslation("VERSION")
      
    else:
        
      str = PROJECT_SHORT_NAME + " recognizes the following commands:\n\n"
      str = str + "new (project name):\n" + getTranslation("NEWCOMMAND") + "\n\n"
      str = str + "addpage (project name) (page name):\n" + getTranslation("ADDPAGECOMMAND") + "\n\n"
      str = str + "delete (project name):\n" + getTranslation("DELETECOMMAND") + "\n\n"
      str = str + "build (project name):\n" + getTranslation("BUILDCOMMAND") + "\n\n"
      str = str + "-v: " + getTranslation("VERSION")
        
    print(str)
  
  else:

    if cmd.lower() == "new":
      print(getTranslation("NEWCOMMAND"))
    
    elif cmd.lower() == "addpage":
      print(getTranslation("ADDPAGECOMMAND"))
        
    elif cmd.lower() == "delete":
      print(getTranslation("DELETECOMMAND"))
      
    elif cmd.lower() == "build":
      print(getTranslation("BUILDCOMMAND"))
      
    else:
      print(getTranslation("UNKNOWNCOMMAND"))
