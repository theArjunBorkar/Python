string = input("Enter a string: ")
temp = ""
for i in string:
    temp = i + temp
print(temp)
if temp == string:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")
