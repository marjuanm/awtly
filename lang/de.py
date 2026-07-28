# Awtly - php transpiller util
# Original file name: de.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from constants import PROJECT_SHORT_NAME

# Generic German translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Ungültige Anzahl von Parametern",
  "UNKNOWNCOMMAND":
    "Unbekannter Befehl",
  "NEWCOMMAND":
    "Erstellt ein Projekt im aktuellen Ordner oder im angegebenen Pfad.",
  "DELETECOMMAND":
    "Löscht ein Projekt aus dem aktuellen Ordner oder dem angegebenen Pfad.",
  "BUILDCOMMAND":
    "Kompiliert ein Projekt zu PHP im aktuellen Ordner oder im angegebenen Pfad.",
  "VERSION":
    "Zeigt die aktuelle Version von " + PROJECT_SHORT_NAME + " an.",
  "INCOMPLETECOMMAND":
    "Unvollständiger Befehl. Führen Sie das Projekt '" + PROJECT_SHORT_NAME + "' gefolgt vom Befehl 'help' aus, um die Hilfe anzuzeigen.",
  "PATHNOTFOLDERRUNCOMMAND":
    "Der angegebene Pfad ist kein Ordner und kann nicht zur Ausführung des aktuellen Befehls verwendet werden. Stattdessen wird der aktuelle Pfad verwendet.",
  "CONFIRMOVERWRITEPROJECT":
    "Das Projekt existiert bereits.\nMöchten Sie fortfahren? (j/n): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "Sie haben keine Berechtigung, den Projektordner zu überschreiben oder zu löschen",
  "INVALIDPROJECTNAME":
    "Der Name des Projektordners darf keine Dateiendungen enthalten.",
  "INVALIDTEMPLATENAME":
    "Der Name des Vorlagenordners darf keine Dateiendungen enthalten.",
  "TEMPLATENOTFOUND":
    "Der Vorlagenordner wurde nicht gefunden.",
  "FOLDERPROJECTNAME":
    "Projektordner",
  "CREATINGPROJECTFILES":
    "Projektstruktur wird erstellt",
  "DONE":
    "Fertig.", 
  "CONFIRMDELETEPROJECT":
    "Projekt löschen.\nMöchten Sie fortfahren? (j/n): ",
  "PROJECTFOLDERNOTFOUND":
    "Projekt nicht gefunden",
  "FOLDERPROJECTNAMENOTFOUND":
    "Projekt not gefunden",
  "PROJECTFILENOTFOUND":
    "Projektdatei nicht gefunden",
  "FILENOTFOUND":
    "Datei nicht gefunden",
  "INVALIDCONFIGURATIONLINE":
    "Ungültige Zeile in der Konfigurationsdatei",
  "EMPTYCONFIGURATIONKEY":
    "Leerer Schlüssel in der Konfigurationsdatei",
  "DUPLICATECONFIGURATIONKEY":
    "Doppelter Schlüssel in der Konfigurationsdatei",
  "CONFIRMOVERWRITEPAGE":
    "Einige Dateien existieren bereits und werden überschrieben.\nMöchten Sie fortfahren? (j/n): ",
  "CREATINGPAGEFILES":
    "Zusätzliche Dateien werden erstellt",
  "ADDPAGECOMMAND":
    "Fügt die erforderlichen Dateien hinzu, um eine neue Seite im angegebenen Projekt zu erstellen",
  "INVALIDPAGENAME":
    "Der Name der zum Projekt hinzuzufügenden Seite darf keine Dateiendungen enthalten.",
  "INVALIDID":
    "Ungültige Übersetzungs-ID"
}
