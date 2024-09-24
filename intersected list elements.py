list_1 = eval(input("Enter list 1 elements: "))
list_2 = eval(input("Enter list 2 elements: "))
print("Intersected elements:")
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i] == list_2[j]:
            print(list_1[i])
