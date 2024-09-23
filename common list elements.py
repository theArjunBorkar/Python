lst_A = eval(input("Enter list A elements: "))
lst_B = eval(input("Enter list B elemens: "))
print("Common list elements: ")
for i in range(len(lst_A)):
    for j in range(len(lst_B)):
        if lst_A[i] == lst_B[j]:
            print(lst_A[i])
