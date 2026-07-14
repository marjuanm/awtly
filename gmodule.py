# Awtly - php transpiller util
# Original file name: gmodule.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from pathlib import Path

# Purpose: Update current path
# Created date: 12/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 12/06/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to gemini
# Thanks to https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
def getPath():
  return str(Path().absolute()) # Directory of current working directory, not __file__
