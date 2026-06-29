# Awtly - php transpiller util
# Original file name: translations.py
# Copyright (C) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import locale

from messages import MSG
from constants import PROJECT_SHORT_NAME

# Purpose: Get translation
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 29/06/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to gemini
def getTranslation(msgid):

  lang, encoding = locale.getlocale()

  if lang and (lang.lower().startswith("es") or lang.lower().startswith("spanish")):
      
    if msgid == MSG.INVALIDPARAMSNUMBER:
      return "Número de parámetros no válido"
    elif msgid == MSG.UNKNOWNCOMMAND:
      return "Comando desconocido"
    elif msgid == MSG.NEWCOMMAND:
      return "Crea un proyecto en la carpeta actual o en la ruta especificada."
    elif msgid == MSG.DELETECOMMAND:
      return "Elimina un proyecto de la carpeta actual o de la ruta especificada."
    elif msgid == MSG.BUILDCOMMAND:
      return "Compila un proyecto a PHP en la carpeta actual o en la ruta especificada."
    elif msgid == MSG.VERSION:
      return "Muestra la versión actual de " + PROJECT_SHORT_NAME + "."
    elif msgid == MSG.INCOMPLETECOMMAND:
      return "Comando incompleto, invoque el proyecto '" + PROJECT_SHORT_NAME + "' y luego el comando 'help' para mostrar ayuda."
    elif msgid == MSG.PATHNOTFOLDERRUNCOMMAND:
      return "La ruta ingresada no es una carpeta y no puede ser usada para ejecutar el comando actual, se usará la ruta actual en su lugar."
    elif msgid == MSG.CONFIRMOVERWRITEPROJECT:
      return "El proyecto ya existe\n¿Desea continuar? (s/n): "
    elif msgid == MSG.INVALIDPROJECTNAME:
      return "El nombre de la carpeta para su proyecto no debe contener extensiones de archivos."
    elif msgid == MSG.FOLDERPROJECTNAME:
      return "Carpeta del proyecto"
    elif msgid == MSG.CREATINGPROJECTFILES:
      return "Creando estructura del proyecto"
    elif msgid == MSG.DONE:
      return "Listo." 
    elif msgid == MSG.CONFIRMDELETEPROJECT:
      return "Borrar el proyecto\n¿Desea continuar? (s/n): "
    elif msgid == MSG.PROJECTFOLDERNOTFOUND:
      return "Proyecto no encontrado"
    elif msgid == MSG.FOLDERPROJECTNAMENOTFOUND:
      return "Proyecto no encontrado"
    elif msgid == MSG.CONFIRMOVERWRITEPAGE:
      return "Algunos archivos ya existen, se sobreescribirán\n¿Desea continuar? (s/n): "
    elif msgid == MSG.CREATINGPAGEFILES:
      return "Creando documentos adicionales"
    elif msgid == MSG.ADDPAGECOMMAND:
      return "Agrega los archivos necesarios para crear una nueva página en el proyecto especificado"
    elif msgid == MSG.INVALIDPAGENAME:
      return "El nombre de la página a agregar al proyecto no debe contener extensiones de archivos."
    else:
      return "ID de traducción inválido"
      
  else:
      
    if msgid == MSG.INVALIDPARAMSNUMBER:
      return "Invalid number of parameters"
    elif msgid == MSG.UNKNOWNCOMMAND:
      return "Unknown command"
    elif msgid == MSG.NEWCOMMAND:
      return "Create a project in the current folder or the specified path."
    elif msgid == MSG.DELETECOMMAND:
      return "Deletes a project from the current folder or specified path."
    elif msgid == MSG.BUILDCOMMAND:
      return "Compiles a PHP project in the current folder or specified path."
    elif msgid == MSG.VERSION:
      return "Show " + PROJECT_SHORT_NAME + "'s current version."
    elif msgid == MSG.INCOMPLETECOMMAND:
      return "Incomplete command, invoke the project '" + PROJECT_SHORT_NAME + "' and then the 'help' command to display help."
    elif msgid == MSG.PATHNOTFOLDERRUNCOMMAND:
      return "The path entered is not a folder and cannot be used to execute the current command, the current path will be used instead."
    elif msgid == MSG.CONFIRMOVERWRITEPROJECT:
      return "The project already exists\nDo you want continue? (y/n): "
    elif msgid == MSG.INVALIDPROJECTNAME:
      return "The folder name for your project should not contain file extensions."
    elif msgid == MSG.FOLDERPROJECTNAME:
      return "Folder project name"
    elif msgid == MSG.CREATINGPROJECTFILES:
      return "Creating project structure"
    elif msgid == MSG.DONE:
      return "Done." 
    elif msgid == MSG.CONFIRMDELETEPROJECT:
      return "Delete the project\nDo you want continue? (y/n): "
    elif msgid == MSG.PROJECTFOLDERNOTFOUND:
      return "Project not found"
    elif msgid == MSG.FOLDERPROJECTNAMENOTFOUND:
      return "Project not found"
    elif msgid == MSG.CONFIRMOVERWRITEPAGE:
      return "Some files already exist, they will be overwritten\nDo you want continue? (y/n): "
    elif msgid == MSG.CREATINGPAGEFILES:
      return "Creating additional documents"
    elif msgid == MSG.ADDPAGECOMMAND:
      return "Adds the files needed to create a new page in the specified project"
    elif msgid == MSG.INVALIDPAGENAME:
      return "The name of the page to be added to the project must not contain file extensions."
    else:
      return "Invalid ID translator"
