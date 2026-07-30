# Awtly - php transpiller util
# Original file name: help_action.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import os
import shutil
import locale

from pathlib import Path
from common.functions import getPath
from core.translations import getTranslation
from common.constants import PROJECT_SHORT_NAME

# Purpose: Show help
# Created date: 10/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 30/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def helpAction(cmd):
    
  if cmd.strip() == "":  
      
    lang, encoding = locale.getlocale()
    # lang = "zh"
    
    if lang and (lang.lower().startswith("es") or lang.lower().startswith("spanish")):
  
      str = PROJECT_SHORT_NAME + " reconoce los siguientes comandos:\n\n"
      str = str + getHelpCommands()
      
    elif lang and (lang.lower().startswith("ar") or lang.lower().startswith("arab")):
    
      str = PROJECT_SHORT_NAME + " يتعرف على الأوامر التالية:\n\n"
      str = str + getHelpCommands()
      
    elif lang.lower().startswith("de") or lang.lower().startswith("ger") or lang.lower().startswith("deuts"):
      
      str = PROJECT_SHORT_NAME + " erkennt die folgenden Befehle:\n\n"
      str = str + getHelpCommands()
    
    elif lang and (lang.lower().startswith("fr") or lang.lower().startswith("french")):
        
      str = PROJECT_SHORT_NAME + " reconnaît les commandes suivantes :\n\n"
      str = str + getHelpCommands()
      
    elif lang and (lang.lower().startswith("pt") or lang.lower().startswith("portuguese")):
        
      str = PROJECT_SHORT_NAME + " reconhece os seguintes comandos:\n\n"
      str = str + getHelpCommands()
      
    elif lang and (lang.lower().startswith("ru") or lang.lower().startswith("russian")):
        
      str = PROJECT_SHORT_NAME + " повторите следующие команды:\n\n"
      str = str + getHelpCommands()
      
    elif lang and (lang.lower().startswith("tr") or lang.lower().startswith("turkish")):
        
      str = PROJECT_SHORT_NAME + " şu komutları çalıştırın:\n\n"
      str = str + getHelpCommands()
      
    elif lang and (lang.lower().startswith("zh") or lang.lower().startswith("chinese") or lang.lower().startswith("ch")):  
      
      str = PROJECT_SHORT_NAME + " 识别以下命令：\n\n"
      str = str + getHelpCommands()
      
    else:
        
      str = PROJECT_SHORT_NAME + " recognizes the following commands:\n\n"
      str = str + getHelpCommands()
        
    print(str)
  
  else:
      
    lang, encoding = locale.getlocale()
    #lang = "zh"
    
    if lang and (lang.lower().startswith("es") or lang.lower().startswith("spanish")):
      currlang = "es"
    elif lang and (lang.lower().startswith("ar") or lang.lower().startswith("arab")):
      currlang = "ar"
    elif lang.lower().startswith("de") or lang.lower().startswith("ger") or lang.lower().startswith("deuts"):
      currlang = "de"
    elif lang and (lang.lower().startswith("fr") or lang.lower().startswith("french")):
      currlang = "fr"
    elif lang and (lang.lower().startswith("pt") or lang.lower().startswith("portuguese")):
      currlang = "pt"
    elif lang and (lang.lower().startswith("ru") or lang.lower().startswith("russian")):
      currlang = "ru"
    elif lang and (lang.lower().startswith("tr") or lang.lower().startswith("turkish")):
      currlang = "tr"
    elif lang and (lang.lower().startswith("zh") or lang.lower().startswith("chinese") or lang.lower().startswith("ch")):  
      currlang = "zh"
    else:
      currlang = "en"
    
    if cmd.lower() == "new":
      print(getTranslation("NEWCOMMAND") + "\n\n" + getCommandDetails("NEWCOMMAND", currlang))
    
    elif cmd.lower() == "addpage":
      print(getTranslation("ADDPAGECOMMAND") + "\n\n" + getCommandDetails("ADDPAGECOMMAND", currlang))
        
    elif cmd.lower() == "delete":
      print(getTranslation("DELETECOMMAND") + "\n\n" + getCommandDetails("DELETECOMMAND", currlang))
      
    elif cmd.lower() == "build":
      print(getTranslation("BUILDCOMMAND") + "\n\n" + getCommandDetails("BUILDCOMMAND", currlang))
      
    else:
      print(getTranslation("UNKNOWNCOMMAND"))
      
# Purpose: Return command list and basic information
# Created date: 30/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 30/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def getHelpCommands():

  str = "new: " + getTranslation("NEWCOMMAND") + "\n"
  str = str + "addpage: " + getTranslation("ADDPAGECOMMAND") + "\n"
  str = str + "delete: " + getTranslation("DELETECOMMAND") + "\n"
  str = str + "build: " + getTranslation("BUILDCOMMAND") + "\n"
  str = str + "-v: " + getTranslation("VERSION")
  
  return str

# Purpose: Return command details
# Created date: 30/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 30/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def getCommandDetails(cmd, lang):
    
  if cmd.upper().strip() == "NEWCOMMAND":
      
    if lang.lower().strip() == "es":
    
      str = "new (nombre del proyecto):\n"
      str = str + "new (nombre del proyecto) (template):\n"
      str = str + "new website|component (nombre del proyecto):\n"
      str = str + "new website|component (nombre del proyecto) (plantilla):\n"
      
    elif lang.lower().strip() == "ar": 
        
      str = "new (اسم المشروع):\n"
      str = str + "new (اسم المشروع) (القالب):\n" 
      str = str + "new website|component (اسم المشروع):\n" 
      str = str + "new website|component (اسم المشروع) (القالب):\n"
      
    elif lang.lower().strip() == "de": 
        
      str = "new (Projektname):\n"
      str = str + "new (Projektname) (Vorlage):\n" 
      str = str + "new website|component (Projektname):\n" 
      str = str + "new website|component (Projektname) (Vorlage):\n"
      
    elif lang.lower().strip() == "fr":   
        
      str = "new (nom du projet) :\n"
      str = str + "new (nom du projet) (modèle):\n" 
      str = str + "new website|component (nom du projet):\n" 
      str = str + "new website|component (nom du projet) (modèle):\n"
      
    elif lang.lower().strip() == "pt":   
      
      str = "new (nome do projeto):\n"
      str = str + "new (nome do projeto) (modelo):\n" 
      str = str + "new website|component (nome do projeto):\n" 
      str = str + "new website|component (nome do projeto) (modelo):\n"
      
    elif lang.lower().strip() == "ru":   
        
      str = "new (имя проекта):\n"
      str = str + "new (название проекта) (шаблон):\n" 
      str = str + "new website|component (название проекта):\n" 
      str = str + "new website|component (название проекта) (шаблон):\n"
        
    elif lang.lower().strip() == "tr":
        
      str = "new (proje adı):\n" + getTranslation(cmd) + "\n\n"
      str = str + "new (proje adı) (şablon):\n" + getTranslation(cmd) + "\n\n" 
      str = str + "new website|component (proje adı):\n" + getTranslation(cmd) + "\n\n" 
      str = str + "new website|component (proje adı) (şablon):\n" + getTranslation(cmd) + "\n\n"
      
    elif lang.lower().strip() == "zh":

      str = "new (项目名称)：\n"
      str = str + "new (项目名称) (模板):\n" 
      str = str + "new website|component (项目名称):\n" 
      str = str + "new website|component (项目名称) (模板):\n"
      
    else:        
        
      str = "new (project name):\n"
      str = str + "new (project name) (template):\n" 
      str = str + "new website|component (project name):\n" 
      str = str + "new website|component (project name) (template):\n"
      
  if cmd.upper().strip() == "ADDPAGECOMMAND":
      
    if lang.lower().strip() == "es":
    
      str = "addpage (nombre del proyecto) (nombre de la pagina):\n"
      str = str + "addpage (nombre del proyecto) (nombre de la pagina) (plantilla):\n"
      
    elif lang.lower().strip() == "ar": 
        
      str = "addpage (اسم المشروع) (اسم الصفحة):\n"
      str = str + "addpage (اسم المشروع) (اسم الصفحة) (القالب):\n"
      
    elif lang.lower().strip() == "de": 
        
      str = "addpage (Projektname) (Seitenname):\n"
      str = str + "addpage (Projektname) (Seitenname) (Vorlage):\n"
      
    elif lang.lower().strip() == "fr":   
        
      str = "addpage (nom du projet) (nom de la page) :\n"
      str = str + "addpage (nom du projet) (nom de la page) (modèle):\n"
      
    elif lang.lower().strip() == "pt":   
      
      str = "addpage (nome do projeto) (nome da página):\n"
      str = str + "addpage (nome do projeto) (nome da página) (modelo):\n"
      
    elif lang.lower().strip() == "ru":   
        
      str = "addpage (имя проекта) (имя страницы):\n"
      str = str + "addpage (название проекта) (название страницы) (шаблон):\n"
      str = str + "addpage (название проекта) (название страницы) (шаблон):\n"
        
    elif lang.lower().strip() == "tr":
        
      str = "addpage (proje adı) (sayfa adı):\n"
      str = str + "addpage (proje adı) (sayfa adı) (şablon):\n"
      
    elif lang.lower().strip() == "zh":

      str = "addpage (项目名称) (页面名称)：\n"
      str = str + "addpage (项目名称) (页面名称) (模板):\n"
      
    else:        
        
      str = "addpage (project name) (page name):\n"
      str = str + "addpage (project name) (page name) (template):\n"
      
  if cmd.upper().strip() == "DELETECOMMAND":
      
    if lang.lower().strip() == "es":
      str = "delete (nombre del proyecto):\n"
      
    elif lang.lower().strip() == "ar": 
      str = "delete (اسم المشروع):\n"
      
    elif lang.lower().strip() == "de": 
      str = "delete (Projektname):\n"
      
    elif lang.lower().strip() == "fr":   
      str = "delete (nom du projet) :\n"
      
    elif lang.lower().strip() == "pt":   
      str = "delete (nome do projeto):\n"
      
    elif lang.lower().strip() == "ru":   
      str = "delete (имя проекта):\n"
        
    elif lang.lower().strip() == "tr":
      str = "delete (proje adı):\n"
      
    elif lang.lower().strip() == "zh":
      str = "delete (项目名称)：\n"
      
    else:        
      str = "delete (project name):\n"
      
  if cmd.upper().strip() == "BUILDCOMMAND":
      
    if lang.lower().strip() == "es":
      str = "build (nombre del proyecto):\n"
      
    elif lang.lower().strip() == "ar": 
      str = "build (اسم المشروع):\n"
      
    elif lang.lower().strip() == "de": 
      str = "build (Projektname):\n"
      
    elif lang.lower().strip() == "fr":   
      str = "build (nom du projet) :\n"
      
    elif lang.lower().strip() == "pt":   
      str = "build (nome do projeto):\n"
      
    elif lang.lower().strip() == "ru":   
      str = "build (имя проекта):\n"
        
    elif lang.lower().strip() == "tr":
      str = "build (proje adı):\n"
      
    elif lang.lower().strip() == "zh":
      str = "build (项目名称)：\n"
      
    else:        
      str = "build (project name):\n"
      
  return str
