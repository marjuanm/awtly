# Awtly - php transpiller util
# Original file name: en_US.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from common.constants import PROJECT_SHORT_NAME

# USA translation
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Invalid number of parameters",
  "UNKNOWNCOMMAND":
    "Unknown command",
  "NEWCOMMAND":
    "Create a project in the current folder or the specified path.",
  "DELETECOMMAND":
    "Deletes a project from the current folder or specified path.",
  "BUILDCOMMAND":
    "Compiles a PHP project in the current folder or specified path.",
  "VERSION":
    "Show " + PROJECT_SHORT_NAME + "'s current version.",
  "INCOMPLETECOMMAND":
    "Incomplete command, invoke the project '" + PROJECT_SHORT_NAME + "' and then the 'help' command to display help.",
  "PATHNOTFOLDERRUNCOMMAND":
    "The path entered is not a folder and cannot be used to execute the current command, the current path will be used instead.",
  "CONFIRMOVERWRITEPROJECT":
    "The project already exists\nDo you want continue? (y/n): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "You don't have permission to overwrite or delete the project folder",
  "INVALIDPROJECTNAME":
    "The folder name for your project should not contain file extensions.",
  "INVALIDTEMPLATENAME":
    "The template folder name should not contain file extensions.",
  "TEMPLATENOTFOUND":
    "The template folder was not found.",
  "FOLDERPROJECTNAME":
    "Folder project name",
  "CREATINGPROJECTFILES":
    "Creating project structure",
  "DONE":
    "Done.", 
  "CONFIRMDELETEPROJECT":
    "Delete the project\nDo you want continue? (y/n): ",
  "PROJECTFOLDERNOTFOUND":
    "Project not found",
  "FOLDERPROJECTNAMENOTFOUND":
    "Project not found",
  "PROJECTFILENOTFOUND":
    "Project file not found",
  "FILENOTFOUND": 
    "The file was not found",
  "INVALIDCONFIGURATIONLINE": 
    "Invalid line in config file",
  "EMPTYCONFIGURATIONKEY": 
    "Empty key in config file",
  "DUPLICATECONFIGURATIONKEY": 
    "Duplicate key in config file",
  "CONFIRMOVERWRITEPAGE":
    "Some files already exist, they will be overwritten\nDo you want continue? (y/n): ",
  "CREATINGPAGEFILES":
    "Creating additional documents",
  "ADDPAGECOMMAND":
    "Adds the files needed to create a new page in the specified project",
  "INVALIDPAGENAME":
    "The name of the page to be added to the project must not contain file extensions.",
  "UNKNOWNLANGUAGE":
    "Unknown language.",
  "ALREADYERRORSFOUND":
    "Errors found during execution, please check your debug file.",
  "INVALIDID":
    "Invalid ID translator"
}
