# Swapping without a temporary variable
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
a, b = b, a  
print("After swapping: a =", a, ", b =", b)

# Swapping using a temporary variable
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, ", b =", b)
