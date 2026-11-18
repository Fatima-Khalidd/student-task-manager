def add_task(tasks, title):
    """Add a new task and return it."""
    new_id = max([t["id"] for t in tasks], default=0) + 1
    task = {"id": new_id, "title": title, "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    """Mark the selected task as completed. Raise ValueError if not found."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise ValueError("No task with id " + str(task_id))


def delete_task(tasks, task_id):
    """Delete a task by its id."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break
    return tasks