from datetime import date, timedelta
from board_items.task import Task
from board_items.issue import Issue
from board_items.board_item import BoardItem
from board_items.item_status import ItemStatus
from board.readonly_board import ReadonlyBoard
from board.editable_board import EditableBoard


def add_days_to_now(days):
    return date.today() + timedelta(days=days)


print("=== Basic items ===")

item = BoardItem(
    "Learn OOP",
    add_days_to_now(5)
)

next_item = ItemStatus.get_next(ItemStatus.IN_PROGRESS)

board = EditableBoard()
steven = board.add_user("Steven", "steven@asd.bg")
peter = board.add_user("Peter", "peter@asd.bg")

task = Task('Test the application flow', steven, add_days_to_now(2))

task.advance_status()
task.advance_status()

task.assignee = peter
print(task.history())

issue = Issue(
    "App flow tests?",
    "We need to test the flow!",
    add_days_to_now(1)
)

# issue.advance_status()
# issue.dueDate += timedelta(days=1)

# print("\n--- Issue history ---")
print(issue.info())

board.add_item(task)
board.add_item(issue)

print("\n--- Board ---")
print(f"Items in board: {board.count}")


print("\n=== Users, capacity and reassigning ===")

board = EditableBoard()
steven = board.add_user("Steven", "steven@asd.bg")
task1 = Task('Test the application flow', steven, add_days_to_now(2))
steven.receive_task(task1)
board.add_item(task1)
print(f"Capacity of the team: {board.team_capacity}")

peter = board.add_user("Peter", "peter@asd.bg")
print(f"Capacity of the team: {board.team_capacity}")     

task2 = Task('Fix authentication', steven, add_days_to_now(2))
board.add_item(task2)
peter.receive_task(task2)
print(f"Capacity of the team: {board.team_capacity}")     

print(task1.status)
steven.advance_task_status(task1)
print(task1.status)

board.reassign_task(task1, peter)
print(f"Steven assigned tasks: {steven.assigned_tasks}")
print(f"Peter assigned tasks: {[t.info() for t in peter.assigned_tasks]}")
print(task1.status)

peter.advance_task_status(task1)
peter.advance_task_status(task1)
print(task1.status)

print(f"Capacity of the team: {board.team_capacity}")
print(task1.history())


print("\n=== Readonly and editable boards ===")

readonly_board = ReadonlyBoard()
steven = readonly_board.add_user("Steven", "steven@asd.bg")
readonly_task = Task('Dont refactor anything', steven, add_days_to_now(2))

readonly_board.add_item(issue)
readonly_board.add_item(readonly_task)
print(readonly_board.count) 

editable_board = EditableBoard()
editable_board.add_item(issue)
editable_board.remove_item(issue)
print(editable_board.count)