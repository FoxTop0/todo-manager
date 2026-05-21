import json
import os

class TaskStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
        return True
    
    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def delete_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
