#list methode
S = 'mumbai'

# Printing each character and its Unicode code point using a for loop
for char in S:
    print(f"Character '{char}' has Unicode code point: {ord(char)}")

S = 'mumbai'

# Computing the sum of Unicode code points using a loop
unicode_sum = sum(ord(char) for char in S)
print(f"The sum of Unicode code points in '{S}' is: {unicode_sum}")

S = 'mumbai'

# Creating a list of Unicode code points using the list method
unicode_list = list(map(ord, S))
print("List of Unicode code points:", unicode_list)
