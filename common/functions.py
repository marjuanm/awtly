# Awtly - php transpiller util
# Original file name: gmodule.py
# New file name: functions.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from pathlib import Path

from core.translations import getTranslation

# Purpose: Get current path
# Created date: 12/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 12/06/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to gemini
# Thanks to https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
def getPath():
  return str(Path().absolute()) # Directory of current working directory, not __file__
  
# Purpose: Load configuration from cfg file
# Created date: 28/07/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 28/07/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to chatgpt
def getConfig(filename):

  config = {}
  errors = []
  filename = Path(filename)

  if not filename.exists():
    
    errors.append(getTranslation("FILENOTFOUND"))
    return False, config, errors
    
  else:

    try:

      with filename.open("r", encoding="utf-8") as f:

        for lineno, line in enumerate(f, start=1):

          line = line.strip()
          
          # Ignore empty lines
          if not line:
            continue

          # Ignore comments
          if line.startswith("#"):
            continue

          # Invalid syntax
          if "=" not in line:
            errors.append(getTranslation("INVALIDCONFIGURATIONLINE") + ", " + line.strip() + "\n" + str(filename.resolve()) + ":" + str(lineno))
            continue

          key, value = line.split("=", 1)
          key = key.strip()
          value = value.strip()
          
          # Empty key
          if not key:
            errors.append(getTranslation("EMPTYCONFIGURATIONKEY") + ", " + line.strip() + "\n" + str(filename.resolve()) + ":" + str(lineno))
            continue

          # Duplicate key
          if key in config:
            errors.append(getTranslation('DUPLICATECONFIGURATIONKEY') + ", " + line.strip() + "\n" + str(filename.resolve()) + ":" + str(lineno))
            continue
            
          # Remove quotes
          if len(value) >= 2:
            if (value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'"):
              value = value[1:-1]

          config[key] = value

    except Exception as e:
    
      errors.append(str(e))
      return False, config, errors

    if errors:
      return False, config, errors
    else:
      return True, config, []
