x = int(input("Angka pertama: "))
y = int(input("Angka kedua: "))
z = int(input("Angka ketiga: "))

def cek_angka(a, b, c):
    if x != y and x != z and y != z and (x == y+z) or (y == x+z) or (z == x+y):
        return True
    else:
        return False

print(cek_angka(x, y, z)) 


