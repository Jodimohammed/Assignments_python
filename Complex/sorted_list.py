#python program to check if a list is sorted 

def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

my_list = [1, 3, 5, 7, 9]
print(f"Is the list sorted in ascending order? {is_sorted_ascending(my_list)}")
