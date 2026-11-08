# BoardR

A small task-management system written in Python, built to practise
object-oriented programming. Part of my training with Telerik Academy.

## What it does

- Tasks and issues with a title, due date, status and a full event history
- Users with a validated username and email, and a limit of 3 active tasks each
- A board that keeps its users, calculates the team's free capacity
  and reassigns tasks between users
- Two kinds of boards: one that can only add items, and one that can add and remove

## OOP concepts used

- Classes, inheritance and `super()` (`BoardItem` -> `Task`, `Issue`)
- Properties with validation (getters and setters)
- Composition: a `Task` has a `User` as its assignee
- Multiple inheritance with small building blocks
  (`ReadonlyBoard` = `Board` + `CanAddItem`,
  `EditableBoard` = `Board` + `CanAddItem` + `CanRemoveItem`)
- Custom `__str__` and error handling with `ValueError`

## How to run

Requires Python 3.

    python main.py

`main.py` runs a demo that creates users, tasks and boards and prints the results.

## Project structure

    board/          Board, CanAddItem, CanRemoveItem, ReadonlyBoard, EditableBoard
    board_items/    BoardItem, Task, Issue, ItemStatus
    user/           User
    event_log.py    EventLog
    main.py         demo

## Status

A learning project. Next steps: unit tests.