# Awtly - php transpiller util
# Original file name: pt_PT.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from constants import PROJECT_SHORT_NAME

# Portugal translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Número de parâmetros inválido",
  "UNKNOWNCOMMAND":
    "Comando desconhecido",
  "NEWCOMMAND":
    "Cria um projeto na pasta atual ou no caminho especificado.",
  "DELETECOMMAND":
    "Elimina um projeto da pasta atual ou do caminho especificado.",
  "BUILDCOMMAND":
    "Compila um projeto para PHP na pasta atual ou no caminho especificado.",
  "VERSION":
    "Mostra a versão atual de " + PROJECT_SHORT_NAME + ".",
  "INCOMPLETECOMMAND":
    "Comando incompleto. Execute o projeto '" + PROJECT_SHORT_NAME + "' seguido do comando 'help' para exibir a ajuda.",
  "PATHNOTFOLDERRUNCOMMAND":
    "O caminho especificado não é uma pasta e não pode ser usado para executar o comando atual. O caminho atual será usado em vez disso.",
  "CONFIRMOVERWRITEPROJECT":
    "O projeto já existe.\nDeseja continuar? (s/n): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "Não tem permissão para sobrescrever ou eliminar a pasta do projeto",
  "INVALIDPROJECTNAME":
    "O nome da pasta do projeto não deve conter extensões de ficheiro.",
  "INVALIDTEMPLATENAME":
    "O nome da pasta do modelo não pode conter uma extensão de ficheiro.",
  "TEMPLATENOTFOUND":
    "A pasta de modelos não foi encontrada.",
  "FOLDERPROJECTNAME":
    "Pasta do projeto",
  "CREATINGPROJECTFILES":
    "A criar a estrutura do projeto",
  "DONE":
    "Concluído.", 
  "CONFIRMDELETEPROJECT":
    "Eliminar o projeto.\nDeseja continuar? (s/n): ",
  "PROJECTFOLDERNOTFOUND":
    "Projeto não encontrado",
  "FOLDERPROJECTNAMENOTFOUND":
    "Projeto não encontrado",
  "CONFIRMOVERWRITEPAGE":
    "Alguns ficheiros já existem e serão substituídos.\nDeseja continuar? (s/n): ",
  "CREATINGPAGEFILES":
    "A criar ficheiros adicionais",
  "ADDPAGECOMMAND":
    "Adiciona os ficheiros necessários para criar uma nova página no projeto especificado",
  "INVALIDPAGENAME":
    "O nome da página a adicionar ao projeto não deve conter extensões de ficheiro.",
  "INVALIDID":
    "ID de tradução inválido"
}
