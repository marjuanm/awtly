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
# Last modified date: 02/07/2026
# Last modified username: Juan Manuel Mar Hdz.
# Thanks to chatpgt / gemini
def getTranslation(msgid):
    
  REGIONAL_LANGS = {
    ("es", "mexico"): "lang.es_mx",
    ("Spanish", "Mexico"): "lang.es_mx",
    ("es", "spain"): "lang.es_es",
    ("Spanish", "Spain"): "lang.es_ES",
    ("en", "united states"): "lang.en_us",
    ("English", "United States"): "lang.en_us",
    ("en", "great britain"): "lang.en_gb",
    ("English", "Great Britain"): "lang.en_gb",
    ("pt", "portugal"): "lang.pt_pt",
    ("Portuguese", "Portugal"): "lang.pt_pt",
    ("pt", "brazil"): "lang.pt_br",
    ("Portuguese", "Brazil"): "lang.pt_br",
  }

  SUPPORTED_LANGS = {
    "es": "lang.es",
    "en": "lang.en",
    "ar": "lang.ar",
    "de": "lang.de",
    "fr": "lang.fr",
    "pt": "lang.pt",
    "ru": "lang.ru",
    "tr": "lang.tr",
    "zh": "lang.zh",
    "ch": "lang.zh",
  }

  language = ""
  country = ""
  lang, encoding = locale.getlocale()
  #lang = "zh"
  
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
      elif lang.lower().startswith("ar") or lang.lower().startswith("arab"):
        module = SUPPORTED_LANGS.get(language, "lang.ar")
      elif lang.lower().startswith("de") or lang.lower().startswith("ger") or lang.lower().startswith("deuts"):
        module = SUPPORTED_LANGS.get(language, "lang.de")
      elif lang and (lang.lower().startswith("fr") or lang.lower().startswith("french")):  
        module = SUPPORTED_LANGS.get(language, "lang.fr")
      elif lang and (lang.lower().startswith("pt") or lang.lower().startswith("portuguese")):  
        module = SUPPORTED_LANGS.get(language, "lang.pt")
      elif lang and (lang.lower().startswith("ru") or lang.lower().startswith("russian")):  
        module = SUPPORTED_LANGS.get(language, "lang.ru")
      elif lang and (lang.lower().startswith("tr") or lang.lower().startswith("turkish")):  
        module = SUPPORTED_LANGS.get(language, "lang.tr")
      elif lang and (lang.lower().startswith("zh") or lang.lower().startswith("chinese") or lang.lower().startswith("ch")):  
        module = SUPPORTED_LANGS.get(language, "lang.zh")
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
