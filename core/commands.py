# Awtly - php transpiller util
# Original file name: commands.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import os
import shutil
import locale

from pathlib import Path
from common.functions import getPath
from core.translations import getTranslation
from core.cmd_actions.newproject_action import newProjectAction
from core.cmd_actions.addpage_action import addPageAction
from core.cmd_actions.deleteproject_action import deleteProjectAction
from core.cmd_actions.buildproject_action import buildProjectAction
from core.cmd_actions.help_action import helpAction
from common.constants import PROJECT_NAME, PROJECT_SHORT_NAME, PROJECT_VERSION, PROJECT_YEAR, TEAM_NAME

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
# Last modified date: 14/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def deleteProject(projname):
  deleteProjectAction(projname)

# Purpose: Build a project (transpiler action)
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 28/07/2026
# Last modified username: Juan Manuel Mar Hdz.
def buildProject(projname):
  buildProjectAction(projname)
  
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
  helpAction(cmd)
