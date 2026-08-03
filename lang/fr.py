# Awtly - php transpiller util
# Original file name: fr.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from common.constants import PROJECT_SHORT_NAME

# Generic French translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Nombre de paramètres invalide",
  "UNKNOWNCOMMAND":
    "Commande inconnue",
  "NEWCOMMAND":
    "Crée un projet dans le dossier actuel ou le chemin spécifié.",
  "DELETECOMMAND":
    "Supprime un projet du dossier actuel ou du chemin spécifié.",
  "BUILDCOMMAND":
    "Compile un projet en PHP dans le dossier actuel ou le chemin spécifié.",
  "VERSION":
    "Affiche la version actuelle de " + PROJECT_SHORT_NAME + ".",
  "INCOMPLETECOMMAND":
    "Commande incomplète. Exécutez le projet '" + PROJECT_SHORT_NAME + "' suivi de la commande 'help' pour afficher l'aide.",
  "PATHNOTFOLDERRUNCOMMAND":
    "Le chemin spécifié n'est pas un dossier et ne peut pas être utilisé pour exécuter la commande actuelle. Le chemin actuel sera utilisé à la place.",
  "CONFIRMOVERWRITEPROJECT":
    "Le projet existe déjà.\nVoulez-vous continuer ? (o/n) : ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "Vous n'avez pas l'autorisation d'écraser ou de supprimer le dossier du projet",
  "INVALIDPROJECTNAME":
    "Le nom du dossier du projet ne doit pas contenir d'extensions de fichier.",
  "INVALIDTEMPLATENAME":
    "Le nom du dossier de modèle ne peut pas contenir d'extension de fichier.",
  "TEMPLATENOTFOUND":
    "Le dossier de modèles est introuvable.",
  "FOLDERPROJECTNAME":
    "Dossier du projet",
  "CREATINGPROJECTFILES":
    "Création de la structure du projet",
  "DONE":
    "Terminé.", 
  "CONFIRMDELETEPROJECT":
    "Supprimer le projet.\nVoulez-vous continuer ? (o/n) : ",
  "PROJECTFOLDERNOTFOUND":
    "Projet introuvable",
  "FOLDERPROJECTNAMENOTFOUND":
    "Projet introuvable",
  "PROJECTFILENOTFOUND":
    "Fichier de projet introuvable",
  "FILENOTFOUND":
    "Fichier introuvable",
  "INVALIDCONFIGURATIONLINE":
    "Ligne invalide dans le fichier de configuration",
  "EMPTYCONFIGURATIONKEY":
    "Clé vide dans le fichier de configuration",
  "DUPLICATECONFIGURATIONKEY":
    "Clé en double dans le fichier de configuration",
  "CONFIRMOVERWRITEPAGE":
    "Certains fichiers existent déjà et seront écrasés.\nVoulez-vous continuer ? (o/n) : ",
  "CREATINGPAGEFILES":
    "Création de fichiers supplémentaires",
  "ADDPAGECOMMAND":
    "Ajoute les fichiers requis pour créer une nouvelle page dans le projet spécifié",
  "INVALIDPAGENAME":
    "Le nom de la page à ajouter au projet ne doit pas contenir d'extensions de fichier.",
  "UNKNOWNLANGUAGE":
    "Langue inconnue.",
  "ALREADYERRORSFOUND":
    "Erreurs trouvées pendant l'exécution, veuillez vérifier votre fichier de débogage.",
  "INVALIDID":
    "ID de traduction invalide"
}
