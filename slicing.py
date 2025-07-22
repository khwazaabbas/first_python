x = "khwaza abbas ansari"
print(x[2:5]) # slicing
print(x[ :10]) # slice from the start
print(x[7:]) # slice to the end
txt = """ india is a great country,
my name is xyz,
its to hot,
its too cold
"""
print(len(txt))
for chr in txt:
    print(chr)

y = "  hyderabad is famous for biryani  !!!   "
print(y.strip())

z = "mani ansari"
print(z.upper())

a = "MANI ANSARI"
print(a.lower())

b = "not at all"
print(b.replace("l", "z"))

c = "mani, ansari"
print(c.split(","))

