import random

#fuction that will guess the random number until it succeeds
def guess_the_number(l, r, correct_number):
    #adding operation counter
    counter = 0
    while True:
        random_number = random.randrange(l, r+1)
        counter += 1
        #If guessed number is less than correct number then we can increase the left end of range
        if random_number < correct_number:
            l += 1
        #Similarly we can lower the right end if number was too high
        elif random_number > correct_number:
            r -= 1
        else:
            return random_number, counter, l, r


if __name__ == '__main__':
    left_end = 1
    right_end = 1000
    user_number = int(input(f"Enter a number from {left_end} to {right_end}: "))
    #defining the ends of the number range


    answer = guess_the_number(left_end, right_end, user_number)
    print(f"""Correct number is: {answer[0]}
    Computer guessed it after this many attempts: {answer[1]}
    Range by the end: {answer[2]}-{answer[3]}""")
