# Program: Task Tracker Input Script
# Author: Jaden Horky
# Description: This script collects task details from a user, utilizes multiple data types, and displays a formatted summary.

# --- DATA TYPE PLACEHOLDERS ---
# Placeholder: task completion status, starts as False (Boolean)
is_complete = False

# Placeholder: completion percentage will be calculated later (Float)
completion_rate = 0.0

# --- WELCOME SECTION ---
print("Welcome to Task Tracker!")
print("Please enter your task details below.")
print()

# --- COLLECT INPUT ---
# 1. Task name (String)
task_name = input("Enter task name: ")

# 2. Priority level (String)
task_priority = input("Enter priority level (high, medium, low): ")

# 3. Estimated time (String converted to Integer)
time_input = input("Estimated time to complete (in minutes): ")
task_time = int(time_input)

# 4. Urgency (String)
task_urgent = input("Is this task urgent? (yes/no): ")

print()

# --- DISPLAY SUMMARY ---
print("--- Task Summary ---")
print("Task:", task_name)
print("Priority:", task_priority)
print("Estimated Time:", task_time, "minutes")
print("Urgent:", task_urgent)