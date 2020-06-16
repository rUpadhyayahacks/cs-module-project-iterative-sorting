# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j


        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):

        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


    return arr


# STRETCH: implement the Count Sort function below
# The maximum arg was so we could specify the max value
# The total range of data we'll be sorting sits between 0 and maximum
def count_sort(arr, maximum=-1):
    # Your code here
    # if the arr is empty
    if len(arr) == 0:
        return arr

    # if maximum is not given, we'll take the max value from the input array
    if maximum == -1:
        maximum = max(arr)

    # make a bunch of buckets
    buckets = [0 for _ in range(maximum + 1)] # so we can capture the maximum value. Range is exclusive

    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[x] += 1

    # we have the counts of every value in our input array that we were sorting
    # loop through our buckets, starting at the smallest index
    # j keeps track of the spot we're writing to in our input array
    j = 0

    # this whole loop is reversing the tallying we did in the previous loop
    for i in range(len(buckets)): # O(max)
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1

    return arr











    # size = len(arr)
    # output = [0] * size
    # count = [0] * 10
    # for i in range(0, size):
        
    #     count[arr[i]] += 1

    # for i in range(1, 10):
    #     count[i] += count[i-1]

    # i = size - 1
    # while i >= 0:
    #     output[count[arr[i]] - 1] = arr[i]
    #     count[arr[i]] -= 1
    #     i -= 1
    
    # for i in range(0, size):
    #     arr[i] = output[i]

    # return arr

    # # create a variable 'n' set to the length of the array
    # n = len(arr)
    # # create an 'output' array of characters which will be sorted
    # # since a byte can only hold 256 different values, the maximum string length would...
    # # be 255 given that the first byte is reserved for storing the length
    # output = [0 for i in range(256)] 
    # # create a 'count' array to store the count of inidividul characters
    # count = [0 for i in range(256)] 
    # # create a 'sorted_arr' array to store and later return the sorted array
    # sorted_arr = ["" for _ in arr] 
    # # traverse through all elements in the array
    # for i in arr:
    #     # store a count of each character in the 'count' array
    #     count[i] += 1
    #     # if an element in the array is negative, return an error message string
    #     if i < 0:
    #         return 'Error, negative numbers not allowed in Count Sort' 
    # # traverse through all elements in the range of 256 possible characters and...
    # # update count[i] so that it now contains the actual position of the character in the output array 
    # for i in range(256): 
    #     count[i] += count[i - 1] 
    # # traverse through all elements in the array and build the output character array 
    # for i in range(n): 
    #     output[count[arr[i]] - 1] = arr[i] 
    #     count[arr[i]] -= 1
    # # traverse through all elements in the array and copy the 'output' array to the 'sorted_arr' array...
    # # which is our new list of sorted characters
    # for i in range(n): 
    #     sorted_arr[i] = output[i]
    # # return the 'sorted_arr' array
    # return sorted_arr