# Aim of this code is to find an avarage number of attempts needed to guess the random number by computer>
# If we decrease a range ends each time a wrong number is guessed.
import random

def guess_the_number(l, r, correct_number):
    # adding operation counter
    times_guessed = 0
    while True:
        random_number = random.randrange(l, r + 1)
        times_guessed += 1
        # If guessed number is less than correct number then we can increase the left end of range
        if random_number < correct_number:
            l = random_number
        # Similarly we can lower the right end if number was too high
        elif random_number > correct_number:
            r = random_number
        else:
            return times_guessed

if __name__ == '__main__':
    # Adding a variable that will count all guesses from 100 of iterations
    total_number_of_operations = 0
    # Defining the ends of range used to generate numbers
    left_end = 1
    right_end = 1000
    # Repeating the guessing 100 times so that we can get a clear vision of average
    for attempt in range(1, 101):
        random_numer_to_find = random.randint(left_end, right_end)
        times_guessed = guess_the_number(left_end, right_end, random_numer_to_find)
        total_number_of_operations += times_guessed

    print(f'''Total number of guesses: {total_number_of_operations}
    Average number of guesses per iteration is: {total_number_of_operations/100}''')
