kalimat = str(input("Masukan kalimat: "))
def panjangkata(kalimat):
    kata = kalimat.split()
    kataterpendek = min(kata, key=len)
    kataterpanjang = max(kata, key=len)
    return kataterpendek, kataterpanjang

kataterpendek, kataterpanjang = panjangkata(kalimat)
print("terpendek =", kataterpendek, ",", "terpanjang =", kataterpanjang)