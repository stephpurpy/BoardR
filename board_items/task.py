from board_items.item_status import ItemStatus
from datetime import date
from board_items.board_item import BoardItem
from user.user import User

class Task(BoardItem):
    def __init__(self, title: str, assignee: User, dueDate: date):
        super().__init__(title, dueDate, ItemStatus.TODO)
        self.assignee = assignee

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):

        if not isinstance(value, User):
            raise ValueError("Assignee must be a User.")
        
        if hasattr(self, "_assignee"):
            previousAssignee = self._assignee
            self._assignee = value
            self.add_event(

                 f"Assignee changed from {previousAssignee} to {value}"
            ) 
        else:   
            self._assignee = value

    def info(self):
        boardItemInfo = super().info()

        return f"{self.__class__.__name__} (assigned to: {self.assignee}) {boardItemInfo}"