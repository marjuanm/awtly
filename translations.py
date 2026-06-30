# Awtly - php transpiller util
# Original file name: translations.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

import locale
import importlib

from constants import PROJECT_SHORT_NAME

# Purpose: Get translation
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 30/06/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to chatpgt / gemini
def getTranslation(msgid):
    
  REGIONAL_LANGS = {
    ("es", "mexico"): "lang.es_mx",
    ("es", "spain"): "lang.es_es",
    ("en", "united states"): "lang.en_us",
    ("en", "great britain"): "lang.en_gb",
  }

  SUPPORTED_LANGS = {
    "es": "lang.es",
    "en": "lang.en",
  }

  language = ""
  country = ""
  lang, encoding = locale.getlocale()
  
  if lang:

    parts = lang.split("_", 1)
    language = parts[0].lower()

    if len(parts) > 1:
      country = parts[1].lower()

    # Load regional language file
    module = REGIONAL_LANGS.get((language, country))

    # If fail, load generic file
    if module is None:
        
      if lang.lower().startswith("es") or lang.lower().startswith("spanish"):
        module = SUPPORTED_LANGS.get(language, "lang.es")
      else:
        module = SUPPORTED_LANGS.get(language, "lang.en")
      
    try:
      trans = importlib.import_module(module)

    except ModuleNotFoundError:

      # Load generic english file if all fail already
      trans = importlib.import_module("lang.en")

    return trans.MESSAGES.get(msgid, trans.MESSAGES.get("INVALIDID", msgid))

  else:
      
    trans = importlib.import_module("lang.en")
    return trans.MESSAGES.get(msgid, trans.MESSAGES.get("INVALIDID", msgid))
