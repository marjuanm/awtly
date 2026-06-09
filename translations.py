import locale

from messages import MSG

# Purpose: Get translation
# Created date: 08/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 08/06/2026
# Last modified username: Juan Manuel Mar Hdz.
def getTranslation(msgid):

  lang, encoding = locale.getlocale()

  if lang and (lang.lower().startswith("es") or lang.lower().startswith("spanish")):
      
    if msgid == MSG.INVALIDPARAMSNUMBER:
      return "Número de parámetros no válido"
    elif msgid == MSG.INVALIDPARAMETER:
      return "Parámetro desconocido"
    else:
      return "ID de traducción inválido"
      
  else:
      
    if msgid == MSG.INVALIDPARAMSNUMBER:
      return "Invalid number of parameters"
    elif msgid == MSG.INVALIDPARAMETER:
      return "Unknown parameter"
    else:
      return "Invalid ID translator"

