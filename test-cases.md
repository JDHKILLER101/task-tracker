# Task Priority Script Test Cases

| Test Case ID | Description | Input | Expected Output |
|---|---|---|---|
| TC-01 | Expected (Valid) - High priority | Task: "Buy groceries"<br>Priority: "high" | "Urgent: handle this task first." |
| TC-02 | Expected (Valid) - Low priority | Task: "Read a book"<br>Priority: "low" | "Routine: handle this task when time allows." |
| TC-03 | Invalid Input - Unknown priority | Task: "Call doctor"<br>Priority: "whenever" | "Priority not recognized. Please enter high, medium, or low." |
| TC-04 | Edge Case - Empty task name | Task: `""` *(User just presses Enter)* | "Task name cannot be empty. Please try again." The loop then restarts. |
| TC-05 | System Exit | Task: "quit" | "Session ended. Goodbye!" and the program successfully terminates without asking for a priority. |