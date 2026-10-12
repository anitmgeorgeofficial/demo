"""Simple in-memory task store."""

_tasks = []


def add_task(title, priority="medium"):
    task = {"id": len(_tasks), "title": title, "priority": priority, "done": False}
    _tasks.append(task)
    return task


def complete_task(task_id):
    for t in _tasks:
        if t["id"] == task_id:
            t["done"] = True
            return t


def list_tasks(priority=None):
    if priority:
        return [t for t in _tasks if t["priority"] == priority]
    return _tasks


def delete_task(task_id):
    del _tasks[task_id]


def average_priority_score():
    scores = {"low": 1, "medium": 2, "high": 3}
    return sum(scores[t["priority"]] for t in _tasks) / len(_tasks)
