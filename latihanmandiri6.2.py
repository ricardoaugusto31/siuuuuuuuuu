n = int(input("n = "))

for i in range(n):
    faktor = 1
    for j in range(n-i):
        faktor = faktor*(j+1)
    print(faktor, end=" ")
    for k in range(n-i, 0, -1):
        print(k, end=" ")
    print()