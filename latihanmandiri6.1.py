def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n = int(input("Masukkan bilangan: "))

# cari bilangan prima terdekat < n
i = n - 1
while i > 1:
    if is_prime(i):
        print("Bilangan prima terdekat dari", n, "adalah", i)
        break
    i -= 1
else:
    print("Tidak ada bilangan prima terdekat dari", n)



