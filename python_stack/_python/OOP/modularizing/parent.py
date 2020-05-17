local_val = "magical unicorns"


def square(x):
    return x * x


class User:
    def __init__(self, name):
        self.name = name.title()

    def say_hello(self):
        return "hello"


if __name__ == "__main__":
    print("The file is being executed directly")
else:
    print("The file is being executed at at import in file:", __name__)


print(square(5))
user = User('anna')
print(user.name)
print(user.say_hello())
print(__name__)
