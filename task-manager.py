# Program: Task Manager (OOP Refactored)
# Author: Jaden Horky
# Description: A console-based task manager using Task objects and JSON persistence.

import json
from task import Task

TASKS_FILE = "tasks.json"
tasks = []


def save_tasks():
    """Saves the current global tasks list to a JSON file by converting objects to dicts."""
    with open(TASKS_FILE, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
    print("Tasks saved.")


def load_tasks():
    """Loads tasks from a JSON file and instantiates them as Task objects."""
    global tasks
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = [Task.from_dict(t) for t in json.load(file)]
            print(f"Loaded {len(tasks)} task(s).")
    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")
    except json.JSONDecodeError:
        tasks = []
        print("Save file is corrupted. Starting with an empty task list.")


def add_task(name, priority, estimated_time):
    """Creates a Task object and appends it to the global tasks list."""
    new_task = Task(name, priority, estimated_time)
    tasks.append(new_task)
    print(f"Task added: {new_task.name}")


def view_tasks():
    """Loops through the tasks list and prints each task's details."""
    if not tasks:
        print("No tasks found.")
        return
    
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")


def complete_task(index):
    """Marks a task as complete based on its index."""
    if 0 <= index < len(tasks):
        tasks[index].mark_complete()
        print(f"Task marked complete: {tasks[index].name}")
    else:
        print("Error: Invalid task number.")


def delete_task(index):
    """Removes a task from the list based on its index."""
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task deleted: {removed.name}")
    else:
        print("Error: Invalid task number.")


def run_manager():
    """Main loop that provides the menu options and orchestrates the program."""
    load_tasks()
    print("Welcome to the Task Manager!")
    
    while True:
        print("\nOptions: add | view | complete | delete | save | quit")
        choice = input("Choose an option: ").strip().lower()
        
        if choice == "add":
            name = input("Task name: ")
            priority = input("Priority (high, medium, low): ")
            try:
                estimated_time = int(input("Estimated time in minutes: "))
                add_task(name, priority, estimated_time)
            except ValueError:
                print("Error: Please enter a whole number for estimated time.")
                continue
                
        elif choice == "view":
            view_tasks()
            
        elif choice == "complete":
            view_tasks()
            if tasks:
                try:
                    task_num = int(input("Enter task number to mark complete: "))
                    complete_task(task_num - 1)
                except ValueError:
                    print("Error: Please enter a valid number.")
                    continue
                    
        elif choice == "delete":
            view_tasks()
            if tasks:
                try:
                    task_num = int(input("Enter task number to delete: "))
                    delete_task(task_num - 1)
                except ValueError:
                    print("Error: Please enter a valid number.")
                    continue
        
        elif choice == "save":
            save_tasks()
            
        elif choice == "quit":
            save_tasks()
            print("Goodbye!")
            break
            
        else:
            print("Unrecognized option. Please choose add, view, complete, delete, save, or quit.")

run_manager()