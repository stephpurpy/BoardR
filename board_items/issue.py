from board_items.item_status import ItemStatus
from datetime import date
from board_items.board_item import BoardItem

class Issue(BoardItem):
    def __init__(self,title: str, description: str, dueDate: date):
        super().__init__(title, dueDate, ItemStatus.OPEN)

        if description.strip():
            self._description = description

        else:
            self._description = "No description"
        
    @property
    def description(self):
        return self._description

    def info(self):
        boardItemInfo = super().info()

        return f"{self.__class__.__name__} ({self.description}) {boardItemInfo}"