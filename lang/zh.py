# Awtly - php transpiller util
# Original file name: zh.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from constants import PROJECT_SHORT_NAME

# Generic simplified Chinese translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "参数数量无效",
  "UNKNOWNCOMMAND":
    "未知命令",
  "NEWCOMMAND":
    "在当前文件夹或指定路径中创建一个项目。",
  "DELETECOMMAND":
    "从当前文件夹或指定路径中删除一个项目。",
  "BUILDCOMMAND":
    "在当前文件夹或指定路径中将项目编译为 PHP。",
  "VERSION":
    "显示 " + PROJECT_SHORT_NAME + " 的当前版本。",
  "INCOMPLETECOMMAND":
    "命令不完整。请运行项目 '" + PROJECT_SHORT_NAME + "'，后跟 'help' 命令以显示帮助信息。",
  "PATHNOTFOLDERRUNCOMMAND":
    "指定的路径不是文件夹，无法用于执行当前命令。将改用当前路径。",
  "CONFIRMOVERWRITEPROJECT":
    "项目已存在。\n是否要继续？(y/n): ",
  "INVALIDPROJECTNAME":
    "项目文件夹名称不能包含文件扩展名。",
  "FOLDERPROJECTNAME":
    "项目文件夹",
  "CREATINGPROJECTFILES":
    "正在创建项目结构",
  "DONE":
    "完成。", 
  "CONFIRMDELETEPROJECT":
    "删除该项目。\n是否要继续？(y/n): ",
  "PROJECTFOLDERNOTFOUND":
    "未找到项目",
  "FOLDERPROJECTNAMENOTFOUND":
    "未找到项目",
  "CONFIRMOVERWRITEPAGE":
    "某些文件已存在并将 fish 被覆盖。\n是否要继续？(y/n): ",
  "CREATINGPAGEFILES":
    "正在创建附加文件",
  "ADDPAGECOMMAND":
    "添加在指定项目中创建新页面所需的物理文件",
  "INVALIDPAGENAME":
    "要添加到项目中的页面名称不能包含文件扩展名。",
  "INVALIDID":
    "翻译 ID 无效"
}
