# Awtly - php transpiller util
# Original file name: en_GB.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from common.constants import PROJECT_SHORT_NAME

# England translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Invalid number of parameters",
  "UNKNOWNCOMMAND":
    "Unknown command",
  "NEWCOMMAND":
    "Creates a project in the current directory or the specified path.",
  "DELETECOMMAND":
    "Deletes a project from the current directory or the specified path.",
  "BUILDCOMMAND":
    "Compiles a project to PHP in the current directory or the specified path.",
  "VERSION":
    "Shows the current version of " + PROJECT_SHORT_NAME + ".",
  "INCOMPLETECOMMAND":
    "Incomplete command. Run the project '" + PROJECT_SHORT_NAME + "' followed by the 'help' command to display help.",
  "PATHNOTFOLDERRUNCOMMAND":
    "The specified path is not a directory and cannot be used to execute the current command. The current directory will be used instead.",
  "CONFIRMOVERWRITEPROJECT":
    "The project already exists.\nDo you want to continue? (y/n): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "You don't have permission to overwrite or delete the project folder",
  "INVALIDPROJECTNAME":
    "The project directory name must not contain file extensions.",
  "INVALIDTEMPLATENAME":
    "The template directory name must not contain file extensions.",
  "TEMPLATENOTFOUND":
    "The template directory was not found.",
  "FOLDERPROJECTNAME":
    "Project directory",
  "CREATINGPROJECTFILES":
    "Creating project structure",
  "DONE":
    "Completed.", 
  "CONFIRMDELETEPROJECT":
    "Delete the project.\nDo you want to continue? (y/n): ",
  "PROJECTFOLDERNOTFOUND":
    "Project not found",
  "FOLDERPROJECTNAMENOTFOUND":
    "Project not found",
  "PROJECTFILENOTFOUND": 
    "Project file could not be found",
  "FILENOTFOUND": 
    "File could not be found",
  "INVALIDCONFIGURATIONLINE": 
    "Invalid line in configuration file",
  "EMPTYCONFIGURATIONKEY": 
    "Empty key in configuration file",
  "DUPLICATECONFIGURATIONKEY": 
    "Duplicate key in configuration file",
  "CONFIRMOVERWRITEPAGE":
    "Some files already exist and will be overwritten.\nDo you want to continue? (y/n): ",
  "CREATINGPAGEFILES":
    "Creating additional files",
  "ADDPAGECOMMAND":
    "Adds the files required to create a new page in the specified project",
  "INVALIDPAGENAME":
    "The name of the page to add to the project must not contain file extensions.",
  "INVALIDID":
    "Invalid translation ID"
}
