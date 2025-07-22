num = int(input("Please enter the number for which you want to see the multiplication table =  "))
print("multiplication table of ", num)
count = 1
while count <= 10:
    print(f"{num} x {count} = {num * count}")
    count += 1

print("try with another digit")