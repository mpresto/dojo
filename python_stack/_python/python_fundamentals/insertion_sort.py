# Insertion Sort
'''Compare value of current index to value at following index. If value of
following index is less than value at current index, pop the following index. 
Compare popped value to value at each index from start of array to current 
index. If popped value is greater than index value, compare to next index value.
Continue until popped value is <= value at the next index. Then insert popped
value before this index. Increment current index by 1 and repeat.'''


sort_me = [6, 5, 3, 1, 8, 7, 2, 4]


def insertion_sort(arr):

    # sort each idx in array
    for i in range(len(arr)):

        # set current index value
        curr_idx = i
        print("current idx:", curr_idx)

        # compare current idx val to next values in array
        for j in range(i+1, len(arr)):
            print("j:", j)

            # compare values:
            if arr[curr_idx] > arr[j]:
                popped = arr.pop(arr[j])
                print("popped:", popped)
            
                # for k in range(curr_idx, 0, -1):
                #     print("k", k)
                #     # if popped < arr[curr_idx-k]:
                #     #     arr.insert(curr_idx-k-1, popped)


print(insertion_sort(sort_me))

# list.insert(index, element)

# SOLUTION:

# my_arr = [9,3,78,12,76,0,-2]

# for idx in range(1, len(my_arr)): 
#     temp = my_arr[idx] 
#     prev_idx = idx-1
#     while prev_idx >= 0 and temp < my_arr[prev_idx]: 
#         my_arr[prev_idx + 1] = my_arr[prev_idx] 
#         prev_idx -= 1
#     my_arr[prev_idx + 1] = temp 

# print(my_arr)