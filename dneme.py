import json
ogrenciler = []
while True:
        ogrenci =  {
        "adi": "",
        "soyadi": "",
        "numarasi": 0,
        "dersler": {
            "matematik": "",
            "fen": "",
        }
    }
        
        yeni_ogrenci = input("Ogrencinin adini giriniz: ")
        ogrenci["adi"] = yeni_ogrenci
        yeni_soyad = input("Soyadini girniz: ")
        ogrenci["soyadi"] = yeni_soyad
        try:
            yeni_numara = int(input("numarayi giriniz: "))
        except ValueError:
            print("Hatali girdiniz.Lutfen sadece sayi giriniz.")
            continue
        ogrenci["numarasi"] = yeni_numara
        try:
            matematik_notu = int(input("Matematik notunu giriniz: "))
        except ValueError:
            print("Hatali girdiniz.Lütfen sayi giriniz.")
            continue
        ogrenci["dersler"]["matematik"] = matematik_notu
        try:
            fen_notu = int(input("Fen notunu giriniz: "))
        except ValueError:
            print("Hatali girdiniz.Lütfen sayi giriniz.")
            continue
        ogrenci["dersler"]["fen"] = fen_notu
        ogrenciler.append(ogrenci)
        devam = input("Yeni ogrenci girmek ister misiniz(e/h): ").lower()
        if devam == 'h':
            break
print("\nKaydedilen Öğrenciler:", ogrenciler)
for ogr in ogrenciler:
    notlar = ogr["dersler"].values()
    ortalama = sum(notlar) /len(notlar)
    if ortalama >= 90:
        harf = 'AA'
    elif ortalama >= 85:
        harf = 'BA'
    elif ortalama >= 80:
        harf = 'BB'
    elif ortalama >= 70:
        harf = 'CB'
    elif ortalama >= 60:
        harf = 'CC'
    elif ortalama >= 50:
        harf = 'DD'
    else:
        harf = 'FF'
    ogr["ortalama"] = ortalama
    ogr["harf_notu"] = harf
def dosyaya_kaydet(veri):
    try:
        with open("ogrenciler.json","w", encoding="utf-8") as dosya:
            json.dump(veri, dosya, indent=4, ensure_ascii=False)
    except (IOError, OSError) as e:
        print(f"Dosyayi kaydetme hatasi olustu!")
        return
dosyaya_kaydet(ogrenciler)
try:
    arananNo = int(input("Aranan ogrenci no:"))
    bulundu = False
    for ogr1 in ogrenciler:
        if ogr1["numarasi"] == arananNo:
            print(
                f"Ogrencinin adi: {ogr1['adi']}\n"
                f"Ogrencinin soyadi: {ogr1['soyadi']}\n"
                f"Ogrencinin numarasi: {ogr1['numarasi']}\n"
                f"Ogrencinin aldigi dersler: {ogr1['dersler']}\n"
                f"Ogrencinin notlari:\n"
                f"Matematik notu: {ogr1['dersler']['matematik']}\n"
                f"Fen notu: {ogr1['dersler']['fen']}\n"
                f"Ogrenci ortalamasi: {ogr1['ortalama']}\n"
                f"Harf notu: {ogr1['harf_notu']}"
            )
            bulundu = True
            break
    if not bulundu:
        print("Lutfen tanimli bir sayi giriniz.")
except ValueError:
    print("Hatali girdiniz.Lütfen sayi giriniz.")
toplamOrtalama = 0
for ogr2 in ogrenciler:
    toplamOrtalama += ogr2["ortalama"]
toplamOrtalama = toplamOrtalama / len(ogrenciler)
print(f"\nSinifin genel ortalamasi: {toplamOrtalama}")
en_basarili = max(ogrenciler, key=lambda x: x["ortalama"])
en_dusuk = min(ogrenciler, key=lambda x: x["ortalama"])
print(f"\nEn basarili ogrenci: {en_basarili}"
      f"\nEn basarisiz ogrenci: {en_dusuk}")