import unittest


# 1. Reverse List
# Example: reverseList([1,3,5]) should return [5,3,1]
# Example Test: assertEqual( reverseList([1,3,5]), [5,3,1] )
# Add at least 3 other test cases


# def reverse_list(arr):
#     for i in range(int(len(arr)/2)):
#         arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
#     return arr


# class reverse_list_test(unittest.TestCase):
#     """class of tests to be run for reverse_list()"""
#     def test_one(self):
#         self.assertEqual(reverse_list([1, 3, 5]), [5, 3, 1])

#     def test_two(self):
#         self.assertEqual(reverse_list([10, 8, 4]), [4, 8, 10])

#     def test_three(self):
#         self.assertTrue(reverse_list([1, 2, 4]) == [4, 2, 1])

#     def test_four(self):
#         self.assertNotEqual(reverse_list([11, 3, 7]), [7, 11, 3])


# if __name__ == '__main__':
#     unittest.main()


# unittest.main()


# 2. isPalindrome - Write a function that checks whether the given word is a
#       palindrome (a word that spells the same backward).
# Example: isPalindrome("racecar") should return True
# Example Test: assertEqual( isPalindrome("racecar"), True ) or
#       assertTrue( isPalindrome("racecar"))
# Example Test: assertFalse( isPalindrome("rabcr") ).
# Add at least 5 other test cases

# def is_palindrome(word):
#     for i in range(int(len(word)/2)):
#         if word[i] == word[len(word)-i-1]:
#             return True


# class is_palindrome_test(unittest.TestCase):
#     '''a class to test is_palindrome()'''

#     def test_one(self):
#         self.assertEqual(is_palindrome('racecar'), True)

#     def test_two(self):
#         self.assertTrue(is_palindrome('kayak'))

#     def test_three(self):
     
#         self.assertNotEqual(is_palindrome('ana'), False)

#     def test_four(self):
#         self.assertFalse(is_palindrome('banana'))


# if __name__ == '__main__':
#     unittest.main()


# unittest.main()


# 3. coins - Write a function that determines how many quarters, dimes,
# nickels, and pennies to give to a customer for a change where you minimize
# the number of coins you give out.
# Example: given 87 cents, result should be 3 qs, 1 ds, 0 ns and 2 ps
# Example Test: assertEqual( coin(87), [3,1,0,2] )
# Add at least 5 other test cases

# def coins(num):
#     count_q = 0
#     count_d = 0
#     count_n = 0
#     count_p = 0
    
#     # see how many quarters fit
#     while num >= 25:
#         num -= 25
#         count_q += 1
#     while num >= 10:
#         num -= 10
#         count_d += 1
#     while num >= 5:
#         num -= 5
#         count_n += 1
#     while num >= 1:
#         num -= 1
#         count_p += 1

#     coin_list = [count_q, count_d, count_n, count_p]
#     return coin_list


# class coins_test(unittest.TestCase):
#     '''a class to test coins()'''
#     def test_one(self):
#         self.assertEqual(coins(87), [3, 1, 0, 2])

#     def test_two(self):
#         self.assertFalse(coins(87) == [3, 1, 0, 1])

#     def test_three(self):
#         self.assertTrue(coins(87) == [3, 1, 0, 2])

#     def test_four(self):
#         self.assertNotEqual(coins(87), [3, 2, 0, 4])


# if __name__ == '__main__':
#     unittest.main()


# unittest.main()


# 4. BONUS - factorial - Write a recursive function that returns the factorial
# of a given number. Remember that the factorial of a number is the product of
# all the numbers between 1 and the given number (eg. 4! = 4*3*2*1).
# Example: factorial(5) should return 120.
# Add at least 3 test cases

# def factorial(num):
#     val = 1
#     i = num
#     while i >= 1:
#         val *= i
#         i -= 1
#     return val


# class factorial_test(unittest.TestCase):
#     '''test class for factorial()'''

#     def test_one(self):
#         self.assertEqual(factorial(5), 120)

#     def test_two(self):
#         self.assertTrue(factorial(5) == 120)


# if __name__ == '__main__':
#     unittest.main()


# unittest.main()

# 5. BONUS - fibonacci - Write a recursive function that accepts a number, n,
# and returns the nth Fibonacci number from the sequence. The first two
# Fibonacci numbers are 0 and 1. Every number after that is calculated by
# adding the previous 2 numbers from the sequence.
# (i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
# Example: fibonacci(5) should return 3 (the 5th number in the sequence is 3).
# Add at least 3 test cases

# def fibonacci(n):
    #w/out recursion:

    # fib = [0, 1]
    # for i in range(2, n):
    #     val = fib[i-1] + fib[i-2]
    #     fib.append(val)
    # return fib

    # w recursion:

def fibonacci(n):
    # w recursion:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else: 
        return (fibonacci(n-1) + fibonacci(n-2))


class fibonacci_test(unittest.TestCase):
    '''test class for fibonacci()'''
    def test_one(self):
        self.assertEqual(fibonacci(5), 3)

    def test_two(self):
        self.assertNotEqual(fibonacci(5), 11)

    def test_three(self):
        self.assertFalse(fibonacci(3) == 5)

    def test_four(self):
        self.assertTrue(fibonacci(5) == 3)


if __name__ == '__main__':
    unittest.main()


unittest.main()

