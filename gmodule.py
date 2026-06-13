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
  
# Purpose: Get operative system type
# Created date: 12/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 12/06/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to gemini
def getOS():
    
  path = getPath()

  if len(path.strip()) < 2:
    return "unknown"
  else:

    if path[0].strip() == "/":
      return "linux"
    else:
    
      if len(path.strip()) < 2:
        return "unknown"
      else:
      
        subpath = path.strip()[1]

        if subpath.strip() == ":":
          return "windows"
        else:
          return "unknown"
