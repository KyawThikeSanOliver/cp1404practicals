"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

result = None  # Initialize result outside the try block
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: Add more code here if needed
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
