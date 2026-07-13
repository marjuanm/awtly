# Awtly - php transpiller util
# Original file name: es_MX.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from constants import PROJECT_SHORT_NAME

# Mexico translation file
MESSAGES = {
	
  "INVALIDPARAMSNUMBER":
	"Número de parámetros no válido",
  "UNKNOWNCOMMAND":
    "Comando desconocido",
  "NEWCOMMAND":
    "Crea un proyecto en la carpeta actual o en la ruta especificada.",
  "DELETECOMMAND":
    "Elimina un proyecto de la carpeta actual o de la ruta especificada.",
  "BUILDCOMMAND":
    "Compila un proyecto a PHP en la carpeta actual o en la ruta especificada.",
  "VERSION":
    "Muestra la versión actual de " + PROJECT_SHORT_NAME + ".",
  "INCOMPLETECOMMAND":
    "Comando incompleto, invoque el proyecto '" + PROJECT_SHORT_NAME + "' y luego escriba el comando 'help' para mostrar ayuda.",
  "PATHNOTFOLDERRUNCOMMAND":
    "La ruta ingresada no es una carpeta y no puede ser usada para ejecutar el comando actual, se usará la ruta actual en su lugar.",
  "CONFIRMOVERWRITEPROJECT":
    "El proyecto ya existe\n¿Desea continuar? (s/n): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "No cuenta con permisos para sobreescribir o borrar la carpeta del proyecto",
  "INVALIDPROJECTNAME":
    "El nombre de la carpeta para el proyecto no debe contener extensiones de archivos.",
  "INVALIDTEMPLATENAME":
    "El nombre de la carpeta de plantilla no debe contener extensiones de archivo.",
  "TEMPLATENOTFOUND":
    "No se encuentra la carpeta de la plantilla.",
  "FOLDERPROJECTNAME":
    "Carpeta del proyecto",
  "CREATINGPROJECTFILES":
    "Creando la estructura del proyecto",
  "DONE":
    "Listo.", 
  "CONFIRMDELETEPROJECT":
    "Borrar el proyecto\n¿Desea continuar? (s/n): ",
  "PROJECTFOLDERNOTFOUND":
    "Proyecto no encontrado",
  "FOLDERPROJECTNAMENOTFOUND":
    "Proyecto no encontrado",
  "CONFIRMOVERWRITEPAGE":
    "Algunos archivos ya existen y se sobreescribirán\n¿Desea continuar? (s/n): ",
  "CREATINGPAGEFILES":
    "Creando documentos adicionales",
  "ADDPAGECOMMAND":
    "Agrega los archivos necesarios para crear una nueva página en el proyecto especificado",
  "INVALIDPAGENAME":
    "El nombre de la página para agregar al proyecto no debe contener extensiones de archivos.",
  "INVALIDID":
    "ID de traducción inválido"			
						
}
