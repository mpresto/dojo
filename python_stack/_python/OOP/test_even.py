import unittest


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


class is_even_tests(unittest.TestCase):

    def test_two(self):
        self.assertTrue(is_even(2))

    def test_three(self):
        self.assertEqual(is_even(3), True)

    def set_up(self):
        print("Running setup")

    def tear_down(self):
        print("Tearing down")


if __name__ == '--main__':
    unittest.main()


unittest.main()