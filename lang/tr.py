# Awtly - php transpiller util
# Original file name: ru.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

from constants import PROJECT_SHORT_NAME

# Generic Turkish translation file
MESSAGES = {
  "INVALIDPARAMSNUMBER":
    "Geçersiz parametre sayısı",
  "UNKNOWNCOMMAND":
    "Bilinmeyen komut",
  "NEWCOMMAND":
    "Mevcut klasörde veya belirtilen yolda bir proje oluşturur.",
  "DELETECOMMAND":
    "Mevcut klasörden veya belirtilen yoldan bir projeyi siler.",
  "BUILDCOMMAND":
    "Mevcut klasörde veya belirtilen yolda bir projeyi PHP'ye derler.",
  "VERSION":
    PROJECT_SHORT_NAME + " uygulamasının mevcut sürümünü gösterir.",
  "INCOMPLETECOMMAND":
    "Eksik komut. Yardımı görüntülemek için '" + PROJECT_SHORT_NAME + "' projesini çalıştırın ve ardından 'help' komutunu ekleyin.",
  "PATHNOTFOLDERRUNCOMMAND":
    "Belirtilen yol bir klasör değil ve mevcut komutu yürütmek için kullanılamaz. Bunun yerine mevcut yol kullanılacaktır.",
  "CONFIRMOVERWRITEPROJECT":
    "Proje zaten mevcut.\nDevam etmek istiyor musunuz? (e/h): ",
  "NOGRATSTOOVERWRITEORDELETEFOLDER":
    "Proje klasörünün üzerine yazma veya klasörü silme izniniz yok",
  "INVALIDPROJECTNAME":
    "Proje klasörü adı dosya uzantıları içermemelidir.",
  "INVALIDTEMPLATENAME":
    "Şablon klasörü adı dosya uzantısı içeremez.",
  "TEMPLATENOTFOUND":
    "Şablon klasörü bulunamadı.",
  "FOLDERPROJECTNAME":
    "Proje klasörü",
  "CREATINGPROJECTFILES":
    "Proje yapısı oluşturuluyor",
  "DONE":
    "Tamamlandı.", 
  "CONFIRMDELETEPROJECT":
    "Projeyi sil.\nDevam etmek istiyor musunuz? (e/h): ",
  "PROJECTFOLDERNOTFOUND":
    "Proje bulunamadı",
  "FOLDERPROJECTNAMENOTFOUND":
    "Proje bulunamadı",
  "CONFIRMOVERWRITEPAGE":
    "Bazı dosyalar zaten mevcut ve üzerlerine yazılacak.\nDevam etmek istiyor musunuz? (e/h): ",
  "CREATINGPAGEFILES":
    "Ek dosyalar oluşturuluyor",
  "ADDPAGECOMMAND":
    "Belirtilen projede yeni bir sayfa oluşturmak için gerekli olan dosyaları ekler",
  "INVALIDPAGENAME":
    "Projeye eklenecek sayfanın adı dosya uzantıları içermemelidir.",
  "INVALIDID":
    "Geçersiz çeviri kimliği"
}
