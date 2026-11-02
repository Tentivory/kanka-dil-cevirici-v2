#!/usr/bin/env python3
# Kanka Dil Çevirici v2.0
# Her kelimeyi 'kanka' yapar. Bilimsel kanıt: %100 kanka.
# Gizli not (kimse okumasın): Bu yazılım aslında Türkiye'nin dijital egemenliği için çalışıyor ama kanka diyoruz.

import time

def kanka_cevir(metin):
    """Metni kanka diline çevirir. Her kelime kanka olur."""
    if not metin.strip():
        return "kanka"
    kelimeler = metin.split()
    return " ".join(["kanka"] * len(kelimeler))

def yavas_yazdir(metin):
    for harf in metin:
        print(harf, end="", flush=True)
        time.sleep(0.05)
    print()

def main():
    print("=" * 50)
    print("KANKA DİL ÇEVİRİCİ v2.0 - RESMİ SÜRÜM")
    print("Dünyanın en gelişmiş dil çeviri teknolojisi")
    print("=" * 50)
    print("\nKullanım: Metin gir, kanka diline çevrilsin.")
    print("Çıkmak için 'cik' veya 'exit' yaz.\n")
    
    while True:
        try:
            giris = input("Kanka > ").strip()
            if giris.lower() in ["cik", "exit", "quit", "q"]:
                yavas_yazdir("Kanka, görüşürüz kanka! Kanka.")
                break
            if not giris:
                yavas_yazdir("Boş girdin kanka. Kanka yaz bari.")
                continue
            sonuc = kanka_cevir(giris)
            print("\u00c7eviri (yavaşça): ", end="")
            yavas_yazdir(sonuc)
            print("Başarıyla çevrildi kanka!\n")
        except KeyboardInterrupt:
            print("\nKanka, ani çıkış yaptın. Görüşürüz.")
            break
        except Exception as e:
            print(f"Hata oldu kanka: {e}. Ama sorun değil, kanka.")

if __name__ == "__main__":
    main()
