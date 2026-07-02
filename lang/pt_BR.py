# Awtly - php transpiller util
# Original file name: pt_BR.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from constants import PROJECT_SHORT_NAME

# Brazil translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Número de parâmetros inválido",
  "UNKNOWNCOMMAND":
    "Comando desconhecido",
  "NEWCOMMAND":
    "Cria um projeto na pasta atual ou no caminho especificado.",
  "DELETECOMMAND":
    "Exclui um projeto da pasta atual ou do caminho especificado.",
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
  "INVALIDPROJECTNAME":
    "O nome da pasta do projeto não deve conter extensões de arquivo.",
  "FOLDERPROJECTNAME":
    "Pasta do projeto",
  "CREATINGPROJECTFILES":
    "Criando a estrutura do projeto",
  "DONE":
    "Concluído.", 
  "CONFIRMDELETEPROJECT":
    "Excluir o projeto.\nDeseja continuar? (s/n): ",
  "PROJECTFOLDERNOTFOUND":
    "Projeto não encontrado",
  "FOLDERPROJECTNAMENOTFOUND":
    "Projeto não encontrado",
  "CONFIRMOVERWRITEPAGE":
    "Alguns arquivos já existem e serão substituídos.\nDeseja continuar? (s/n): ",
  "CREATINGPAGEFILES":
    "Criando arquivos adicionais",
  "ADDPAGECOMMAND":
    "Adiciona os arquivos necessários para criar uma nova página no projeto especificado",
  "INVALIDPAGENAME":
    "O nome da página a ser adicionada ao projeto não deve conter extensões de arquivo.",
  "INVALIDID":
    "ID de tradução inválido"
}
