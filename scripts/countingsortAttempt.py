# import random
# import time
import math
# max_value = 10
# min_value = 1
# array_size = 10
# print("Creating random array")
# random_array = [0] * array_size
# # biggestElement = min_value - 1
# # smallestElement = max_value + 1
# print("Populating it")


# for i in range(array_size):
#     print('\r' + f"Progress: {i/array_size*100:.2f}%", end='', flush=True)  # Clear the previous line and update progress
    
#     random_array[i] = random.randint(min_value, max_value)
#     # biggestElement = max(biggestElement, random_array[i])
#     # smallestElement = min(smallestElement, random_array[i])
# print()
# def bogoSort(arr):
#     counter = 1
#     sorted = False
#     while not sorted:
#         print('\r' + "Trying." + ('.' * (math.floor(counter) % 3)) + '  ', end='')
#         counter += 0.0002
#         sorted = True
#         for i in range(1, len(arr)):
#             if (arr[i] < arr[i - 1]):
#                 # shuffle
#                 sorted = False
#                 random.shuffle(arr)
#     print('Done!')
#     return arr
    


# # print(f"smallest: {smallestElement}, biggest: {biggestElement}")
# starting_time = time.time()
# print(f"starting time: {str(starting_time)}")
# # bucket_size = biggestElement - smallestElement + 1
# # buckets = [0] * bucket_size

# # # Count the occurrences of each element in random_array
# # for element in random_array:
# #     buckets[element - smallestElement] += 1

# # # Reconstruct the sorted array
# sorted_array = bogoSort(random_array)

# # for i, count in enumerate(buckets):
# #     sorted_array.extend([i + smallestElement] * count)

# print(f"Sorted array: {sorted_array}")
# print(f"Took {str(time.time() - starting_time)}")


def equation(x):
    return math.gamma(x) - (x**2 - 1)

def find_solution():
    # Initial values for the bisection method
    a = 1.0
    b = 3.0

    while b - a > 1e-15:  # Continue until the desired level of precision is reached
        
        mid = (a + b) / 2
        if equation(a) * equation(mid) < 0:
            b = mid
        else:
            a = mid

    return (a + b) / 2

solution = find_solution()
print(solution)