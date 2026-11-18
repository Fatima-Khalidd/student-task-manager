# Student Task Manager

A simple command-line task manager written in Python. It lets students add tasks, view them, mark them as complete and delete them. Tasks are saved in a `tasks.json` file so they are kept between runs.

**Project status:** Testing phase complete, v1.0.0 ready

## Features
- Add tasks with automatic sequential IDs (empty titles are rejected)
- View all tasks with completion checkboxes (`[ ]` / `[x]`)
- Mark single or multiple tasks as completed
- Delete tasks by ID with input validation
- Persistent local storage using `tasks.json`

## Setup
Requirements: Python 3.8 or newer. No extra packages are needed.

Clone the repository and navigate into the folder:
```bash
git clone [https://github.com/Fatima-Khalidd/student-task-manager.git](https://github.com/Fatima-Khalidd/student-task-manager.git)
cd student-task-manager