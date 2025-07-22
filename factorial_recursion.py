def factorial(x):
    if x == 0 or x ==1:
        return 1
    else:
        return (x * factorial(x-1))
num = int(input("enter a number  :  "))
result = factorial(num)
print(f"the factorial of", num, "is", result)