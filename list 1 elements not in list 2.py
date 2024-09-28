def unique_elements(list_1, list_2):
    unique_list = []
    for i in range(len(list_1)):
        if list_1[i] not in list_2:
            unique_list.append(list_1[i])
    return unique_list
list_1 = eval(input("Enter list 1 elements: "))
list_2 = eval(input("Enter list 2 elements: "))
print("Elements that are in list 1 but not in list 2 are:", unique_elements(list_1, list_2))
