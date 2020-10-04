# Combinatorix in the itertools

from itertools import *
# product permutations combinations combinations_with_replacements

for c in 'LOVE':
    print(c)


for c in 'LOVE':
    for d in 'HATE':
        print(c + d)


for c in 'LOVE':
    for d in 'HATE':
        for e in 'PEACE':
            print(c + d + e)


# Cartesian product 
for c, d in product('LOVE', 'HATE'):
    print(c + d)


for c, d, e in product('LOVE', 'HATE', 'PEACE'):
    print(c + d + e)


for c, d, e in product('LOVE', 'LOVE', 'LOVE'):
    print(c + d + e)


for c, d, e in product('LOVE', repeat=3):
    print(c + d + e)


for t in product('LOVE', repeat=3):
    print(''.join(t))


#someobject.somemeth(arg1, arg2)
#typesomeobject.somemeth(someobject, arg1, arg2)
#someobject.somemeth(arg1, arg2)      #Bound Method: object and method are bound
t = ('raymond', 'dean', 'hettinger')
' '.join(t)
print(str.join(' ', t))
print(t)


# arity - the number of arguments a function takes


from time import ctime
print(ctime())

#map works best with arity 1 functions:
# map(arity1, iterable) --> iterator

ords = list(map(ord, 'Raymond'))
print(ords)

# Need a tool to take a high arity function and make it smaller: Freeze some of the args!
pow(2, 5)  # it takes 2 args to FULLY evaluate the function
# if you only know 1 arg, you can PARTIALLY evaluate the function

from functools import partial
twopow = partial(pow, 2)
twopow(5)
print(twopow(5))

print(list(map(twopow, range(20))))
print(list(map(partial(pow, 2), range(20))))

space_join = partial(str.join, ' ')
print(space_join(['raymond', 'dean', 'hettinger']))

# we have a tool in python that partials unbound methods by freezing th first object: a bound_method
space_join = ' '.join
print(space_join(['raymond', 'dean', 'hettinger']))
' '.join(['raymond', 'dean', 'hettinger'])


#Bound methods are exactly the same as partially a method with an object


pow(2, 5)
t = (2, 5)
# pow(t)
# # This throws an error^

# use asterix --
print(pow(*t))

lot = [(2, 5), (3, 2), (7, 2), (7, 3)]
pow(*lot[0])
list(starmap(pow, lot))
# starmap loops over all the tuples in the list of tuples
# and unpacks the arguments for a higher arity function

list(map(''.join, product('LOVE', repeat=3)))
list(starmap(''.join, product('LOVE', repeat=3)))

list(range(2))  # [0, 1]
for t in product(range(2), repeat=4):
    print(t)

list(map(str, row))
''.join(map(str, row))

#### go back to his notes for the rest of this ^^^





from pprint import pprint as pp
pp(list(product('LOVE', repeat=2)))

from collections import Counter
p = 'simsalabim'
q = 'abracadabra'

set(p) & set(q)  # & is the intersection between the two
set(p) - set(q)  # letters that are unique to p (difference)
set(q) - set(p)  # letters that are unique to q (difference)
set(q) | set(p)  # the union of both
# intersection, difference and union

# a counter/multiset is a kind of set that eliminates duplicates but remembers 
# how many duplicates it saw



'''Teach computer to play mastermind'''

from collection import Counter
from typing import NamedTuple
from random import choice
from itertools import product
from pprint import pprint as pp

class Score(NamedTuple):
    hits: int
    misses: int

def start():
    global possibles
    possible = list(product(colors, repeat=holes))

def grade(guess, code):
    hits = sum(p==q for p, q in zip(guess, code))
    misses = sum((Counter(guess) & Counter(code)).values()) - hits
    return Score(hits, misses)

def reduce(guess, hits, misses):
    possibles[:] = [p for p in possibles if grade(p, guess) == (hits, misses)]
print(guess, '-->', len(possibles))

def make)play():
    return choices(possibles)

def solve(code):
    start()
    while len(possibles) >1:
        guess = make_play()
        score = grade(guess, code)
        reduce(gugess, *score)

if __name__ == '__main__':
    solve ('GRYB')




########################
from heapq import nsmallest, nlargest
from statistics import *
data = [22, 24, 27, 25, 17, 19, 25, 26, 26, 25, 24, 24, 22, 19, 20]

