digits = [
    ["###", "# #", "# #", "# #", "###"],   # 0
    ["  #", "  #", "  #", "  #", "  #"],   # 1
    ["###", "  #", "###", "#  ", "###"],   # 2
    ["###", "  #", "###", "  #", "###"],   # 3
    ["# #", "# #", "###", "  #", "  #"],   # 4
    ["###", "#  ", "###", "  #", "###"],   # 5
    ["###", "#  ", "###", "# #", "###"],   # 6
    ["###", "  #", "  #", "  #", "  #"],   # 7
    ["###", "# #", "###", "# #", "###"],   # 8
    ["###", "# #", "###", "  #", "###"]    # 9
]

def display_number(number):
    # Convert the number to a string and iterate through each digit
    for digit in str(number):
        digit = int(digit)  # Convert the digit back to an integer
        pattern = digits[digit]  # Get the LED pattern for the current digit

        # Display each line of the LED pattern
        for line in pattern:
            print(line.replace("#", "*").replace(" ", " "))  # Replace '#' with '*' for visual representation

        print()  # Print a blank line between digits

# Prompt the user to enter a non-negative integer number
number = int(input("Enter a non-negative integer number: "))

# Display the number using the simulated seven-segment display
display_number(number)
