from datetime import datetime

class EventLog:
    def __init__(self, description: str):
        if not description.strip():
            raise ValueError("Description cannot be empty")

        self._description = description
        self._timestamp = datetime.now()


    @property
    def description(self):
        return self._description
    @property
    def timestamp(self):
        return self._timestamp
  
    def info(self):
        formatedTime = self.timestamp.strftime(
            "%m/%d/%Y, %H:%M:%S"
        )

        return f"[{formatedTime}] {self.description}"