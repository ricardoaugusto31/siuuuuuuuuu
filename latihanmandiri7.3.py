kalimatrusak = str(input("Masukan kalimat yang spasinya berlebihan: "))

def spasi(kalimat):
    kata = kalimat.split()
    kalimat = " ".join(kata)
    return kalimat
print(spasi(kalimatrusak))