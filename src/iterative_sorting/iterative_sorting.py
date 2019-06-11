import sys

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_element = sys.maxsize
        smallest_index = i

        # Find smallest one
        for j in range(i, len(arr)):
            if arr[j] < smallest_element:
                smallest_element = arr[j]
                smallest_index = j
                
        # Swap
        element = arr[i]
        arr[i] = smallest_element
        arr[smallest_index] = element
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                element = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = element
                
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
