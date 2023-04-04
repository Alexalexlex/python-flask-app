class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        task_id = len(self.tasks) + 1
        new_task = {
            "id": task_id,
            "task": task,
        }
        self.tasks.append(new_task)
        return new_task

    def list_tasks(self):
        return self.tasks
