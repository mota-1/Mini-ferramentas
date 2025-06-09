from ajudantes.loop_calculando import start_calculating_message
def calculate_divisor_counts(limit):
    # Criando uma lista para armazenar o número de divisores de cada número
    print("Criando lista enorme")
    divisor_counts = [1] * (limit + 1) # poderia ser bem mais rápido ao inicializar com 2, e o j com 2 também
    print("Populando lista enorme")
    stop_event = start_calculating_message("Encontrando divisores")
    for i in range(2, limit + 1):
        for j in range(i, limit + 1, i):
            divisor_counts[j] += 1
    stop_event.set()
    print('')
        

    return divisor_counts

limit = 10**6


divisor_counts = calculate_divisor_counts(limit)


biggerest = max(divisor_counts)

largest_element_index = divisor_counts.index(biggerest)
print(f"Número mais composto até {limit}: {largest_element_index}, com {biggerest} divisores")