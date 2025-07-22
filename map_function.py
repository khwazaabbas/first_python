'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for num in list1:
    list2.append(num ** 3)
print(list2)





list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def cube(num):
    return num**3
list4 = list(map(cube, list3))
print(list4)


'''


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(number):
    return number * number
sqrt_numbers = list(map(square, numbers))
print(sqrt_numbers)