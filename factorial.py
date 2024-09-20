num = int(input("Enter any number: "))
i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial of", num, "is", fact)
