#python program to check if all elements in a list are the same 

def all_elements_same(lst):
    return all(elem == lst[0] for elem in lst)



list1 = [3, 3, 3, 3, 3]
list2 = [1, 2, 3, 4, 5]

print(f"Are all elements in list1 the same? {all_elements_same(list1)}")
print(f"Are all elements in list2 the same? {all_elements_same(list2)}")
