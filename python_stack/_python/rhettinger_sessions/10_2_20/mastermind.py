'Teach computer to play mastermind'
# https://en.wikipedia.org/wiki/Mastermind_(board_game)

from collections import Counter
from typing import NamedTuple
from random import choice
from itertools import product
from pprint import pprint as pp

colors = 'RGBYPOC'
holes = 4

class Score(NamedTuple):
    hits: int
    misses: int

def start():
    global possibles
    possibles = list(product(colors, repeat=holes))

def grade(guess, code):
    hits = sum(p==q for p, q in zip(guess, code))
    misses = sum((Counter(guess) & Counter(code)).values()) - hits
    return Score(hits, misses)

def reduce(guess, hits, misses):
    possibles[:] = [p for p in possibles if grade(p, guess) == (hits, misses)]
    print(guess, '-->', len(possibles))

def make_play():
    return choice(possibles)

def solve(code):
    start()
    while len(possibles) > 1:
        guess = make_play()
        score = grade(guess, code)
        reduce(guess, *score)

if __name__ == '__main__':

    solve('GRYB')

