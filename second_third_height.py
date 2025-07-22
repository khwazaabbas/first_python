def find_second_third_highest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 3:
        print("Nothhjuiu enough unique numbers in the list.")
        return
    unique_numbers.sort(reverse=True)
    second_highest = unique_numbers[1]
    third_highest = unique_numbers[2]
    print("Second highest number:", second_highest)
    print("Third highest number:", third_highest)
numbers = list(map(int,input("enter the list number seperated by the spaces : ").split()))
find_second_third_highest(numbers)