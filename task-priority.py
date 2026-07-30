# Program: Task Priority Checker
# Author: Jaden Horky
# Description: This script collects tasks in a loop and categorizes them by priority until the user quits.

# Step 1: Welcome Message
print("Welcome to Task Tracker Priority Checker!\n")

# Step 2 & 3: While loop and input collection
while True:
    task_name = input("Enter a task name (or type 'quit' to stop): ")
    
    # Check if the user wants to quit before asking for priority
    if task_name.lower() == 'quit':
        print("Session ended. Goodbye!")
        break
        
    # Step 5: Comparison operator other than ==
    if len(task_name) < 1:
        print("Task name cannot be empty. Please try again.\n")
        continue

    # Collect priority level
    task_priority = input("Enter priority (high, medium, low): ")

    # Step 4: Priority logic with if, elif, and else
    if task_priority.lower() == "high":
        print("Urgent: handle this task first.")
    elif task_priority.lower() == "medium":
        print("Schedule: this task should be scheduled soon.")
    elif task_priority.lower() == "low":
        print("Routine: handle this task when time allows.")
    else:
        print("Priority not recognized. Please enter high, medium, or low.\n")