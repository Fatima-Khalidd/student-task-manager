import json
import os

from tasks import add_task, complete_task, delete_task

DATA_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        mark = "[x]" if task["done"] else "[ ]"
        print(str(task["id"]) + ". " + mark + " " + task["title"])


def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add task\n2. Show tasks\n3. Complete tasks\n4. Delete task\n5. Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                add_task(tasks, input("Task title: "))
            elif choice == "2":
                show_tasks(tasks)
            elif choice == "3":
                for part in input("Task ids (example 1,2): ").split(","):
                    complete_task(tasks, int(part))
            elif choice == "4":
                delete_task(tasks, int(input("Task id: ")))
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print("Error:", error)
        save_tasks(tasks)


if __name__ == "__main__":
    main()