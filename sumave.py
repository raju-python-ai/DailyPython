def sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) 
    return total, average
numbers = [10, 20, 30, 40, 50]
total, avg = sum_and_average(numbers)
print(f"Sum: {total}, Average: {avg}")
