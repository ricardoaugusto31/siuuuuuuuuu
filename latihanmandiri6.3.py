t = int(input("Masukan tinggi: "))
l = int(input("Masukan lebar: "))
c = 1
for i in range(t):
    for j in range(l):
        print(c, end=" ")
        c += 1
    print("")