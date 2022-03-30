"""Game Guess the number"""

from itertools import count
import numpy as np

number = np.random.randint(1, 101) # think of a number

# number of attempts
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The number must be less!")
    elif predict_number < number:
        print("The number must be greater!")
    else:
        print("You guessed the number! This number {}, in {} tries".format(number, count))
        break # end the game