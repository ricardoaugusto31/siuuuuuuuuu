kalimat = str(input("Ketikan kalimat anda: "))
kata = str(input("Kata yang dihitung frekuensinya: "))

def frekuensi_kata(a, b):
    a = a.lower()
    count = a.count(b.lower())
    return count

print("Kata", "'",kata,"'", "muncul", frekuensi_kata(kalimat, kata), "kali")