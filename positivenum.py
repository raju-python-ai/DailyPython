#using sum() function
def sum_of_positives(numbers):
    return sum(num for num in numbers if num > 0)

numbers = [-8, -9, -7, -4, -6, -3, 7]
result = sum_of_positives(numbers)
print(result)  

#using loop 
def sum_of_positives(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

numbers = [-8, -9, -7, -4, -6, -3, 7]
result = sum_of_positives(numbers)
print(result)  