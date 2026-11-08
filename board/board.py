from user.user import User
from board_items.item_status import ItemStatus

class Board:
    def __init__(self):
        self._items = []
        self._users = []

    @property
    def count(self):
        return len(self._items)

    def add_user(self, username, email):
        for user in self._users:
            if username == user.username:
                raise ValueError("User with that username already exists.")
        
        new_user = User(username, email)
        self._users.append(new_user)
        return new_user

    @property
    def team_capacity(self):
        total = 0
        for user in self._users:
            total += user.capacity

        return total

    def reassign_task(self, task, new_assignee):
        if task not in self._items:
            raise ValueError("There is no such task on the Board.")

        if new_assignee is task.assignee:
            raise ValueError("It is already assigned to this user.")

        if task.status not in (ItemStatus.TODO, ItemStatus.IN_PROGRESS):
            raise ValueError("Only tasks in ToDo or In Progress can be reassigned.")

        if new_assignee.capacity <= 0:
            raise ValueError("The new assignee has no capacity for more tasks.")
        
        current_assignee = task.assignee
        current_assignee.remove_task(task)

        while task.status != ItemStatus.TODO:
            task.revert_status()

        new_assignee.receive_task(task)
