# 1. Countdown
def countdown(num):
    list = []
    for i in range(num, 0, -1):
        list.append(i)
    return(list)


print(countdown(5))


# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return(list[1])


print(print_and_return([1, 2]))


# 3. First Plus Length
def first_plus_length(arr):
    sum = arr[0] + len(arr)
    return sum


print(first_plus_length([1, 2, 3, 4, 5]))


# 4. Values Greater than Second
def greater_than_second(arr):
    new_arr = []
    count = 0
    if len(arr) < 2:
        return False
    else:
        for i in range(len(arr)):
            if arr[i] > arr[1]:
                count += 1
                new_arr.append(arr[i])
    print(count)
    return new_arr


print(greater_than_second([5, 2, 3, 2, 1, 4]))
print(greater_than_second([3]))


# 5. This Length, That Value
def length_and_value(s, v):
    list = []
    for i in range(s):
        list.append(v)
    return list


print(length_and_value(4, 7))
print(length_and_value(6, 2))


