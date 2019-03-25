"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
output1 = a[slice(1,2)]
print(output1[0])

# Output the second-to-last element: 9
length = len(a)
output2 = a[slice(length-2,length-1)]
print(output2[0])

# Output the last three elements in the array: [7, 9, 6]
output3 = a[slice(length-3,length)]
print(output3)

# Output the two middle elements in the array: [1, 7]
output4 = a[slice(2,4)]
print(output4)

# Output every element except the first one: [4, 1, 7, 9, 6]
output5 = a[slice(1,length)]
print(output5)

# Output every element except the last one: [2, 4, 1, 7, 9]
output6 = a[slice(length-1)]
print(output6)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"'
output7 = s[slice(7,12)]
print(output7)