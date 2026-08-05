# Program: Task Manager (Polymorphism Update)
# Author: Jaden Horky
# Description: A console-based task manager using OOP, polymorphism, and JSON persistence.

import json
from task import Task, UrgentTask, RecurringTask, task_from_dict

TASKS_FILE = "tasks.json"
tasks = []


def save_tasks():
    """Saves the current global tasks list to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
    print("Tasks saved.")


def load_tasks():
    """Loads tasks from JSON, using the factory function to build the correct subclass."""
    global tasks
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = [task_from_dict(t) for t in json.load(file)]
            print(f"Loaded {len(tasks)} task(s).")
    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")
    except json.JSONDecodeError:
        tasks = []
        print("Save file is corrupted. Starting with an empty task list.")


def add_task(name, priority, estimated_time):
    """Creates a basic Task object and appends it to the global tasks list."""
    new_task = Task(name, priority, estimated_time)
    tasks.append(new_task)
    print(f"Task added: {new_task.name}")


def add_urgent_task():
    """Collects details, creates an UrgentTask, and appends it to the list."""
    name = input("Task name: ")
    try:
        estimated_time = int(input("Estimated time in minutes: "))
        deadline = input("Deadline (e.g. 2024-12-01): ")
        new_task = UrgentTask(name, estimated_time, deadline)
        tasks.append(new_task)
        print(f"Urgent task added: {new_task.name}")
    except ValueError:
        print("Error: Please enter a whole number for estimated time.")


def add_recurring_task():
    """Collects details, creates a RecurringTask, and appends it to the list."""
    name = input("Task name: ")
    priority = input("Priority (high, medium, low): ")
    try:
        estimated_time = int(input("Estimated time in minutes: "))
        frequency = input("Frequency (e.g. daily, weekly): ")
        new_task = RecurringTask(name, priority, estimated_time, frequency)
        tasks.append(new_task)
        print(f"Recurring task added: {new_task.name}")
    except ValueError:
        print("Error: Please enter a whole number for estimated time.")


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
        print("\nOptions: add | add-urgent | add-recurring | view | complete | delete | save | quit")
        choice = input("Choose an option: ").strip().lower()
        
        if choice == "add":
            name = input("Task name: ")
            priority = input("Priority (high, medium, low): ")
            try:
                estimated_time = int(input("Estimated time in minutes: "))
                add_task(name, priority, estimated_time)
            except ValueError:
                print("Error: Please enter a whole number for estimated time.")
                
        elif choice == "add-urgent":
            add_urgent_task()
            
        elif choice == "add-recurring":
            add_recurring_task()
                
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
                    
        elif choice == "delete":
            view_tasks()
            if tasks:
                try:
                    task_num = int(input("Enter task number to delete: "))
                    delete_task(task_num - 1)
                except ValueError:
                    print("Error: Please enter a valid number.")
        
        elif choice == "save":
            save_tasks()
            
        elif choice == "quit":
            save_tasks()
            print("Goodbye!")
            break
            
        else:
            print("Unrecognized option. Please choose a valid command from the list.")

if __name__ == "__main__":
    run_manager()