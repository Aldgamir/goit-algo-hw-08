import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)  # перетворюємо список у купу

    total_cost = 0

    while len(cable_lengths) > 1:
        # Видаляємо два найменші елементи
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)
        
        # Об'єднуємо їх
        combined_length = shortest1 + shortest2
        
        # Додаємо витрати на з'єднання до загальних витрат
        total_cost += combined_length
        
        # Додаємо об'єднану довжину назад до купи
        heapq.heappush(cable_lengths, combined_length)
    
    return total_cost

# Задаемо довільні значення довжини кабелів
cable_lengths = [4, 3, 2, 6]
min_cost = min_cost_to_connect_cables(cable_lengths)
print("Мінімальні витрати на з'єднання кабелів:", min_cost)
