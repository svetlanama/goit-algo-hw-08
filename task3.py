import heapq

def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths or len(cable_lengths) < 2:
        return 0

    # Створюємо міні-купу з усіх довжин кабелів
    heapq.heapify(cable_lengths)

    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Витягуємо два найменші кабелі
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)

        # Об'єднуємо їх, додаємо вартість до загальної
        current_cost = cable1 + cable2
        total_cost += current_cost

        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cable_lengths, current_cost)

    return total_cost


if __name__ == "__main__":
    cable_lengths1 = [4, 3, 2, 6]
    min_cost1 = min_cost_to_connect_cables(cable_lengths1)
    print(f"Мінімальна вартість з'єднання кабелів {cable_lengths1}: {min_cost1}")  # Очікується: 29

    cable_lengths2 = [1, 2, 3, 4, 5]
    min_cost2 = min_cost_to_connect_cables(cable_lengths2)
    print(f"Мінімальна вартість з'єднання кабелів {cable_lengths2}: {min_cost2}")  # Очікується: 33

    cable_lengths3 = [1, 1, 1]
    min_cost3 = min_cost_to_connect_cables(cable_lengths3)
    print(f"Мінімальна вартість з'єднання кабелів {cable_lengths3}: {min_cost3}")  # Очікується: 6

    cable_lengths4 = []
    min_cost4 = min_cost_to_connect_cables(cable_lengths4)
    print(f"Мінімальна вартість з'єднання кабелів {cable_lengths4}: {min_cost4}")  # Очікується: 0

    cable_lengths5 = [7]
    min_cost5 = min_cost_to_connect_cables(cable_lengths5)
    print(f"Мінімальна вартість з'єднання кабелів {cable_lengths5}: {min_cost5}")  # Очікується: 0
