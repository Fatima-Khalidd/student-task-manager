def add_task(tasks, title):
    """Add a new task. Empty titles are rejected."""
    if not title.strip():
        raise ValueError("Task title cannot be empty")
    new_id = max([t["id"] for t in tasks], default=0) + 1
    task = {"id": new_id, "title": title.stripe(), "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    """Mark one task as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
    return tasks


def delete_task(tasks, task_id):
    """Delete a task by its id."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break
    return tasks