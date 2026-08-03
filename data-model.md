# Data Model and Requirements Mapping

## Section 1: Task Dictionary Structure

| Field Name | Data Type | Description | Default Value |
|---|---|---|---|
| `name` | string | The name or description of the task. | None (Provided by user) |
| `priority` | string | The importance level (high, medium, low). | None (Provided by user) |
| `is_complete` | boolean | Indicates whether the task is finished. | `False` |
| `estimated_time` | integer | The estimated completion time in minutes. | None (Provided by user) |

## Section 2: Requirements Mapping

| Functional Requirement | Data Field or Function | How It Is Fulfilled |
|---|---|---|
| User can add a new task | `add_task()` function | Creates a dictionary with the required fields and appends it to the global `tasks` list. |
| User can view all tasks | `view_tasks()` function | Iterates over the `tasks` list and formats the dictionary values into a readable console string. |
| User can mark a task complete | `complete_task()` function | Accesses a specific dictionary by index and updates its `is_complete` boolean field to `True`. |
| User can delete a task | `delete_task()` function | Accesses the global `tasks` list and uses the `pop()` method to remove the dictionary at the specified index. |

## Section 3: Assumptions

*   **In-Memory Storage:** The data model currently assumes tasks only need to exist while the script is running. Because no file I/O operations are present, all tasks are wiped when the program terminates.
*   **Integer Time:** The model assumes the user will always enter a whole number for the estimated time, handled by an integer conversion.
*   **Case Sensitivity:** The model assumes the program handles case transformations, treating "High" and "high" as the same priority level.