from board_items.item_status import ItemStatus

class User:

    MAX_ACTIVE_TASKS = 3

    def __init__(self, username, email):

        if not username.strip():
            raise ValueError("You should enter a username!")

        self._username = username
        self.email = email
        self._assigned_tasks = []

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("You should enter a real email address. Example: user@gmail.com")
        
        self._email = value

    @property
    def assigned_tasks(self):
        return tuple(self._assigned_tasks)

    @property
    def capacity(self):
        count = 0
        for task in self._assigned_tasks:
            if task.status in (ItemStatus.TODO, ItemStatus.IN_PROGRESS):
                count += 1

        return self.MAX_ACTIVE_TASKS - count

    def receive_task(self, task):
        if self.capacity <= 0:
            raise ValueError("Reached max active tasks limit.")

        task.assignee = self
        self._assigned_tasks.append(task)

    def remove_task(self, task):
        if task not in self._assigned_tasks:
            raise ValueError("Task is not assigned to this user.")
        
        self._assigned_tasks.remove(task)

    def advance_task_status(self, task):
        if task.assignee is not self:
            raise ValueError("Task is not assigned to this user.")

        if task.status not in (ItemStatus.TODO, ItemStatus.IN_PROGRESS):
            raise ValueError("Only tasks in ToDo or InProgress can be advanced.")

        task.advance_status()

    def __str__(self):
        return self.username