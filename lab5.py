purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    return sum(purchase["quantity"]*purchase["price"] for purchase in purchases)

print(f"Общая выручка: {total_revenue(purchases)}")


def items_by_category(purchases):
    result = {}

    for purchase in purchases:
        category = purchase["category"]
        item = purchase["item"]

        if category not in result:
            result[category] = set()

        result[category].add(item)

    # преобразуем множества в списки
    return {category: list(items) for category, items in result.items()}

print(f"Товары по категориям: {items_by_category(purchases)}")


def expensive_purchases(purchases):
    result = []
    min_price = min(p["price"] for p in purchases)

    for purchase in purchases:
        if purchase["price"] >= min_price:
            result.append(purchase)

    return result, min_price

expensive, min_price = expensive_purchases(purchases)
print(f"Покупки дороже {min_price}: {expensive}")


def average_price_by_category(purchases):
    result = {}

    for purchase in purchases:
        category = purchase["category"]
        price = purchase["price"]

        if category not in result:
            result[category] = []

        result[category].append(price)

    # считаем среднее
    return {
        category: sum(prices) / len(prices)
        for category, prices in result.items()
    }

print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")


def most_frequent_category(purchases):
    result = {}

    for purchase in purchases:
        category = purchase["category"]
        quantity = purchase["quantity"]

        if category not in result:
            result[category] = 0

        result[category] += quantity  # суммируем

    # возвращаем категорию с максимальным количеством
    return max(result, key=result.get)

print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")
