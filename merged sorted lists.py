def merged_lists(List_1, List_2):
    merged_sorted_list = []
    i, j = 0, 0
    while i < len(List_1) and j < len(List_2):
        if List_1[i] <= List_2[j]:
            merged_sorted_list.append(List_1[i])
            i += 1
        else:
            merged_sorted_list.append(List_2[j])
            j += 1
    merged_sorted_list.extend(List_1[i:])
    merged_sorted_list.extend(List_2[j:])
    return merged_sorted_list
List_1 = eval(input("Enter list 1 elements: "))
List_2 = eval(input("Enter list 2 elements: "))
print("Merged lists:", merged_lists(List_1, List_2))
