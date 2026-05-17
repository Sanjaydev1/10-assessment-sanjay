from collections import deque


def bfs_shortest_path_length(graph, start, target):
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        current_node, distance = queue.popleft()

        if current_node == target:
            return distance

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                queue.append((neighbor, distance + 1))

    return -1

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print(
    bfs_shortest_path_length(graph, "A", "D")
)