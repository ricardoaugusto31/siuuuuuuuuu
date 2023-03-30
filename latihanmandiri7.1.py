katapertama = str(input("Kata pertama: "))
katakedua = str(input("Kata kedua: "))

def anagram(a , b):
    a = a.lower()
    b = b.lower()


    urutan_a = sorted(a)
    urutan_b = sorted(b)

    if urutan_a == urutan_b:
        return True
    else:
        return False
print(anagram(katapertama, katakedua))
