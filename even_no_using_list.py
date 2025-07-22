def get_even_numbers(input_list):
    even_list = []
    for num in input_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

user_input = input("Enter numbers separated by spaces: ")
number_list = list(map(int, user_input.split()))
even_numbers = get_even_numbers(number_list)
print("Even numbers:", even_numbers)