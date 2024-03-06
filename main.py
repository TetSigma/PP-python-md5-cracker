import hashlib
from itertools import product

hash_to_match = "90e4af88eef87f65950a080cc5d218d2"

def generate_combinations(available_chars, length):
    all_combinations = [''.join(combination) for combination in product(available_chars, repeat=length)]
    return all_combinations

available_chars = "abcdefghijklmnopqrstuvwxyz"
length = 3
possible_combinations = generate_combinations(available_chars, length)

for combination in possible_combinations:
    for char in possible_combinations:
        candidate = char + 'techni' + combination
        if hashlib.md5(candidate.encode()).hexdigest() == hash_to_match:
            print("Found matching string:", candidate)
            break



