class ItemStatus:
    OPEN = "Open"
    TODO = "ToDo"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    VERIFIED = "Verified"

    STATUSES = [
        OPEN,
        TODO,
        IN_PROGRESS,
        DONE,
        VERIFIED
    ]

    @classmethod
    def get_next(cls, current):
        currentIndex = cls.STATUSES.index(current)


        if currentIndex == len(cls.STATUSES) - 1:
            return current

        return cls.STATUSES[currentIndex + 1]
    
    @classmethod
    def get_previous(cls, current):
        currentIndex = cls.STATUSES.index(current)

        if currentIndex == 0:
            return current

        return cls.STATUSES[currentIndex - 1]

