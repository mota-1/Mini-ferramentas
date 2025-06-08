import math
    

def calculate_divisor_counts(limit):
    # Criando uma lista para armazenar o número de divisores de cada número
    print("Criando lista enorme")
    divisor_counts = [1] * (limit + 1)
    print("Populando lista enorme\n \n")
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
limite = 10**6
print("Encontrando divisores...")
divisor_counts = calculate_divisor_counts(limite)

print("Encontrando máximo...")
biggerest = max(divisor_counts)
largest_element_index = divisor_counts.index(biggerest)
print(f"Número mais composto até {limite}: {largest_element_index}, com {biggerest} divisores")

# limit = 10**6
# anti_primes = find_anti_primes(limit)

# print("Anti-Primes up to", limit, "are:", anti_primes)
