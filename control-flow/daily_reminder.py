# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt the user for the priority level of the task
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

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
    urgency_message = "Consider completing it when you have free time."
    message_prefix = "Note:"

# Final reminder output with print() to check the output
reminder_message = f"\n{message_prefix} '{task}' is a {priority_message} task. {urgency_message}"

# Print the reminder message
print(reminder_message)
