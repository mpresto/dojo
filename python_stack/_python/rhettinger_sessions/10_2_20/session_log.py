Python 3.9.0rc2 (v3.9.0rc2:2bd31b5fde, Sep 16 2020, 20:19:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # https://www.dropbox.com/sh/i56w8gm1rounm54/AADrexzOHPTS7C-tjHpo90OQa?dl=0
>>> # http://bit.ly/python-lg3
>>> # create a script the prints hello world and run it.
>>> # Why teach computers to play games?
>>> # Almost always the skills carry over to tasks.
>>> # Games are fun.  Present interesting problems in small packages.
>>> 
>>> # Code marker:     Red Blue Green Red
>>> # Code breaker:    Yell Blue Orang Red   |-->  RightPlace=2 Wrong=0
>>> #                  Yell Blue Red   Red   |-->  RightPlace=2 Wrong=1
>>> 
>>> # Combinatorics in the itertools
>>> from itertools import *
>>> # product permutations combinations combinations_with_replacements
>>> for c in 'LOVE':
	print(c)

	
L
O
V
E
>>> for c in 'LOVE':
	for d in 'HATE':
		print(c+d)

		
LH
LA
LT
LE
OH
OA
OT
OE
VH
VA
VT
VE
EH
EA
ET
EE
>>> 4 * 4
16
>>> for c in 'LOVE':
	for d in 'PEACE':
		for e in 'HATE':
			print(c+d+e)

			
LPH
LPA
LPT
LPE
LEH
LEA
LET
LEE
LAH
LAA
LAT
LAE
LCH
LCA
LCT
LCE
LEH
LEA
LET
LEE
OPH
OPA
OPT
OPE
OEH
OEA
OET
OEE
OAH
OAA
OAT
OAE
OCH
OCA
OCT
OCE
OEH
OEA
OET
OEE
VPH
VPA
VPT
VPE
VEH
VEA
VET
VEE
VAH
VAA
VAT
VAE
VCH
VCA
VCT
VCE
VEH
VEA
VET
VEE
EPH
EPA
EPT
EPE
EEH
EEA
EET
EEE
EAH
EAA
EAT
EAE
ECH
ECA
ECT
ECE
EEH
EEA
EET
EEE
>>> 4 * 5 * 4
80
>>> 
>>> 
>>> for c, d in product('LOVE', 'HATE'):
	print(c + d)

	
LH
LA
LT
LE
OH
OA
OT
OE
VH
VA
VT
VE
EH
EA
ET
EE
>>> 
>>> for c, d, e in product('LOVE', 'PEACE', 'HATE'):
	print(c + d + e)

	
LPH
LPA
LPT
LPE
LEH
LEA
LET
LEE
LAH
LAA
LAT
LAE
LCH
LCA
LCT
LCE
LEH
LEA
LET
LEE
OPH
OPA
OPT
OPE
OEH
OEA
OET
OEE
OAH
OAA
OAT
OAE
OCH
OCA
OCT
OCE
OEH
OEA
OET
OEE
VPH
VPA
VPT
VPE
VEH
VEA
VET
VEE
VAH
VAA
VAT
VAE
VCH
VCA
VCT
VCE
VEH
VEA
VET
VEE
EPH
EPA
EPT
EPE
EEH
EEA
EET
EEE
EAH
EAA
EAT
EAE
ECH
ECA
ECT
ECE
EEH
EEA
EET
EEE
>>> for c, d in product('LOVE', 'LOVE'):
	print(c + d)

	
LL
LO
LV
LE
OL
OO
OV
OE
VL
VO
VV
VE
EL
EO
EV
EE
>>> for c, d, e in product('LOVE', 'LOVE', 'LOVE'):
	print(c + d + e)

	
LLL
LLO
LLV
LLE
LOL
LOO
LOV
LOE
LVL
LVO
LVV
LVE
LEL
LEO
LEV
LEE
OLL
OLO
OLV
OLE
OOL
OOO
OOV
OOE
OVL
OVO
OVV
OVE
OEL
OEO
OEV
OEE
VLL
VLO
VLV
VLE
VOL
VOO
VOV
VOE
VVL
VVO
VVV
VVE
VEL
VEO
VEV
VEE
ELL
ELO
ELV
ELE
EOL
EOO
EOV
EOE
EVL
EVO
EVV
EVE
EEL
EEO
EEV
EEE
>>> for c, d, e in product('LOVE', repeat=3):
	print(c + d + e)

	
LLL
LLO
LLV
LLE
LOL
LOO
LOV
LOE
LVL
LVO
LVV
LVE
LEL
LEO
LEV
LEE
OLL
OLO
OLV
OLE
OOL
OOO
OOV
OOE
OVL
OVO
OVV
OVE
OEL
OEO
OEV
OEE
VLL
VLO
VLV
VLE
VOL
VOO
VOV
VOE
VVL
VVO
VVV
VVE
VEL
VEO
VEV
VEE
ELL
ELO
ELV
ELE
EOL
EOO
EOV
EOE
EVL
EVO
EVV
EVE
EEL
EEO
EEV
EEE
>>> for t in product('LOVE', repeat=3):
	print(t)

	
('L', 'L', 'L')
('L', 'L', 'O')
('L', 'L', 'V')
('L', 'L', 'E')
('L', 'O', 'L')
('L', 'O', 'O')
('L', 'O', 'V')
('L', 'O', 'E')
('L', 'V', 'L')
('L', 'V', 'O')
('L', 'V', 'V')
('L', 'V', 'E')
('L', 'E', 'L')
('L', 'E', 'O')
('L', 'E', 'V')
('L', 'E', 'E')
('O', 'L', 'L')
('O', 'L', 'O')
('O', 'L', 'V')
('O', 'L', 'E')
('O', 'O', 'L')
('O', 'O', 'O')
('O', 'O', 'V')
('O', 'O', 'E')
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    print(t)
KeyboardInterrupt
>>> for t in product('LOVE', repeat=3):
	print(''.join(t))

	
LLL
LLO
LLV
LLE
LOL
LOO
LOV
LOE
LVL
LVO
LVV
LVE
LEL
LEO
LEV
LEE
OLL
OLO
Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    print(''.join(t))
KeyboardInterrupt
>>> type('')
<class 'str'>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> # someobject.somemeth(arg1, arg2)
>>> # typesomeobject.somemeth(someobject, arg1, arg2)
>>> 
>>> # someobject.somemeth(arg1, arg2)                    # Bound method:   the object and method are bound
>>> 
>>> t = ('raymond', 'dean', 'hettinger')
>>> ' '.join(t)
'raymond dean hettinger'
>>> str.join(' ', t)
'raymond dean hettinger'
>>> # typesomeobject.somemeth(someobject, arg1, arg2)   # Unbound method:  we only know the method
>>> 
>>> pow(2, 5)              # The arity of this function is two.
32
>>> ord('A')               # arity one
65
>>> from time import ctime
>>> ctime()
'Fri Oct  2 10:28:31 2020'
>>> # map(arity1, iteratable) --> iterator
>>> 
>>> [ord('R'), ord('a'), ord('y')]
[82, 97, 121]
>>> list(map(ord, 'Raymond'))
[82, 97, 121, 109, 111, 110, 100]
>>> 
>>> # Need a tool to take a high arity function and make it smaller:  Freeze some of the arguments
>>> pow(2, 5)             # It takes two arguments to FULLY evaluate the function
32
>>> # You only know the 2 # You can only PARTIALLY evaluate the function
>>> 
>>> from functools import partial
>>> twopow = partial(pow, 2)
>>> twopow(5)
32
>>> list(map(twopow, range(20)))
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
>>> list(map(partial(pow, 2), range(20)))
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
>>> 
>>> 
>>> space_join = partial(str.join, ' ')
>>> space_join(['raymond', 'dean', 'hettinger'])
'raymond dean hettinger'
>>> # We have a tool in python that partials unbound methods by freezing the first object:  bound_method
>>> space_join = ' '.join
>>> space_join(['raymond', 'dean', 'hettinger'])
'raymond dean hettinger'
>>> 
>>> # Bound methods are exactly the same as partially a method with an object.
>>> ' '.join(['raymond', 'dean', 'hettinger'])
'raymond dean hettinger'
>>> 
>>> 
>>> pow(2, 5)
32
>>> t = (2, 5)
>>> pow(t)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    pow(t)
TypeError: pow() missing required argument 'exp' (pos 2)
>>> pow(*t)
32
>>> 
>>> lot = [(2, 5), (3, 2), (7, 2), (7, 3)]
>>> lot[0]
(2, 5)
>>> pow(*lot[0])
32
>>> pow(*lot[1])
9
>>> list(map(pow, lot))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    list(map(pow, lot))
TypeError: pow() missing required argument 'exp' (pos 2)
>>> 
>>> list(starmap(pow, lot))
[32, 9, 49, 343]
>>> # Starmap loops over all the tuples in the list of tuples,
>>> # and unpacks the arguments for a higher arity function.
>>> for t in product('LOVE', repeat=3):
	print(''.join(t))

	
LLL
LLO
LLV
LLE
LOL
LOO
LOV
LOE
LVL
LVO
LVV
LVE
LEL
LEO
LEV
LEE
OLL
OLO
OLV
OLE
OOL
OOO
OOV
OOE
OVL
OVO
OVV
OVE
OEL
OEO
OEV
OEE
VLL
VLO
VLV
VLE
VOL
VOO
VOV
VOE
VVL
VVO
VVV
VVE
VEL
VEO
VEV
VEE
ELL
ELO
ELV
ELE
EOL
EOO
EOV
EOE
EVL
EVO
EVV
EVE
EEL
EEO
EEV
EEE
>>> list(map(''.join, product('LOVE', repeat=3)))
['LLL', 'LLO', 'LLV', 'LLE', 'LOL', 'LOO', 'LOV', 'LOE', 'LVL', 'LVO', 'LVV', 'LVE', 'LEL', 'LEO', 'LEV', 'LEE', 'OLL', 'OLO', 'OLV', 'OLE', 'OOL', 'OOO', 'OOV', 'OOE', 'OVL', 'OVO', 'OVV', 'OVE', 'OEL', 'OEO', 'OEV', 'OEE', 'VLL', 'VLO', 'VLV', 'VLE', 'VOL', 'VOO', 'VOV', 'VOE', 'VVL', 'VVO', 'VVV', 'VVE', 'VEL', 'VEO', 'VEV', 'VEE', 'ELL', 'ELO', 'ELV', 'ELE', 'EOL', 'EOO', 'EOV', 'EOE', 'EVL', 'EVO', 'EVV', 'EVE', 'EEL', 'EEO', 'EEV', 'EEE']
>>> 
>>> list(range(2))
[0, 1]
>>> for t in product(range(2), repeat=4):
	print(t)

	
(0, 0, 0, 0)
(0, 0, 0, 1)
(0, 0, 1, 0)
(0, 0, 1, 1)
(0, 1, 0, 0)
(0, 1, 0, 1)
(0, 1, 1, 0)
(0, 1, 1, 1)
(1, 0, 0, 0)
(1, 0, 0, 1)
(1, 0, 1, 0)
(1, 0, 1, 1)
(1, 1, 0, 0)
(1, 1, 0, 1)
(1, 1, 1, 0)
(1, 1, 1, 1)
>>> n = 42
>>> str(n)
'42'
>>> row = (1, 1, 0, 1)
>>> list(map(str, row))
['1', '1', '0', '1']
>>> ''.join(map(str, row))
'1101'
>>> for t in product(range(2), repeat=4):
	print(''.join(map(str, row)))

	
1101
1101
1101
1101
1101
1101
1101
1101
1101
1101
1101
1101
1101
1101
1101
1101
>>> for row in product(range(2), repeat=4):
	print(''.join(map(str, row)))

	
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
>>> 
>>> 
>>> 
>>> from pprint import pprint as pp
>>> pp(list(product('LOVE', repeat=2)))
[('L', 'L'),
 ('L', 'O'),
 ('L', 'V'),
 ('L', 'E'),
 ('O', 'L'),
 ('O', 'O'),
 ('O', 'V'),
 ('O', 'E'),
 ('V', 'L'),
 ('V', 'O'),
 ('V', 'V'),
 ('V', 'E'),
 ('E', 'L'),
 ('E', 'O'),
 ('E', 'V'),
 ('E', 'E')]
>>> print(list(product('LOVE', repeat=2)))
[('L', 'L'), ('L', 'O'), ('L', 'V'), ('L', 'E'), ('O', 'L'), ('O', 'O'), ('O', 'V'), ('O', 'E'), ('V', 'L'), ('V', 'O'), ('V', 'V'), ('V', 'E'), ('E', 'L'), ('E', 'O'), ('E', 'V'), ('E', 'E')]
>>> 
>>> # I want a product() but with out repeated elements:   permutations
>>> pp(list(permutations('LOVE', 2)))
[('L', 'O'),
 ('L', 'V'),
 ('L', 'E'),
 ('O', 'L'),
 ('O', 'V'),
 ('O', 'E'),
 ('V', 'L'),
 ('V', 'O'),
 ('V', 'E'),
 ('E', 'L'),
 ('E', 'O'),
 ('E', 'V')]
>>> # I want a product() with repeated elements and repeat reordered repeats:   OL LO
>>> # I want a product() with repeated elements and repeat reordered repeats:   OL LO:  combinations
>>> pp(list(combinations('LOVE', 2)))
[('L', 'O'), ('L', 'V'), ('L', 'E'), ('O', 'V'), ('O', 'E'), ('V', 'E')]
>>> 
>>> 
>>> # User status:   new_user  trial_user   exp_trial_user  paying_user  former_paying_user  banned_user
>>> # Actions:    login  sign-up trial  ban_user
>>> # Site:       make a post,    view archives,   see_ads
>>> 
>>> # for status, action, location in product(statuses, actions, sites): ...
>>> 
>>> # sign-up  pay  stop paying   ask for trial
>>> # permutatation(actions, 4)
>>> 
>>> 
>>> for cwr in combinations_with_replacement('LOVE', 3):
	print(''.join(cwr))

	
LLL
LLO
LLV
LLE
LOO
LOV
LOE
LVV
LVE
LEE
OOO
OOV
OOE
OVV
OVE
OEE
VVV
VVE
VEE
EEE
>>> 
>>> 
>>> 
>>> from collections import Counter
>>> Counter('simsalabim')
Counter({'s': 2, 'i': 2, 'm': 2, 'a': 2, 'l': 1, 'b': 1})
>>> election = 'CTTTCCCCTTCCCTCCCTTCTTSTTCC'
>>> Counter(election)
Counter({'C': 14, 'T': 12, 'S': 1})
>>> Counter(election).most_common(2)
[('C', 14), ('T', 12)]
>>> Counter(election).most_common(1)
[('C', 14)]
>>> Counter(election).most_common(1)[0]
('C', 14)
>>> 
>>> # Counters implement multisets
>>> 
>>> set('simsalabim')
{'l', 'b', 'a', 'm', 'i', 's'}
>>> # A counter/multiset is a kind of set that eliminates duplicates but remembers how many dups it saw.
>>> 
>>> 
>>> p = 'simsalabim'
>>> q = 'abracadabra'
>>> set(p) & set(q)
{'b', 'a'}
>>> set(p) - set(q)
{'l', 'm', 's', 'i'}
>>> set(q) - set(p)
{'c', 'd', 'r'}
>>> set(q) | set(p)
{'b', 'd', 'l', 'c', 'a', 'r', 'm', 'i', 's'}
>>> #  intersection  difference  union
>>> 
>>> 
>>> even = {2, 4, 6, 8, 10}
>>> primes = {2, 3, 5, 7, 11}
>>> even & primes
{2}
>>> even | primes
{2, 3, 4, 5, 6, 7, 8, 10, 11}
>>> even - primes
{8, 10, 4, 6}
>>> primes - even
{11, 3, 5, 7}
>>> 
>>> 
>>> Counter(p)
Counter({'s': 2, 'i': 2, 'm': 2, 'a': 2, 'l': 1, 'b': 1})
>>> set(p)
{'l', 'b', 'a', 'm', 'i', 's'}
>>> Counter(q)
Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
>>> set(q)
{'b', 'd', 'c', 'a', 'r'}
>>> 
>>> set(p) & set(q)
{'b', 'a'}
>>> Counter(p) & Counter(q)          # Largest common count.   Minimum of the two counts.
Counter({'a': 2, 'b': 1})
>>> p
'simsalabim'
>>> q
'abracadabra'
>>> 
>>> Counter(p) | Counter(q)           # Maximum of the two counts
Counter({'a': 5, 's': 2, 'i': 2, 'm': 2, 'b': 2, 'r': 2, 'l': 1, 'c': 1, 'd': 1})
>>> Counter(p) + Counter(q)
Counter({'a': 7, 'b': 3, 's': 2, 'i': 2, 'm': 2, 'r': 2, 'l': 1, 'c': 1, 'd': 1})
>>> Counter(p + q)
Counter({'a': 7, 'b': 3, 's': 2, 'i': 2, 'm': 2, 'r': 2, 'l': 1, 'c': 1, 'd': 1})
>>> # RDH TW
>>> 
>>> Counter(p - q)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    Counter(p - q)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> Counter(p) - Counter(q)           # Saturating arithmetic (never goes below zero)
Counter({'s': 2, 'i': 2, 'm': 2, 'l': 1})
>>> 
>>> 
>>> Counter('aaabb') - Counter('abbb')
Counter({'a': 2})
>>> 
>>> 
>>> # Goal:  Relate Counters back to sets and show that have related operations
>>> # If the inputs only have one of each element (no dups), counters and sets are the same.
>>> 
>>> set('dean') & set('raymond')
{'d', 'a', 'n'}
>>> Counter(dean)
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    Counter(dean)
NameError: name 'dean' is not defined
>>> Counter('dean')
Counter({'d': 1, 'e': 1, 'a': 1, 'n': 1})
>>> Counter('raymond')
Counter({'r': 1, 'a': 1, 'y': 1, 'm': 1, 'o': 1, 'n': 1, 'd': 1})
>>> Counter('dean') & Counter('raymond')
Counter({'d': 1, 'a': 1, 'n': 1})
>>> 
>>> issubclass(bool, int)
True
>>> # True and False ARE the integers 1 and 0
>>> sum([True, True, False, True])
3
>>> 
>>> warm = {'red', 'orange', 'yellow'}
>>> cool = {'blue', 'violet', 'green'}
>>> 'orange' in cool
False
>>> colors = 'red yellow green orange blue yellow'.split()
>>> colors
['red', 'yellow', 'green', 'orange', 'blue', 'yellow']
>>> 
>>> [color in warm for color in colors]
[True, True, False, True, False, True]
>>> sum([color in warm for color in colors])
4
>>> sum(color in warm for color in colors)
4
>>> 
>>> [color for color in colors if color in warm]
['red', 'yellow', 'orange', 'yellow']
>>> 
>>> 
>>> 
>>> warm = {'red', 'orange', 'yellow'}
>>> cool = {'blue', 'violet', 'green'}
>>> colors = 'red yellow green orange blue yellow'.split()
>>> backup = colors                                         # Assignments NEVER make copies. Create new refs.
>>> colors = [color for color in colors if color in warm]
>>> colors
['red', 'yellow', 'orange', 'yellow']
>>> backup
['red', 'yellow', 'green', 'orange', 'blue', 'yellow']
>>> 
>>> 
>>> 
>>> warm = {'red', 'orange', 'yellow'}
>>> cool = {'blue', 'violet', 'green'}
>>> colors = 'red yellow green orange blue yellow'.split()
>>> backup = colors                                         # Assignments NEVER make copies. Create new refs.
>>> colors[:] = [color for color in colors if color in warm]
>>> 
>>> colors
['red', 'yellow', 'orange', 'yellow']
>>> backup
['red', 'yellow', 'orange', 'yellow']
>>> 
>>> 
>>> 
>>> names = ['manny', 'mo', 'jack']
>>> names = ['tom', 'dick', 'harry']
>>> 
>>> 
>>> 
>>> issubclass(Counter, dict)
True
>>> d = dict(raymond=5, rachel=3)
>>> d['raymond']
5
>>> d['raymond'] += 1
>>> d
{'raymond': 6, 'rachel': 3}
>>> d['matthew']
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    d['matthew']
KeyError: 'matthew'
>>> d['matthew'] += 1
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    d['matthew'] += 1
KeyError: 'matthew'
>>> 
>>> 
>>> # We usually love dictionaries but that KeyError is annoying for missing keys
>>> # at least in the context of counting.    The count should default to zero.
>>> 
>>> c = Counter(raymond=5, rachel=3)
>>> d['raymond']
6
>>> d['raymond'] += 1
>>> d
{'raymond': 7, 'rachel': 3}
>>> d['matthew']
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    d['matthew']
KeyError: 'matthew'
>>> d['matthew'] += 1
Traceback (most recent call last):
  File "<pyshell#268>", line 1, in <module>
    d['matthew'] += 1
KeyError: 'matthew'
>>> 
>>> 
>>> c = Counter(raymond=5, rachel=3)
>>> c['raymond']
5
>>> c['raymond'] += 1
>>> c
Counter({'raymond': 6, 'rachel': 3})
>>> c['matthew']
0
>>> c['matthew'] += 1
>>> c
Counter({'raymond': 6, 'rachel': 3, 'matthew': 1})
>>> 
>>> 
>>> # A counter is a kind of dictionary where missing keys default to zero
>>> # which is useful when counting.
>>> 
>>> 
>>> d = dict(raymond=5, rachel=3, matthew=1)
>>> pprint(d, width=20)
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    pprint(d, width=20)
NameError: name 'pprint' is not defined
>>> from pprint import pprint
>>> pprint(d, width=20)
{'matthew': 1,
 'rachel': 3,
 'raymond': 5}
>>> d.keys()
dict_keys(['raymond', 'rachel', 'matthew'])
>>> d.values()
dict_values([5, 3, 1])
>>> d.items()
dict_items([('raymond', 5), ('rachel', 3), ('matthew', 1)])
>>> 
>>> 
>>> c = Counter(raymond=5, rachel=3, matthew=1)
>>> c.keys()
dict_keys(['raymond', 'rachel', 'matthew'])
>>> c.values()
dict_values([5, 3, 1])
>>> sum(c.values())
9
>>> 
>>> 
>>> # Counters are multisets
>>> # Counters are dictionaries
>>> 
>>> 
>>> for p, q in zip('raymond', 'matthew'):
	print(p, q)

	
r m
a a
y t
m t
o h
n e
d w
>>> for p, q in zip('ray', 'matthew'):
	print(p, q)

	
r m
a a
y t
>>> for p, q in zip('raymond', 'matt'):
	print(p, q)

	
r m
a a
y t
m t
>>> for p, q in zip('ray', 'mat the w'):
	print(p, q)

	
r m
a a
y t
>>> 
>>> 
>>> code = 'RGYB'
>>> 
>>> code =   'RGYB'
>>> guess =  'RBOY'
>>> list(zip(code, guess))
[('R', 'R'), ('G', 'B'), ('Y', 'O'), ('B', 'Y')]
>>> [p == q for p, q in zip(code, guess)]
[True, False, False, False]
>>> sum(p == q for p, q in zip(code, guess))
1
>>> hits = sum(p == q for p, q in zip(code, guess))
>>> hits
1
>>> Counter(code)
Counter({'R': 1, 'G': 1, 'Y': 1, 'B': 1})
>>> Counter(guess)
Counter({'R': 1, 'B': 1, 'O': 1, 'Y': 1})
>>> Counter(code) & Counter(guess)
Counter({'R': 1, 'Y': 1, 'B': 1})
>>> set(code) & set(guess)
{'Y', 'B', 'R'}
>>> 
>>> 
>>> code =   'RGYR'
>>> guess =  'RBRY'
>>> Counter(code) & Counter(guess)
Counter({'R': 2, 'Y': 1})
>>> (Counter(code) & Counter(guess))
Counter({'R': 2, 'Y': 1})
>>> (Counter(code) & Counter(guess)).values()
dict_values([2, 1])
>>> sum((Counter(code) & Counter(guess)).values())
3
>>> sum((Counter(code) & Counter(guess)).values()) - hits
2
>>> 
========================== RESTART: /Users/raymond/Dropbox/Public/lg3/mastermind.py =========================
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/lg3/mastermind.py", line 4, in <module>
    from collection import Counter
ModuleNotFoundError: No module named 'collection'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/lg3/mastermind.py =====
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/lg3/mastermind.py", line 4, in <module>
    from collection import Counter
ModuleNotFoundError: No module named 'collection'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/lg3/mastermind.py =====
>>> grade('RGYR', 'RBRY')
(1, 2)
>>> grade('RGYR', 'RBRY')
(1, 2)
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/lg3/mastermind.py =====
>>> grade('RGYR', 'RBRY')
Score(hits=1, misses=2)
>>> t = grade('RGYR', 'RBRY')
>>> list(t)
[1, 2]
>>> t[:1]
(1,)
>>> a, b = t
>>> len(t)
2
>>> t[0]
1
>>> t[1]
2
>>> t.hits
1
>>> t.misses
2
>>> from random import *
>>> # CPU 16 general purpose registers.   Register are fast!
>>> #                    ^------>  Memory Dram (16 Gb)
>>> #                              Slow!
>>> 
>>> # Human brain 7 +/- 2 general purpose registers
>>> #                    ^------>  Memory Gray matter
>>> #                              Slow and Error prone.
>>> 
>>> # 7 -> 1
>>> # 7 -> 1 (chunking)
>>> # 1 -> 0 (aliasing)
>>> 
>>> # xor rax, rax            # 4 cycles -> 1 cycles -> 0 cycles
>>> 
>>> 
>>> from turtle
SyntaxError: invalid syntax
>>> from turtle import *
>>> shape('turtle')
>>> forward(100)
>>> right(90)
>>> forward(100)
>>> left(90)
>>> backwards(100)
Traceback (most recent call last):
  File "<pyshell#371>", line 1, in <module>
    backwards(100)
NameError: name 'backwards' is not defined
>>> backward(100)
>>> 
>>> # shape forward backward left right  |-> 3 registers
>>> 
>>> 
>>> from random import *
>>> random()                         # 0.0 <= x < 1.0
0.35097911458588693
>>> random() * 100.0                 # 0.0 <= x < 100.0
13.903845882843214
>>> 50.0 + random() * 100.0          # 50.0 <= x < 150.0
64.52424224427227
>>> 50.0 + random() * 100.0          # 50.0 <= x < 150.0
60.747781719029824
>>> uniform(50, 150)
75.05547358974604
>>> uniform(50, 150)
126.55289614098115
>>> 
>>> int(random() * 100.0)
75
>>> int(random() * 100.0)           # 50 <= x < 150
30
>>> int(random() * 100.0)           # 50 <= x < 150
83
>>> int(random() * 100.0) * 5       # 250 <= x < 750 in multiples of 5
400
>>> int(random() * 100.0) * 5       # 250 <= x < 750 in multiples of 5
295
>>> int(random() * 100.0) * 5       # 250 <= x < 750 in multiples of 5
75
>>> int(random() * 100.0) * 5       # 250 <= x < 750 in multiples of 5
495
>>> 250 + int(random() * 100.0) * 5       # 500 <= x < 1000 in multiples of 5
375
>>> 250 + int(random() * 100.0) * 5       # 500 <= x < 1000 in multiples of 5
745
>>> def myunifrom(lo, hi):
	return lo + (hi - lo) * random()

>>> 
>>> 
>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 20, 2))
[10, 12, 14, 16, 18]
>>> # range(start, stop, step)
>>> 
>>> randrange(500, 1000, 5)
745
>>> outcomes = ['win', 'lose', 'draw', 'double', 'try again']
>>> len(outcomes)
5
>>> outcomes[0]
'win'
>>> outcomes[4]
'try again'
>>> 0, 1, 2, 3, 4
(0, 1, 2, 3, 4)
>>> 
>>> random()
0.09737938147487168
>>> random() * 5
3.174287087265575
>>> random() * len(outcomes)
2.41158210233585
>>> int(random() * len(outcomes))
1
>>> int(random() * len(outcomes))
0
>>> outcomes[int(random() * len(outcomes))]
'lose'

>>> 
>>> 
>>> from random import *
>>> outcomes = ['win', 'lose', 'draw', 'double', 'try again']
>>> outcomes[int(random() * len(outcomes))]
'try again'
>>> outcomes[randrange(len(outcomes))]
'double'
>>> # 5 -> 3 -> 1
>>> choice(outcomes)
'win'
>>> 
>>> 
>>> outcomes[int(random() * len(outcomes))]                # 5 register
'draw'
>>> outcomes[randrange(len(outcomes))]                     # 3 register
'win'
>>> choice(outcomes)                                       # 1 register
'draw'
>>> 
>>> 
>>> # x, y, z           unknown real variables      f(x)            solve for x            find x
>>> # a, b, c           coefficients       ax**2 + b*x + c == 0
>>> # n, m              total number of things
>>> # i, j, k           integer indicies into a collection of things
>>> # k, r              number of a subset            n things taken k at a time
>>> 
>>> # p, q              paired parameters
>>> 
>>> k = 20
>>> 
>>> 
>>> from random import *
>>> outcomes = ['win', 'lose', 'draw', 'double', 'try again']
>>> k = 20
>>> # Goal:  make k spins of a roulette wheel
>>> [outcomes[int(random() * len(outcomes))] for i in range(k)]
['draw', 'try again', 'try again', 'draw', 'try again', 'try again', 'try again', 'win', 'win', 'lose', 'win', 'double', 'try again', 'double', 'lose', 'double', 'double', 'double', 'win', 'win']
>>> [outcomes[int(random() * len(outcomes))] for i in range(k)]           # 7 registers
['lose', 'double', 'lose', 'try again', 'win', 'double', 'lose', 'win', 'lose', 'win', 'lose', 'draw', 'double', 'lose', 'lose', 'draw', 'win', 'win', 'try again', 'lose']
>>> [outcomes[randrange(len(outcomes))]  for i in range(k)]               # 5 registers
['double', 'win', 'try again', 'double', 'draw', 'lose', 'double', 'draw', 'draw', 'draw', 'lose', 'draw', 'draw', 'draw', 'draw', 'double', 'double', 'draw', 'draw', 'double']
>>> [choice(outcomes) for i in range(k)]                                  # 3 registers
['try again', 'try again', 'draw', 'lose', 'win', 'lose', 'try again', 'draw', 'double', 'lose', 'try again', 'try again', 'try again', 'try again', 'double', 'try again', 'draw', 'draw', 'draw', 'lose']
>>> choices(outcomes, k=20)
['double', 'double', 'draw', 'lose', 'win', 'try again', 'draw', 'try again', 'draw', 'lose', 'try again', 'try again', 'lose', 'try again', 'lose', 'try again', 'draw', 'try again', 'double', 'double']
>>> # ^== sampling with replacement
>>> 
>>> sample(outcomes, k=3)
['draw', 'double', 'lose']
>>> sample(outcomes, k=3)
['lose', 'draw', 'win']
>>> sample(outcomes, k=3)
['draw', 'double', 'try again']
>>> 
>>> choices(outcomes, k=3)
['win', 'draw', 'try again']
>>> choices(outcomes, k=3)
['double', 'win', 'win']
>>> # randrange choice choices sample
>>> 
>>> 
>>> def mychoice(seq):
	return seq[randrange(len(seq))]

>>> mychoice('raymond')
'y'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/lg3/mastermind.py =====
>>> choices(pop, k=holes)
['B', 'C', 'B', 'P']
>>> 
>>> # Wrong message:
>>> #  Computers create hard problems
>>> #  Humans have to think deeply to solve them.
>>> 
>>> # Right message:
>>> #  Humans create hard problems
>>> #  Computers have to think deeply to solve them.
>>> 
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/lg3/mastermind.py =====
>>> pp(possibles[:40])
Traceback (most recent call last):
  File "<pyshell#477>", line 1, in <module>
    pp(possibles[:40])
NameError: name 'possibles' is not defined
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/lg3/mastermind.py =====
>>> start()
>>> pp(possibles[:40])
[('R', 'R', 'R', 'R'),
 ('R', 'R', 'R', 'G'),
 ('R', 'R', 'R', 'B'),
 ('R', 'R', 'R', 'Y'),
 ('R', 'R', 'R', 'P'),
 ('R', 'R', 'R', 'O'),
 ('R', 'R', 'R', 'C'),
 ('R', 'R', 'G', 'R'),
 ('R', 'R', 'G', 'G'),
 ('R', 'R', 'G', 'B'),
 ('R', 'R', 'G', 'Y'),
 ('R', 'R', 'G', 'P'),
 ('R', 'R', 'G', 'O'),
 ('R', 'R', 'G', 'C'),
 ('R', 'R', 'B', 'R'),
 ('R', 'R', 'B', 'G'),
 ('R', 'R', 'B', 'B'),
 ('R', 'R', 'B', 'Y'),
 ('R', 'R', 'B', 'P'),
 ('R', 'R', 'B', 'O'),
 ('R', 'R', 'B', 'C'),
 ('R', 'R', 'Y', 'R'),
 ('R', 'R', 'Y', 'G'),
 ('R', 'R', 'Y', 'B'),
 ('R', 'R', 'Y', 'Y'),
 ('R', 'R', 'Y', 'P'),
 ('R', 'R', 'Y', 'O'),
 ('R', 'R', 'Y', 'C'),
 ('R', 'R', 'P', 'R'),
 ('R', 'R', 'P', 'G'),
 ('R', 'R', 'P', 'B'),
 ('R', 'R', 'P', 'Y'),
 ('R', 'R', 'P', 'P'),
 ('R', 'R', 'P', 'O')Traceback (most recent call last):
  File "<pyshell#479>", line 1, in <module>
    pp(possibles[:40])
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py", line 53, in pprint
    printer.pprint(object)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py", line 148, in pprint
    self._format(object, self._stream, 0, 0, {}, 0)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py", line 176, in _format
    p(self, object, stream, indent, allowance, context, level + 1)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py", line 221, in _pprint_list
    self._format_items(object, stream, indent, allowance + 1,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py", line 426, in _format_items
    self._format(ent, stream, indent,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py", line 185, in _format
    stream.write(rep)
KeyboardInterrupt
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/lg3/mastermind.py =====
>>> start()
>>> len(possibles)
2401
>>> 7 ** 4
2401
>>> code = ['R', 'G', 'B', 'Y']
>>> guess = make_play()
>>> guess
('C', 'Y', 'B', 'C')
>>> score = grade(guess, code)
>>> score
Score(hits=1, misses=1)
>>> reduce(guess, *score)
('C', 'Y', 'B', 'C') --> 376
>>> 