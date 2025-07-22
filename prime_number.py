number = int(input("enter the number :  "))
if number <= 1:
    print(" not prime number")
else:
    for i in range(2, number):
        if number %i == 0:
            print("this number is not prime")
            break
    else:
        print(" this number is prime")