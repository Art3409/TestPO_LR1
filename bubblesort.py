import random
import json

def generate_random_list(length):
    return [random.randint(10, 100) for _ in range(length)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def save_sorted_result(arr, filename):
    
    sorted_arr = bubble_sort(arr.copy())
    with open(filename, 'w') as f:
        json.dump(sorted_arr, f)
    return True