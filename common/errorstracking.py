# Awtly - php transpiller util
# Original file name: errorstracking.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.
import sys
import platform

from pathlib import Path
from datetime import datetime
from common.functions import getPath
from common.globals import debugfile
from common.constants import PROJECT_VERSION

# Purpose: Save to log file
# Created date: 02/08/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 02/08/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to chatgpt
def errortolog(message):
    
  if debugfile.strip().lower() == "":
    dfile = Path(getPath()) / "debug.log"
  else:
    dfile = Path(getPath()) / debugfile.strip()

  dfile.parent.mkdir(parents=True, exist_ok=True)
  
  # truncate if size is over 
  if dfile.exists() and dfile.stat().st_size > 10485760:  # 10 MB
        
    content = dfile.read_text(encoding="utf-8", errors="ignore")
    middle = len(content) // 2
    newline = content.find("\n", middle)

    if newline != -1:
      content = content[newline + 1:]
    else:
      content = content[middle:]

    dfile.write_text(content, encoding="utf-8")

  # write error
  with dfile.open("a", encoding="utf-8") as logfile:
      
    logfile.write("=" * 20 + "\n")
    logfile.write(f"AWTLY       : {PROJECT_VERSION}\n")
    logfile.write(f"Python      : {sys.version.split()[0]}\n")
    logfile.write(f"Platform    : {platform.platform()}\n")
    logfile.write(f"OS          : {platform.system()}\n")
    logfile.write(f"OS version  : {platform.version()}\n")
    logfile.write(f"Architecture: {platform.architecture()[0]}\n")
    logfile.write(f"Machine     : {platform.machine()}\n")
    logfile.write(f"Processor   : {platform.processor()}\n")
    logfile.write(f"Started     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    logfile.write("=" * 20 + "\n\n")
  
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logfile.write(f"[{now}] {message}\n")
