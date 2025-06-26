print("\n" + "="*50 + "\n📝 TO-DO LIST MANAGER\n" + "="*50)

todos = []

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        task = input("Enter task to add: ")
        todos.append(task)
        print(f"✅ Added: {task}")
    
    elif choice == "2":
        if not todos:
            print("⚠️ No tasks to remove!")
            continue
            
        print("Current tasks:")
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")
            
        try:
            task_num = int(input("Enter task number to remove: ")) - 1
            removed = todos.pop(task_num)
            print(f"❌ Removed: {removed}")
        except (ValueError, IndexError):
            print("⚠️ Invalid task number!")
    
    elif choice == "3":
        if not todos:
            print("Your to-do list is empty!")
        else:
            print("\nYOUR TASKS:")
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("⚠️ Invalid choice. Please enter 1-4")

# Add-ons to try later:
# 1. Add due dates to tasks
# 2. Save tasks to a file