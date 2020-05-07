# 1. Biggie Size
def biggie_size(nums_list):
    for i in range(len(nums_list)):
        if nums_list[i] > 0:
            nums_list[i] = "big"
    return nums_list


print(biggie_size([-1, 3, 5, -5]))


# 2. Count Positives
def count_positives(nums_list):
    count = 0
    for i in range(len(nums_list)):
        if nums_list[i] > 0:
            count += 1
    nums_list[len(nums_list) - 1] = count
    return nums_list


print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))


# 3. Sum Total
def sum_total(nums_list):
    sum = 0
    for val in nums_list:
        sum += val
    return sum


print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))


# 4. Average
def average(nums_list):
    sum = 0
    for i in range(len(nums_list)):
        sum = sum + nums_list[i]
    average = sum / len(nums_list)
    return average


print(average([1, 2, 3, 4]))


# 5. Length
def length(nums_list):
    return len(nums_list)


print(length([37, 2, 1, -9]))
print(length([]))


# 6. Minimum
def minimum(nums_list):
    if len(nums_list) <= 0:
        return False
    else:
        min = nums_list[0]
        for i in range(len(nums_list)):
            if nums_list[i] < min:
                min = nums_list[i]
        return min


print(minimum([37, 2, 1, -9]))
print(minimum([]))


# 7. Maximum
def maximum(nums_list):
    if len(nums_list) <= 0:
        return False
    else:
        max = nums_list[0]
        for i in range(len(nums_list)):
            if nums_list[i] > max:
                max = nums_list[i]
        return max


print(maximum([37, 2, 1, -9]))
print(maximum([]))


# 8. Ultimate Analysis
def ultimate_analysis(nums_list):
    analysis = {}
    sum = sum_total(nums_list)
    min = minimum(nums_list)
    max = maximum(nums_list)
    len = length(nums_list)
    avg = average(nums_list)
    
    analysis = {
        'sumTotal': sum,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length': len
    }
    return analysis


print(ultimate_analysis([37, 2, 1, -9]))


# 9. Reverse List
def reverse_list(nums_list):
    list_length = len(nums_list)
    for i in range(int(list_length / 2)):
        temp = nums_list[i]
        nums_list[i] = nums_list[list_length - 1 - i]
        nums_list[list_length - 1 - i] = temp
    return nums_list


print(reverse_list([37, 2, 1, -9]))
