def add_task(tasks, title):
    """Add a new task. Empty titles are rejected."""
    if not title.strip():
        raise ValueError("Task title cannot be empty")
    new_id = max([t["id"] for t in tasks], default=0) + 1
    task = {"id": new_id, "title": title.stripe(), "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    """Mark the selected task as completed. Raise ValueError if not found."""
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                raise ValueError("Task " + str(task_id) + " is already completed")
            task["done"] = True
            return task
                
            return task
        
    raise ValueError("No task with id " + str(task_id))


def delete_task(tasks, task_id):
    """Delete a task by its id. Raise ValueError if the id is not valid."""
        if not isinstance(task_id, int):
            raise ValueError("Task id must be a number")
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return task
    raise ValueError("No task with id " + str(task_id))