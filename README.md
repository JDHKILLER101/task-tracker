# Task Tracker
**Author:** Jaden Horky

**Description:** 
Task Tracker is a Python-based command-line application. By the end of this course, it will allow users to input, manage, and track the status and priority of their daily tasks.

## Project Structure
- **task_input.py**: Collects basic task information from the user using variables and input/output.
- **task_priority.py**: Adds priority logic using conditionals and a while loop.
- **task_tracker.py**: Refactored version using functions, scope, and docstrings.
- **task_manager.py**: Main task manager utilizing global lists and dictionaries.
- **data_model.md**: Documentation mapping system requirements to the data structure.

## Week 2 Progress

Adding file persistence solved the issue of data loss, allowing the Task Manager to store tasks in a JSON file between sessions so they aren't wiped when the program terminates. If the `FileNotFoundError` wasn't caught when loading tasks, the entire program would crash the very first time a user tried to run it before saving any data. This error handling directly connects to the QA mindset from Week 1 because it anticipates how users (or the environment) might break the system and builds defensive fail-safes to keep the application stable.