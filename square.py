def square_elements(lst):
    return [x**2 for x in lst]

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_elements(numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
