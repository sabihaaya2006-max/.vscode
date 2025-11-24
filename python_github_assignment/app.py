# Welcoming statement
print("Welcome to my Python program!")

# Ask for user input
hours = input("How many hours did you study today?")

try:
     # Convert input to a number
    hours = float(hours)

    # Perform a calculation
    weekly_hours = hours * 7

# Show result clearly
print(f"You are on track to study about {weekly_hours} hours this week!")

except ValueError:
# Deal with non-numeric input
print("Error: Please enter a valid number for hours studied.")