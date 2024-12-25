# Function to validate the task description (only letters, numbers, and spaces)
def validate_task(task):
    if all(c.isalnum() or c.isspace() for c in task):
        return True
    else:
        print("Invalid task description. Only alphanumeric characters and spaces are allowed.")
        return False

# Function to validate the priority level (high, medium, low)
def validate_priority(priority):
    if priority in ["high", "medium", "low"]:
        return True
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        return False

# Function to validate if the task is time-bound (yes or no)
def validate_time_bound(time_bound):
    if time_bound in ["yes", "no"]:
        return True
    else:
        print("Invalid input. Please enter 'yes' or 'no' for time-bound status.")
        return False

# Prompt the user for a task description and validate
while True:
    task = input("Enter your task: ")
    if validate_task(task):
        break

# Prompt the user for the priority level of the task and validate
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if validate_priority(priority):
        break

# Ask if the task is time-bound and validate
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if validate_time_bound(time_bound):
        break

# Process the task based on priority using Match Case
match priority:
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"
    case _:
        priority_message = "invalid priority"

# Check if the task is time-bound and add urgency to the reminder
if time_bound == "yes":
    urgency_message = "that requires immediate attention today!"
    message_prefix = "Reminder:"
else:
    urgency_message = "Note: Consider completing it when you have free time."
    message_prefix = "Note:"

# Construct the final reminder message
reminder_message = f"\n{message_prefix} '{task}' is a {priority_message} task. {urgency_message}"

# Print the reminder message (this is the key part you asked for)
print(reminder_message)
