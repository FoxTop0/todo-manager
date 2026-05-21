from storage import TaskStorage
from task_manager import TaskManager

class TodoApp:
    def __init__(self):
        self.storage = TaskStorage()
        self.manager = TaskManager(self.storage)
    
    def run(self):
        while True:
            print("\n=== TODO LIST MANAGER ===")
            print("1. Add task")
            print("2. Show all tasks")
            print("3. Complete task")
            print("0. Exit")
            
            choice = input("Choose: ")
            
            if choice == "1":
                title = input("Title: ")
                task = self.manager.add_task(title)
                if task:
                    print(f"✅ Task added! ID: {task['id']}")
            
            elif choice == "2":
                tasks = self.manager.get_all()
                if not tasks:
                    print("No tasks")
                for t in tasks:
                    status = "✅" if t['status'] == "completed" else "⏳"
                    print(f"{status} [{t['id']}] {t['title']}")
            
            elif choice == "3":
                task_id = int(input("Task ID: "))
                if self.manager.complete_task(task_id):
                    print("✅ Task completed!")
            
            elif choice == "0":
                print("Goodbye!")
                break

if __name__ == "__main__":
    app = TodoApp()
    app.run()
