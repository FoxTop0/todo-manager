"""
Точка входа и пользовательский интерфейс Todo List Manager
Разработчик: Dev 1
"""

from storage import TaskStorage
from task_manager import TaskManager
import sys


class TodoApp:
    """Главное приложение Todo List Manager"""
    
    def __init__(self):
        self.storage = TaskStorage()
        self.task_manager = TaskManager(self.storage)
    
    def print_menu(self):
        print("\n" + "=" * 50)
        print("✅ TODO LIST MANAGER".center(50))
        print("=" * 50)
        print("1. ➕ Добавить задачу")
        print("2. 📋 Показать все задачи")
        print("3. ✅ Отметить задачу как выполненную")
        print("0. 🚪 Выход")
        print("-" * 50)
    
    def add_task_flow(self):
        print("\n--- ДОБАВЛЕНИЕ ЗАДАЧИ ---")
        title = input("Введите название: ").strip()
        if not title:
            print("❌ Ошибка: название не может быть пустым")
            return
        
        task_id = self.task_manager.add_task(title)
        if task_id:
            print(f"✅ Задача добавлена! ID: {task_id}")
        else:
            print("❌ Ошибка при добавлении")
    
    def show_tasks_flow(self):
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("\n📭 Нет задач")
            return
        
        print("\n📋 СПИСОК ЗАДАЧ:")
        for task in tasks:
            status = "✅" if task['status'] == 'completed' else "⏳"
            print(f"{status} [{task['id']}] {task['title']}")
    
    def complete_task_flow(self):
        try:
            task_id = int(input("Введите ID задачи: "))
            if self.task_manager.complete_task(task_id):
                print(f"✅ Задача {task_id} выполнена!")
            else:
                print("❌ Задача не найдена")
        except ValueError:
            print("❌ Введите число")
    
    def run(self):
        while True:
            self.print_menu()
            choice = input("\n👉 Выберите действие: ")
            
            if choice == "1":
                self.add_task_flow()
            elif choice == "2":
                self.show_tasks_flow()
            elif choice == "3":
                self.complete_task_flow()
            elif choice == "0":
                print("\n👋 До свидания!")
                sys.exit(0)
            else:
                print("❌ Неверный выбор")
            
            input("\nНажмите Enter...")


if __name__ == "__main__":
    app = TodoApp()
    app.run()
