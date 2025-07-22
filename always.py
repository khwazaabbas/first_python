def recursive_function(number):
    starting_num = 0
    if number <= 0:
        return "please try with positive number"
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return recursive_function(number - 1) + recursive_function(number - 2)

number = int(input("enter the number : "))
print("fibonacci number are :", recursive_function(number))

