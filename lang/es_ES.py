# Awtly - php transpiller util
# Original file name: es_ES.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from common.constants import PROJECT_SHORT_NAME

# Spain translation
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Número de parámetros no válido.",
  "UNKNOWNCOMMAND":
    "Comando desconocido.",
  "NEWCOMMAND":
    "Crea un proyecto en la carpeta actual o en la ruta especificada.",
  "DELETECOMMAND":
    "Elimina un proyecto de la carpeta actual o de la ruta especificada.",
  "BUILDCOMMAND":
    "Compila un proyecto a PHP en la carpeta actual o en la ruta especificada.",
  "VERSION":
    "Muestra la versión actual de " + PROJECT_SHORT_NAME + ".",
  "INCOMPLETECOMMAND":
    "Comando incompleto. Ejecute el proyecto '" + PROJECT_SHORT_NAME + "' seguido del comando 'help' para mostrar la ayuda.",
  "PATHNOTFOLDERRUNCOMMAND":
    "La ruta especificada no es una carpeta y no se puede utilizar para ejecutar el comando actual. Se utilizará la ruta actual en su lugar.",
  "CONFIRMOVERWRITEPROJECT":
    "El proyecto ya existe.\n¿Desea continuar? (s/n): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "No cuenta con permisos para sobreescribir o borrar la carpeta del proyecto",
  "INVALIDPROJECTNAME":
    "El nombre de la carpeta para el proyecto no debe contener extensiones de archivo.",
  "INVALIDTEMPLATENAME":
    "El nombre de la carpeta de plantilla no debe contener extensiones de archivo.",
  "TEMPLATENOTFOUND":
    "No se encuentra la carpeta de la plantilla.",
  "FOLDERPROJECTNAME":
    "Carpeta del proyecto",
  "CREATINGPROJECTFILES":
    "Creando la estructura del proyecto",
  "DONE":
    "Operación finalizada.", 
  "CONFIRMDELETEPROJECT":
    "Eliminar el proyecto.\n¿Desea continuar? (s/n): ",
  "PROJECTFOLDERNOTFOUND":
    "Proyecto no encontrado.",
  "FOLDERPROJECTNAMENOTFOUND":
    "Proyecto no encontrado.",
  "PROJECTFILENOTFOUND": 
    "No se ha encontrado el archivo de proyecto",
  "FILENOTFOUND": 
    "No se ha encontrado el archivo",
  "INVALIDCONFIGURATIONLINE": 
    "Línea no válida en el archivo de configuración",
  "EMPTYCONFIGURATIONKEY": 
    "Clave vacía en el archivo de configuración",
  "DUPLICATECONFIGURATIONKEY": 
    "Clave duplicada en el archivo de configuración",
  "CONFIRMOVERWRITEPAGE":
    "Algunos archivos ya existen y se sobrescribirán.\n¿Desea continuar? (s/n): ",
  "CREATINGPAGEFILES":
    "Creando documentos adicionales",
  "ADDPAGECOMMAND":
    "Agrega los archivos necesarios para crear una nueva página en el proyecto especificado.",
  "INVALIDPAGENAME":
    "El nombre de la página para agregar al proyecto no debe contener extensiones de archivo.",
  "INVALIDID":
    "ID de traducción no válido."
}
