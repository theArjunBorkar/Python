def factorial(num):
    if num == 0:
        return 1
    result = factorial(num - 1)
    for i in range(1, num + 1):
        result *= i
    return result
num = int(input("Enter a number: "))
print("Result:", factorial(num))
