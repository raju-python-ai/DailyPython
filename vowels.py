def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

input_string=input("Enter the Word:")
print("Number of vowels:", count_vowels(input_string))
