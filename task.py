# Program: Task Classes
# Author: Jaden Horky
# Description: Defines the base Task class and its subclasses (UrgentTask, RecurringTask).

class Task:
    """Represents a single task in the Task Manager."""
    
    def __init__(self, name, priority, estimated_time):
        """Initializes a new Task object."""
        self.name = name
        self.estimated_time = estimated_time
        self.__priority = priority
        self.__is_complete = False

    def get_priority(self):
        """Returns the task's current priority level."""
        return self.__priority

    def set_priority(self, value):
        """Updates the priority if valid (high, medium, low)."""
        valid_priorities = ["high", "medium", "low"]
        if value.lower() in valid_priorities:
            self.__priority = value.lower()
        else:
            print("Error: Priority must be 'high', 'medium', or 'low'.")

    def get_is_complete(self):
        """Returns the task's completion status."""
        return self.__is_complete

    def mark_complete(self):
        """Marks the task as complete."""
        self.__is_complete = True

    def to_dict(self):
        """Converts the Task object to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "priority": self.__priority,
            "is_complete": self.__is_complete,
            "estimated_time": self.estimated_time
        }

    @classmethod
    def from_dict(cls, data_dict):
        """Creates and returns a Task object from a dictionary."""
        new_task = cls(data_dict["name"], data_dict["priority"], data_dict["estimated_time"])
        if data_dict.get("is_complete"):
            new_task.mark_complete()
        return new_task

    def __str__(self):
        """Returns a readable formatted string representing the task."""
        status = "Complete" if self.__is_complete else "Pending"
        return f"{self.name} | Priority: {self.__priority} | Status: {status} | Est. Time: {self.estimated_time} mins"


class UrgentTask(Task):
    """Represents an urgent task with a strict deadline."""
    
    def __init__(self, name, estimated_time, deadline):
        """Initializes an UrgentTask, automatically setting priority to high."""
        super().__init__(name, "high", estimated_time)
        self.deadline = deadline

    def __str__(self):
        """Returns a formatted string including the [URGENT] label and deadline."""
        status = "Complete" if self.get_is_complete() else "Pending"
        return f"[URGENT] {self.name} | Status: {status} | Est. Time: {self.estimated_time} mins | Deadline: {self.deadline}"

    def to_dict(self):
        """Converts the UrgentTask to a dictionary, appending type and deadline."""
        data = super().to_dict()
        data["type"] = "UrgentTask"
        data["deadline"] = self.deadline
        return data


class RecurringTask(Task):
    """Represents a task that repeats on a regular frequency."""
    
    def __init__(self, name, priority, estimated_time, frequency):
        """Initializes a RecurringTask with a specific frequency."""
        super().__init__(name, priority, estimated_time)
        self.frequency = frequency

    def __str__(self):
        """Returns a formatted string including the [RECURRING] label and frequency."""
        status = "Complete" if self.get_is_complete() else "Pending"
        return f"[RECURRING: {self.frequency}] {self.name} | Priority: {self.get_priority()} | Status: {status} | Est. Time: {self.estimated_time} mins"

    def reset(self):
        """Resets the task completion status to False for the next cycle."""
        self._Task__is_complete = False
        print(f"Task reset for next cycle: {self.name} ({self.frequency})")

    def to_dict(self):
        """Converts the RecurringTask to a dictionary, appending type and frequency."""
        data = super().to_dict()
        data["type"] = "RecurringTask"
        data["frequency"] = self.frequency
        return data


def task_from_dict(data):
    """
    Factory function that returns the appropriate Task object based on dictionary data.
    """
    task_type = data.get("type")
    
    if task_type == "UrgentTask":
        task = UrgentTask(data["name"], data["estimated_time"], data["deadline"])
        if data.get("is_complete"):
            task.mark_complete()
        return task
        
    elif task_type == "RecurringTask":
        task = RecurringTask(data["name"], data["priority"], data["estimated_time"], data["frequency"])
        if data.get("is_complete"):
            task.mark_complete()
        return task
        
    else:
        return Task.from_dict(data)

# Polymorphism Block
if __name__ == "__main__":
    demo_tasks = [
        Task("Buy groceries", "low", 30),
        UrgentTask("Fix server outage", 5, "2024-12-01"),
        RecurringTask("Team standup", "medium", 15, "daily")
    ]

    print("--- Polymorphism Demo ---")
    for task in demo_tasks:
        print(task)
        print("Is a Task instance:\n", isinstance(task, Task))