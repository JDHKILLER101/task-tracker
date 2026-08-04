# Program: Task Manager Foundation
# Author: Jaden Horky
# Description: A console-based task manager using global lists, dictionaries, and JSON file persistence.

import json

TASKS_FILE = "tasks.json"

tasks = []


def save_tasks():
    """Saves the current global tasks list to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved.")


def load_tasks():
    """Loads tasks from a JSON file into the global tasks list."""
    global tasks
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            print(f"Loaded {len(tasks)} task(s).")
    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")
    except json.JSONDecodeError:
        tasks = []
        print("Save file is corrupted. Starting with an empty task list.")


def add_task(name, priority, estimated_time):
    """
    Creates a task dictionary and appends it to the global tasks list.
    
    Args:
        name (str): The name of the task.
        priority (str): The priority level (high, medium, low).
        estimated_time (int): The estimated time in minutes.
    """
    new_task = {
        "name": name,
        "priority": priority,
        "is_complete": False,
        "estimated_time": estimated_time
    }
    tasks.append(new_task)
    print(f"Task added: {name}")


def view_tasks():
    """Loops through the tasks list and prints each task's details."""
    if not tasks:
        print("No tasks found.")
        return
    
    for i, task in enumerate(tasks):
        status = "Complete" if task["is_complete"] else "Pending"
        print(f"{i + 1}. {task['name']} | Priority: {task['priority']} | Status: {status} | Est. Time: {task['estimated_time']} mins")


def complete_task(index):
    """
    Marks a task as complete based on its index.
    
    Args:
        index (int): The zero-based index of the task to complete.
    """
    if 0 <= index < len(tasks):
        tasks[index]["is_complete"] = True
        print(f"Task marked complete: {tasks[index]['name']}")
    else:
        print("Error: Invalid task number.")


def delete_task(index):
    """
    Removes a task from the list based on its index.
    
    Args:
        index (int): The zero-based index of the task to delete.
    """
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task deleted: {removed_task['name']}")
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