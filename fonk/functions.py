def dosya_ac(dosya_ad="kadro.txt"):
    """ Kadro dosyasını açmaya yarar. """
    with open(dosya_ad, 'r') as dosya_local:
        kadro_local = dosya_local.readlines()
    return kadro_local

def dosya_yaz(eklenecek,dosya_adi="kadro.txt"):
    with open(dosya_adi, 'w') as dosya:
        dosya.writelines(eklenecek)


if __name__ == "__main__":
    print("Çet noluyoooo")
