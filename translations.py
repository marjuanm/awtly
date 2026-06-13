import locale

from messages import MSG
from constants import PROJECT_SHORT_NAME

# Purpose: Get translation
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 13/06/2026
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
      return "Comando incompleto, escriba '" + PROJECT_SHORT_NAME + " help' para mostrar ayuda."
    elif msgid == MSG.PATHNOTFOLDERRUNCOMMAND:
      return "La ruta ingresada no es una carpeta y no puede ser usada para ejecutar el comando actual, se usará la ruta actual en su lugar."
    elif msgid == MSG.CONFIRMOVERWRITEPROJECT:
      return "El proyecto ya existe\n¿Desea continuar? (s/n): "
    elif msgid == MSG.INVALIDPROJECTNAME:
      return "El nombre de la carpeta para su proyecto no debe contener extensiones de archivos."
    elif msgid == MSG.FOLDERPROJECTNAME:
      return "Carpeta del proyecto"
    elif msgid == MSG.PATH:
      return "Ruta"
    elif msgid == MSG.YOURREPLY:
      return "¿Borrar la carpeta del proyecto y crear todo de nuevo? (s/n): " 
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
      return "Incomplete command, type '" + PROJECT_SHORT_NAME + " help' to show help."
    elif msgid == MSG.PATHNOTFOLDERRUNCOMMAND:
      return "The path entered is not a folder and cannot be used to execute the current command, the current path will be used instead."
    elif msgid == MSG.CONFIRMOVERWRITEPROJECT:
      return "The project already exists\nDo you want continue? (y/n): "
    elif msgid == MSG.INVALIDPROJECTNAME:
      return "The folder name for your project should not contain file extensions."
    elif msgid == MSG.FOLDERPROJECTNAME:
      return "Folder project name"
    elif msgid == MSG.PATH:
      return "Path"
    elif msgid == MSG.YOURREPLY:
      return "Should I delete the project folder and recreate it? (y/n): " 
    else:
      return "Invalid ID translator"
