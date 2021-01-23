'''
Find the uncommon letters and look around for a clue
ASNWER: grammaphobia
'''
import random

CLUE_1 = 'LOOKAROUNDEVERYLETTER'
CLUE_2 = 'fearofalphabetletters'
UNIQUE_LETTER_SET = set(CLUE_1)
ASCII_CHAR_RANGE = (32, 126)
CHAR_DUMP_SIZE_RANGE = (128, 256)

def generate():
    gen_string = ''
    for let1, let2 in zip(CLUE_1, CLUE_2):
        gen_string += get_char_dump(UNIQUE_LETTER_SET)
        gen_string += let1 + let2
    return gen_string

def get_char_dump(unique_char_set):
    char_dump = ''
    num_chars = random.randint(CHAR_DUMP_SIZE_RANGE[0], CHAR_DUMP_SIZE_RANGE[1])
    for _ in range(num_chars):
        chosen_char = chr(random.randint(ASCII_CHAR_RANGE[0], ASCII_CHAR_RANGE[1]))
        while chosen_char in unique_char_set:
            chosen_char = chr(random.randint(ASCII_CHAR_RANGE[0], ASCII_CHAR_RANGE[1]))
        char_dump += chosen_char
    return char_dump

if __name__ == "__main__":
    print (generate())
