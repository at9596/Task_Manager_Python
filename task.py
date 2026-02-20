class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title}"