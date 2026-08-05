# Program: Task Class
# Author: Jaden Horky
# Description: Defines the Task class with encapsulation and JSON serialization methods.

class Task:
    """Represents a single task in the Task Manager."""
    
    def __init__(self, name, priority, estimated_time):
        """
        Initializes a new Task object.
        
        Args:
            name (str): The name of the task.
            priority (str): The priority level (high, medium, low).
            estimated_time (int): Estimated completion time in minutes.
        """
        self.name = name
        self.estimated_time = estimated_time
        # Private attributes
        self.__priority = priority
        self.__is_complete = False

    def get_priority(self):
        """Returns the task's current priority level."""
        return self.__priority

    def set_priority(self, value):
        """
        Updates the priority if valid (high, medium, low).
        Prints an error message if the value is invalid.
        """
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
        """
        Creates and returns a Task object from a dictionary.
        
        Args:
            data_dict (dict): Dictionary containing task data.
            
        Returns:
            Task: A new Task instance.
        """
        new_task = cls(data_dict["name"], data_dict["priority"], data_dict["estimated_time"])
        
        if data_dict.get("is_complete"):
            new_task.mark_complete()
            
        return new_task

    def __str__(self):
        """Returns a readable formatted string representing the task."""
        status = "Complete" if self.__is_complete else "Pending"
        return f"{self.name} | Priority: {self.__priority} | Status: {status} | Est. Time: {self.estimated_time} mins"