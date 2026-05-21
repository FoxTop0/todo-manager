from validator import TaskValidator
from logger import TaskLogger

class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.validator = TaskValidator()
        self.logger = TaskLogger()
        self.tasks = self.storage.load()
    
    def add_task(self, title, priority="medium"):
        is_valid, error = self.validator.validate_title(title)
        if not is_valid:
            self.logger.log_error(error)
            return None
        
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "status": "pending"
        }
        self.tasks.append(task)
        self.storage.save(self.tasks)
        self.logger.log_info(f"Task added: {title}")
        return task
    
    def get_all(self):
        return self.tasks
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                self.storage.save(self.tasks)
                self.logger.log_info(f"Task {task_id} completed")
                return True
        return False
