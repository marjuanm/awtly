# Awtly - php transpiller util
# Original file name: ru.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from constants import PROJECT_SHORT_NAME

# Generic Russian translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Неверное количество параметров",
  "UNKNOWNCOMMAND":
    "Неизвестная команда",
  "NEWCOMMAND":
    "Создает проект в текущей папке или по указанному пути.",
  "DELETECOMMAND":
    "Удаляет проект из текущей папки или по указанному пути.",
  "BUILDCOMMAND":
    "Компилирует проект в PHP в текущей папке или по указанному пути.",
  "VERSION":
    "Показывает текущую версию " + PROJECT_SHORT_NAME + ".",
  "INCOMPLETECOMMAND":
    "Неполная команда. Запустите проект '" + PROJECT_SHORT_NAME + "' с последующей командой 'help' для отображения справки.",
  "PATHNOTFOLDERRUNCOMMAND":
    "Указанный путь не является папкой и не может быть использован для выполнения текущей команды. Вместо этого будет использован текущий путь.",
  "CONFIRMOVERWRITEPROJECT":
    "Проект уже существует.\nХотите продолжить? (y/n): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "У вас нет прав на перезапись или удаление папки проекта",
  "INVALIDPROJECTNAME":
    "Имя папки проекта не должно содержать расширений файлов.",
  "INVALIDTEMPLATENAME":
    "Имя папки шаблона не может содержать расширение файла.",
  "TEMPLATENOTFOUND":
    "Папка шаблонов не найдена.",
  "FOLDERPROJECTNAME":
    "Папка проекта",
  "CREATINGPROJECTFILES":
    "Создание структуры проекта",
  "DONE":
    "Готово.", 
  "CONFIRMDELETEPROJECT":
    "Удалить проект.\nХотите продолжить? (y/n): ",
  "PROJECTFOLDERNOTFOUND":
    "Проект не найден",
  "FOLDERPROJECTNAMENOTFOUND":
    "Проект не найден",
  "CONFIRMOVERWRITEPAGE":
    "Некоторые файлы уже существуют и будут перезаписаны.\nХотите продолжить? (y/n): ",
  "CREATINGPAGEFILES":
    "Создание дополнительных файлов",
  "ADDPAGECOMMAND":
    "Добавляет файлы, необходимые для создания новой страницы в указанном проекте",
  "INVALIDPAGENAME":
    "Имя добавляемой в проект страницы не должно содержать расширений файлов.",
  "INVALIDID":
    "Неверный ID перевода"
}
