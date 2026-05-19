import json

class TaskStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)
    
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
