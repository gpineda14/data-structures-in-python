def binarySearch(arr, target, low, high):
    # Return True if target is found on arr
    if low > high:
        return False # if low > high, then list is empty, so no match
    else:
        # find midpoint of arr
        mid = (low + high) // 2
        if target == data[mid]:
            return True # match is found
        elif target < data[mid]:
            # recurse on left portion
            return binarySearch(arr, target, low, mid - 1)
        else:
            # recurse on right portion
            return binarySearch(arr, target, mid + 1, high)
