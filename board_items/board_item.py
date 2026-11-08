from board_items.item_status import ItemStatus
from datetime import date
from event_log import EventLog

class BoardItem:
    def __init__(self, title: str, dueDate: date, status=ItemStatus.OPEN):
        
        self._history = []
        self.title = title
        self.dueDate = dueDate
        self._status = status

        self.add_event(f"{self.__class__.__name__} created: {self.title}")
        
    @property
    def status(self):
        return self._status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):

        if not 5 <= len(value) <= 30:
            raise ValueError("Title must be between 5 and 30 characters.")

        if hasattr(self, "_title"):
            previousTitle = self._title
            self._title = value
            self.add_event(
                 f"Title changed from {previousTitle} to {value}"
            ) 
        else:   
            self._title = value
        

    @property
    def dueDate(self):
        return self._dueDate

    @dueDate.setter
    def dueDate(self, value):

        if value < date.today():
            raise ValueError("Due date cannot be in the past.")
        
        if hasattr(self, "_dueDate"):
            previousDate = self._dueDate
            self._dueDate = value

            self.add_event(
                f"DueDate changed from {previousDate} to {value}"
            )
        else:
            self._dueDate = value
        
    
    def history(self):
        result = []

        for event in self._history:
            result.append(event.info())

        return "\n".join(result)

    def advance_status(self):
        previousStatus = self.status
        nextStatus = ItemStatus.get_next(previousStatus)

        if nextStatus == previousStatus:
            self.add_event(
                f"Cant change status, already at {previousStatus}"
            )
        else:
            self._status = nextStatus
            self.add_event(
                f"Status changed from {previousStatus} to {nextStatus}"
            )

    def revert_status(self):
        previousStatus = self.status
        nextStatus = ItemStatus.get_previous(previousStatus)

        if nextStatus == previousStatus:
            self.add_event(
                f"Cant change status, already at {previousStatus}"
            )
        else:
            self._status = nextStatus
            self.add_event(
                f"Status changed from {previousStatus} to {nextStatus}"
            )

    def info(self):
        return f"{self.title}, [{self.status} | {self.dueDate}]"

    def add_event(self, description):
        self._history.append(EventLog(description))

