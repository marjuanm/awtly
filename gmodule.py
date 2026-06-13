from pathlib import Path
from messages import MSG
from translations import getTranslation

# Purpose: Update current path
# Created date: 12/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 12/06/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to gemini
# Thanks to https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
def getPath():
  return str(Path().absolute()) # Directory of current working directory, not __file__
