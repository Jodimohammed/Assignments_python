#a python to do list that a user can add view remove tasks from
#note the tasks are not saved in a db. its for one time use only..

todo_list = []

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"'{task}' has been added to the to-do list.")
    elif choice == '2':
        if not todo_list:
            print("No tasks to remove.")
        else:
            print("Tasks in the To-Do list:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            if 0 <= task_index < len(todo_list):
                removed_task = todo_list.pop(task_index)
                print(f"'{removed_task}' has been removed from the to-do list.")
            else:
                print("Invalid index.")
    elif choice == '3':
        if not todo_list:
            print("No tasks.")
        else:
            print("Tasks in the To-Do list:")
            for task in todo_list:
                print(f"- {task}")
    elif choice == '4':
        print("Exiting the to-do list.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
