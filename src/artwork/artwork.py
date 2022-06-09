from typing import List
import numpy as np

from .sensor import Sensor

def they_overlap(s1: Sensor, s2: Sensor) -> bool:
    radius = (s1.range + s2.range) ** 2
    distance = (s2.x - s1.x) ** 2 + (s2.y - s1.y) ** 2
    return distance <= radius


def paint_can_be_stolen(sensors: List[Sensor], m: int, n: int) -> bool:
    k = len(sensors)
    adjacency_matrix = np.zeros((k + 2, k + 2))

    for i, s in enumerate(sensors):
        if (s.y <= s.range) or (s.x + s.range >= m):
            adjacency_matrix[i + 2, 0] = 1
            adjacency_matrix[0, i + 2] = 1
        if (s.x <= s.range) or (s.y + s.range >= n):
            adjacency_matrix[i + 2, 1] = 1;
            adjacency_matrix[1, i + 2] = 1;

    for i in range(k):
        for j in range(i + 1, k):
            if they_overlap(sensors[i], sensors[j]):
                adjacency_matrix[i + 2, j + 2] = 1;
                adjacency_matrix[j + 2, i + 2] = 1;

    blocked = False
    discovered = [0] * (k + 2)

    i, j = 0, 1
    while j < k + 2 and i < k + 2:
        if adjacency_matrix[i, j]:
            if j == 1:
                blocked = True
                break
            elif not discovered[j]:
                discovered[j] = 1
                i = j
                j = 0
        j += 1

    return not blocked
