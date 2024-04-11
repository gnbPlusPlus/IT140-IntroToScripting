import random

# seedVal = int(input("What seed should be used? "))
# random.seed(seedVal)

print('\nWelcome to the higher/lower game!')
lower_bound = int(float(input('Enter the lower bound number: \n')) // 1.0)
upper_bound = int(float(input('Enter the upper bound number: \n')) // 1.0)

while lower_bound > upper_bound:
    print('The lower bound must be less than the upper bound.')
    lower_bound = int(float(input('Re-enter the lower bound number: \n')) // 1.0)
    upper_bound = int(float(input('Re-enter the upper bound number: \n')) // 1.0)
else:
    answer = random.randint(lower_bound, upper_bound)

print('Great, now guess a number between {} and {}.'.format(lower_bound, upper_bound))
user_guess = int(input())

while user_guess != answer:
    if user_guess < answer and user_guess >= lower_bound:
        print("That’s too low… Guess again.")
        user_guess = int(input())
    elif user_guess > answer and user_guess <= upper_bound:
        print('Too high! Guess again.')
        user_guess = int(input())
    elif user_guess < lower_bound:
        print("That's out of bounds! Guess again.")
        user_guess = int(input())
    elif user_guess > upper_bound:
        print("That's out of bounds! Guess again.")
        user_guess = int(input())
else:
    print("Yes!!! You've guessed it!")