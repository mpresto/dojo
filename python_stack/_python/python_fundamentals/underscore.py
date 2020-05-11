class Underscore:
    def map(self, iterable, callback):
        # your code here
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable

    def find(self, iterable, callback):
        # your code here
        for i in range(len(iterable)):
            if callback(iterable[i]) is True:
                return iterable[i]

    def filter(self, iterable, callback):
        # your code
        filtered = []
        for i in range(len(iterable)):
            if callback(iterable[i]) is True:
                filtered.append(iterable[i])
        return filtered

    def reject(self, iterable, callback):
        # your code
        unrejected = []
        for i in range(len(iterable)):
            if callback(iterable[i]) is False:
                unrejected.append(iterable[i])
        return unrejected


# create an instance of our class:
    # set our instance to a variable that is an underscore:
_ = Underscore()

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)    # should return [2, 4, 6] after you finish implementing the code above

print(_.map([1, 2, 3], lambda x: x * 2))                    # should return [2,4,6]
print(_.find([1, 2, 3, 4, 5, 6], lambda x: x > 4))          # should return the first value that is greater than 4
print(_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))   # should return [2,4,6]
print(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))   # should return [1,3,5]
