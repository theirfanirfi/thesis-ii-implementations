# create a program to generate the random string of given letters.
import random
import string


def generate_random_string(length):
    sample_string = 'abcdefghijklmnopqrstuvwxyz'  # define the specific string
    # define the condition for random string
    result = ''.join((random.choice(sample_string)) for x in range(length))
    return result
