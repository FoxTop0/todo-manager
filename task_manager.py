"""
Модуль управления задачами для Todo List Manager
Разработчик: Dev 3
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
from validator import TaskValidator
from logger import TaskLogger


class TaskManager:
    """Класс для управления задачами"""
    
    def __init__(self, storage):
        self.storage = storage
        self.validator = TaskValidator()
        self.logger = TaskLogger()
        self.tasks = self._load_tasks()
    
    def _load_tasks(self) -> List[Dict[str, Any]]:
        tasks = self.storage.load_tasks()
        for i, task in enumerate(tasks, 1):
            if 'id' not in task:
                task['id'] = i
        return tasks
    
    def _save_tasks(self) -> bool:
        return self.storage.save_tasks(self.tasks)
    
    def _get_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.get('id', 0) for task in self.tasks) + 1
    
    def add_task(self, title: str, description: str = "", 
                 priority: str = "medium", due_date: str = None) -> Optional[int]:
        """Добавляет новую задачу"""
        is_valid, error = self.validator.validate_title(title)
        if not is_valid:
            print(f"Ошибка: {error}")
            return None
        
        task = {
            'id': self._get_next_id(),
            'title': title.strip(),
            'description': description.strip(),
            'priority': priority.lower(),
            'status': 'pending',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'due_date': due_date,
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.tasks.append(task)
        if self._save_tasks():
            return task['id']
        return None
    
    def get_all_tasks(self) -> List[Dict[str, Any]]:
        return self.tasks
    
    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.get('id') == task_id:
                task['status'] = 'completed'
                task['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                return self._save_tasks()
        return False
