# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable for the row counter
row = 0

# Use a while loop to print each row of the pattern
while row < size:
    # Use a for loop to print asterisks on the same line
    for col in range(size):
        print("*", end="")
    # Print a new line after each row
    print()
    # Increment the row counter
    row += 1
