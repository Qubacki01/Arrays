###
#
#


def second_largest(arr):    # Second largest element in an array
    if len(arr) < 2:        # Check if arr has multiple elem
        raise ValueError("Array must have at least two elements.")
    
    largest = None      # No value
    second_largest = None
    
    for num in arr:                             # If num > larg = move to
        if largest is None or num > largest:    # largest and largest to 
            second_largest = largest            # second larg
            largest = num                   
        elif second_largest is None or num > second_largest:
            second_largest = num
            
    return second_largest



def difference_largest_smallest(arr):   # Difference between the largest and smallest values in the array
    if len(arr) < 2:
        raise ValueError("Array must have at least two elements.")
    
    largest = arr[0]
    smallest = arr[0]
    
    for num in arr:              
        if num > largest:       
            largest = num       
        if num < smallest:
            smallest = num
    
    return largest - smallest



def median(arr):    # Median of numbers in an array
    if len(arr) == 0:
        raise ValueError("Array must have at least one element.")
    

    for i in range(len(arr)):       
        for j in range(i + 1, len(arr)):    # Starts from after 'i' to last index
            if arr[i] > arr[j]:             
                arr[i], arr[j] = arr[j], arr[i]  # Swap if true
    
    
    n = len(arr)
    middle = n // 2
    
    if n % 2 != 0:          # If length of array is odd, return middle elem
        return arr[middle]
    else:
        return (arr[middle - 1] + arr[middle]) / 2  # Else return the average of 2 middle elements



def smallest_largest(arr):  # Array containing the smallest and largest values in an array
    if len(arr) < 2:
        raise ValueError("Array must have at least two elements.")
    
    largest = arr[0]
    smallest = arr[0]
    
    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    return [smallest, largest]



def array_to_string(arr):   # String separated by the minus sign
    return "-".join(str(x) for x in arr)
