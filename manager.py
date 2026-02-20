import json
from task import Task
class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        self.save_tasks()

    def save_tasks(self):
        # Convert objects to dictionaries for JSON compatibility
        data = [{"title": t.title, "completed": t.completed} for t in self.tasks]
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        except FileNotFoundError:
            return []