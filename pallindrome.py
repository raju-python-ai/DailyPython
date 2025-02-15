#using slicing
def is_palindrome(s):
    return s == s[::-1]
word = "madam"
print(is_palindrome(word))  


# #using loop
def is_palindrome(s):
    s = s.lower()  
    return s == "".join(reversed(s))
word = "racecar"
print(is_palindrome(word)) 


#using teo poniter approch
def is_palindrome(s):
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
word = "level"
print(is_palindrome(word))
 

    
    