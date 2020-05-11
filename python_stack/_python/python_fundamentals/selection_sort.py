# Selection Sort:
'''Start at first position and iterate over array, looking for min. When min
found, swap values of min and current index. Increment index by 1 and repeat
for each index in array.'''

sort_me = [8, 1, 5, 3, -2, 0, 9, 3, 2]


def selection_sort(arr):
    # repeat for each idx in array
    for i in range(len(arr)):

        # store current min's index position:
        min_idx = i

        # iterate over remaining array looking for new min
        for j in range(i+1, len(arr)):

            # if value is less than min, save as new min_idx
            if arr[min_idx] > arr[j]:
                min_idx = j

        # swap value of current idx and min_idx:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    # return sorted array!
    return(arr)


selection_sort(sort_me)
