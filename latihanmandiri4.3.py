c_f = lambda celsius: (9/5 * celsius) +32
c_r = lambda celsius: 0.8 * celsius

celsius = 100
print(f"{celsius} C = {c_f(celsius)} F")

celsius = 80
print(f"{celsius} C = {c_r(celsius)} R")

celsius = 0
print(f"{celsius} C = {c_f(celsius)} F")