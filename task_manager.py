class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title):
        task = {"id": len(self.tasks) + 1, "title": title, "done": False}
        self.tasks.append(task)
        return task
    
    def get_all(self):
        return self.tasks
