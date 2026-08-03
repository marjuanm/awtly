# Awtly - php transpiller util
# Original file name: ar.py
# Copyright (c) 2026 Juan Manuel Mar Hdz. / Awtly & Contributors
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from common.constants import PROJECT_SHORT_NAME

# Generic Arab translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "عدد المعلمات غير صالح",
  "UNKNOWNCOMMAND":
    "أمر غير معروف",
  "NEWCOMMAND":
    "ينشئ مشروعًا في المجلد الحالي أو المسار المحدد.",
  "DELETECOMMAND":
    "يحذف مشروعًا من المجلد الحالي أو المسار المحدد.",
  "BUILDCOMMAND":
    "يجمع مشروعًا إلى PHP في المجلد الحالي أو المسار المحدد.",
  "VERSION":
    "يعرض الإصدار الحالي لـ " + PROJECT_SHORT_NAME + ".",
  "INCOMPLETECOMMAND":
    "أمر غير مكتمل. قم بتشغيل المشروع '" + PROJECT_SHORT_NAME + "' متبوعًا بأمر 'help' لعرض المساعدة.",
  "PATHNOTFOLDERRUNCOMMAND":
    "المسار المحدد ليس مجلدًا ولا يمكن استخدامه لتنفيذ الأمر الحالي. سيتم استخدام المسار الحالي بدلاً من ذلك.",
  "CONFIRMOVERWRITEPROJECT":
    "المشروع موجود بالفعل.\nهل تريد الاستمرار؟ (y/n): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "لا تملك أذونات الكتابة فوق مجلد المشروع أو حذفه",
  "INVALIDPROJECTNAME":
    "يجب ألا يحتوي اسم مجلد المشروع على امتدادات ملفات.",
  "INVALIDTEMPLATENAME":
    "يجب ألا يحتوي اسم مجلد القالب على امتدادات ملفات.", 
  "TEMPLATENOTFOUND":
    "لم يتم العثور على مجلد القوالب.",
  "FOLDERPROJECTNAME":
    "مجلد المشروع",
  "CREATINGPROJECTFILES":
    "جاري إنشاء بنية المشروع",
  "DONE":
    "تم.", 
  "CONFIRMDELETEPROJECT":
    "حذف المشروع.\nهل تريد الاستمرار؟ (y/n): ",
  "PROJECTFOLDERNOTFOUND":
    "المشروع غير موجود",
  "FOLDERPROJECTNAMENOTFOUND":
    "المشروع غير موجود",
  "PROJECTFILENOTFOUND":
    "ملف المشروع غير موجود",
  "FILENOTFOUND":
    "مفتاح مكرر في ملف الإعدادات",
  "INVALIDCONFIGURATIONLINE":  
    "الملف غير موجود",
  "EMPTYCONFIGURATIONKEY":  
    "سطر غير صالح في ملف الإعدادات",
  "DUPLICATECONFIGURATIONKEY":  
    "مفتاح فارغ في ملف الإعدادات",
  "CONFIRMOVERWRITEPAGE":
    "بعض الملفات موجودة بالفعل وسيتم استبدالها.\nهل تريد الاستمرار؟ (y/n): ",
  "CREATINGPAGEFILES":
    "جاري إنشاء ملفات إضافية",
  "ADDPAGECOMMAND":
    "يضيف الملفات المطلوبة لإنشاء صفحة جديدة في المشروع المحدد",
  "INVALIDPAGENAME":
    "يجب ألا يحتوي اسم الصفحة المراد إضافتها إلى المشروع على امتدادات ملفات.",
  "UNKNOWNLANGUAGE": 
    "لغة غير معروفة.",
  "ALREADYERRORSFOUND":
    "تم العثور على أخطاء أثناء التنفيذ، يرجى مراجعة ملف التصحيح الخاص بك.",
  "INVALIDID":
    "معرف ترجمة غير صالح"
}
