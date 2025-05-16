#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 16, 2025
# This program generates and displays ten
# random numbers from 0 to 100 with
# lists and then displays their average.

# Import the constants module for useful constants.
import constants

# Import the random module for the random integer function.
import random


# Define the main function.
def main():
    # Print an empty space to format text.
    print("")
    # Initialize a list of integers as
    # an empty list to be used later.
    list_of_int = []

    # Use a for loop to loop over the maximum array
    # size to generate the ten random numbers.
    for index in range(constants.MAX_ARRAY_SIZE):
        # Generate a random number from the minimum number
        # size, 0, to the maximum number size, 100.
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # Populate the list by appending the random number.
        list_of_int.append(random_number)

        # Display information about the random
        # number and its current position.
        print(f"{random_number} added to the list at position {index}.")

    # Initialize the sum to 0 to be used later.
    sum = 0

    # Use a for loop to loop over the maximum
    # array size to add all the random numbers.
    for index in range(constants.MAX_ARRAY_SIZE):
        # Add the random number to the sum.
        sum += list_of_int[index]

    # Calculate the average by dividing the sum by the maximum array size.
    average = sum / constants.MAX_ARRAY_SIZE
    # Display the average.
    print(f"\nThe average is: {average}.\n")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
