# Bilişim Dersi 10. Sınıf 1. Dönem 1. Yazılı Notları


# 1) Python nedir?
#Guido van Rossum tarafından geliştirilmeye başlanmıştır.
#1990'lı yılların başında ortaya çıkmıştır.
#Özgür ve ücretsiz bir programlama dilidir.
#Web, masaüstü, oyun ve ağ uygulamalarında kullanılabilir.


# 2) Veri Türleri
#string (str) --> metinsel veri --> "merhaba", "10"
#integer (int) --> tam sayı --> 10, -5
#float (float) --> ondalıklı sayı --> 3.14, -12.5
#boolean (bool) --> mantıksal veri --> True, False

#NOT: String ifadeler tek, çift veya üç tırnakla yazılabilir.


# 3) Veri Dönüşümleri
#str() --> String'e dönüştürür.
#int() --> Tam sayıya dönüştürür.
#float() --> Ondalıklı sayıya dönüştürür.
#bool() --> True veya False döndürür.


# 4) Değişkenler & Sabitler
#Değişkenlere değer atamak için "=" kullanılır.
#Sabit: Değeri değişmeyen veridir.
#Değişken: Değeri değişebilen veridir.


# 5) Değişken İsimlendirme Kuralları
#1. Sayıyla başlayamaz.
#2. Boşluk içeremez.
#3. "_" hariç özel karakter içeremez.
#4. Python'un özel anahtar kelimeleri kullanılamaz.
#5. Türkçe karakter kullanmaktan kaçınılmalıdır.


# 6) Aritmetik Operatörler
#"+" --> Toplama, "-" --> Çıkarma, "*" --> Çarpma, "/" --> Bölme
#"//" --> Tam Bölme, "%" --> Kalan, "**" --> Üs Alma


# 7) Karşılaştırma Operatörleri
#"==" --> Eşittir.
#"!=" --> Eşit değildir.
#">" --> Büyüktür.
#"<" --> Küçüktür.
#">=" --> Büyük veya eşittir.
#"<=" --> Küçük veya eşittir.
#"is" --> Nesne kimliği aynıdır.
#"is not" --> Nesne kimliği farklıdır.
#"in" --> İçerisinde bulunuyor mu?
#"not in" --> İçerisinde bulunmuyor mu?

#NOT: "=" değer atar, "==" eşitlik kontrolü yapar.


# 8) Mantıksal Operatörler
#"and" --> ve, "or" --> veya, "not" --> değil

#and: İki koşulun da True olması gerekir.
#or: Koşullardan en az birinin True olması yeterlidir.
#not: Sonucu tersine çevirir.


# 9) İşlem Önceliği
#1. Patantez --> "()"
#2. Üs Alma --> "**"
#3. Çarpma --> "*", Bölme --> "/", Tam Bölme --> "//", Mod --> "%"
#4. Toplma --> "+", Çıkarma --> "-"

#Aynı seviyedeki işlemler genellikle soldan sağa yapılır.


# 10) Ek Fonksiyonlar
#pow(): Üs Alma İşlemi
print(pow(3, 2))     #9
print(pow(5, 3))     #125
print(pow(6, 2, 7))  #1
#NOT: Üçüncü parametre verilirse üs alma işleminden sonra mod alınır.
# pow(taban, üs, mod)

# round(): Yuvarlama İşlemi
round(3.4)      # 3
round(3.7)      # 4
round(24.5)     # 24
round(25.5)     # 26
#Tam 0.5 durumlarında en yakın çift sayıya yuvarlama kuralını kullanır.
