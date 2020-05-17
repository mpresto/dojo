class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        # self.result += num
        # for num in nums:
        #     self.result += num
        # return self
        pass

    def subtract(self, num, *nums):
        # self.result -= num
        # for num in nums:
        #     self.result -= num
        # return self
        pass


class MathDojo_Test(unittest.TestCase):
    '''a test for MathDojo'''

    def test_one(self):
        self.assertTrue()


# md = MathDojo()

# # test add():
# print(md.add(3).result)
# print(md.add(3, 5).result)
# print(md.add(3, 7, 9).result)

# # test subtract():
# print(md.subtract(3).result)
# print(md.subtract(3, 5).result)
# print(md.subtract(3, 7, 9).result)

# # test chaining:
# x = md.add(2).add(2, 5, 1).subtract(3, 2).result
# print(x)