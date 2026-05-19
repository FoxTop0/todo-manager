def main():
    print("=" * 40)
    print("Todo List Manager")
    print("=" * 40)
    print("1. Add task")
    print("2. Exit")
    
    choice = input("Choose: ")
    if choice == "1":
        title = input("Task title: ")
        print(f"Task '{title}' added!")

if __name__ == "__main__":
    main()
