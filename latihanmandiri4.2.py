def cek_digit_belakang(x, y, z):
    return (x %10 == y %10) or (x%10 == z%10) or (y%10 == z%10)

print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))