import sys
import math
# def calculate_domino_pieces(x):
#     domino_set = set()
#     for i in range(x + 1):
#         for j in range(i, x + 1):
#             domino_set.add((i, j))
#     return domino_set, len(domino_set)

# x = int(input("Enter the value of x: "))
# domino_set, num_pieces = calculate_domino_pieces(x)

# print(f"\nThe number of pieces in the set is: {num_pieces}")
    

def calculate_divisor_counts(limit):
    # Initialize a list to store the count of divisors for each number
    print("Creating gigantic fucking array")
    divisor_counts = [1] * (limit + 1)
    print("Populating gigantic fucking array \n \n")
    squore = math.sqrt(limit)
    for i in range(2, limit + 1):
        # sys.stdout.write(f'\033[1A')
        # sys.stdout.write('\r')
        # print(f"Progress: {(i/limit * 100):.2f}%. i={i}", end='\n')
        
        for j in range(i, limit + 1, i):
            # if i < squore:
            #     print(f"\rProgress of {i}: {(j/limit * 100):.2f}%. j={j}   ", end='')
            divisor_counts[j] += 1
        # print()

    return divisor_counts
# 31.13
limit = 10**6
print("finding divisors...")
divisor_counts = calculate_divisor_counts(limit)

print("finding maximum...")
biggerest = max(divisor_counts)
largest_element_index = divisor_counts.index(biggerest)
print(f"Most composite number up to {limit}: {largest_element_index}, with {biggerest} divisors")

# limit = 10**6
# anti_primes = find_anti_primes(limit)

# print("Anti-Primes up to", limit, "are:", anti_primes)
