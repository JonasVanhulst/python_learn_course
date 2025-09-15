"""
Author: Jonas Vanhulst
Project: Python Learning Roadmap
Description: A structured roadmap with projects to take learners from beginner 
             to professional in Python development.
Date: 2025
"""

import random

def generate_random_number(start, end):
    return random.randint(start, end)


def main():
    print("Welcome to the number guessing game!")
    
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    number_to_guess = generate_random_number(start, end)
    attempts = 0
    guessed = False
    print(f"I have selected a number between {start} and {end}. Can you guess it?")
    
    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < start or user_guess > end:
                print(f"Please guess a number within the range {start} to {end}.")
                continue
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()