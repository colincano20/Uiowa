def selsort(L):
    for i in range(len(L) - 1):
        J = i + L[i:].index(min(L[i:]))
        L[i], L[j] = L[j], L[i]

def find_max(numbers):
    if numbers == []:  #Edge case: empty list
        return None
    
    max_value = numbers[0]  # Start by assuming the first number is the largest
    for num in numbers:
        if num > max_value:  # If a number is larger, update max_value
            max_value = num
    return max_value  # Return the largest value


import random

# Function to check if the list is sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Bogosort implementation
def bogosort(arr):
    attempts = 0
    # Continue shuffling until the array is sorted
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    print(f"Sorted in {attempts} attempts!")
    return arr

# Example usage (commented out to avoid execution)
# arr = [3, 2, 5, 1, 4]
# print("Unsorted array:", arr)
# sorted_arr = bogosort(arr)
# print("Sorted array:", sorted_arr)
