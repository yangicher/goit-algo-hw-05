def binary_search(arr, x):
    low = 0
    mid = 0
    high = len(arr) - 1
    upper_bound = arr[-1]  
    iterations = 0  

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return iterations, arr[mid]

        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            upper_bound = arr[mid]

    return iterations, upper_bound