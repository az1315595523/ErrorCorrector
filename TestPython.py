import math
import random
from typing import List


class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.color = "red"

    def area(self) -> float:
        return math.pi * self.radius ** 2


def calculate_stats(numbers: List[float]) -> dict:
    total = 0.0
    count = len(numbers)
    max_num = float('-inf')
    min_num = float('inf')

    for num in numbers:
        total += num
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    average = total / count if count > 0 else 0
    return {
        "average": average,
        "max": max_num,
        "min": min_num,
        "sum": total
    }


def main():
    data = [random.uniform(1.0, 100.0) for _ in range(10)]

    stats = calculate_stats(data)
    print(f"Statistics: {stats}")

    if stats["max"] > 50 and stats["min"] < 20:
        print("Condition met!")
    else:
        print("Condition not met.")

    circle = Circle(stats["average"])
    print(f"Circle area: {circle.area()}")


main()
