"""Game Guess the number"""

import numpy as np

def random_predict(number:int=1) -> int:
    """ Randomly guess a number
        
    Args:
        number (int, optional): Hidden number. Defaults to l.
            
    Returns:
        int: Number of attempts
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break

    return (count)

print("Count of tries: {}".format(random_predict(10)))


def score_game(random_predict) -> int:
    """How many tries does it take on average to guess
        
    Args:
        rundom_predict (_type_): guess function
            
    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1) # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print('Your algorithm guesses the number on average in: {} attempts'.format(score))
    return(score)

if __name__ == '__main__':
    # run
    score_game(random_predict)