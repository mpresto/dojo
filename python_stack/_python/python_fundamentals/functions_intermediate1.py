import random


def rand_int(min=0, max=100):
    """Create a function that returns a random integer between min and max.
    Using random.random(), return a float between 0.000 and 1.000. Multiply
    the float by the max value to get a number within the 0 to max range.
    In order to clear the min value, add the min value to the returned float.
    This could push the float value over the current max value, so modify the
    equation so that the float value is multiplied by the max value minus
    the min value, instead of by the max value."""

    num = random.random() * (max - min) + min
    return round(num)


print(rand_int()) 		         # should print a random integer between 0 to 100
print(rand_int(max=50)) 	     # should print a random integer between 0 to 50
print(rand_int(min=50)) 	     # should print a random integer between 50 to 100
print(rand_int(min=50, max=20))  # where min>max, print between these two nums
print(rand_int(max=-50))         # where max<0
