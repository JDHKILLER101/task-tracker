# Program: Task Tracker (Refactored)
# Author: Jaden Horky
# Description: A modular task tracker using functions, scope, and default parameters.

APP_VERSION = "2.0"

def greet_user():
    print(f"Welcome to Task Tracker v{APP_VERSION}!")
    print()


def get_task_input():
    prompt_text = "Enter a task name (or type 'quit' to stop): "
    task = input(prompt_text)
    return task


def get_priority_input():
    priority = input("Enter priority (high, medium, low): ")
    return priority

def check_priority(priority="low"):
    priority = priority.lower()
    
    if priority == "high":
        return "Urgent: handle this task first."
    elif priority == "medium":
        return "Schedule: this task should be scheduled soon."
    elif priority == "low":
        return "Routine: handle this task when time allows."
    else:
        return "Priority not recognized. Please enter high, medium, or low."


def run_tracker():
    greet_user()
    
    while True:
        task_name = get_task_input()
        
        if task_name.lower() == "quit":
            print("Goodbye!")
            break
            
        task_priority = get_priority_input()
        if task_priority.strip() == "":
            message = check_priority()
        else:
            message = check_priority(task_priority)
            
        print(message)
        print()

run_tracker()