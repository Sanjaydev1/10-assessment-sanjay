from graph_utils import bfs_shortest_path_length


def test_reachable_path():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": []
    }

    result = bfs_shortest_path_length(graph, "A", "D")

    assert result == 2


def test_unreachable_path():
    graph = {
        "A": ["B"],
        "B": [],
        "C": []
    }

    result = bfs_shortest_path_length(graph, "A", "C")

    assert result == -1

def test_graph_with_cycle():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]
    }

    result = bfs_shortest_path_length(graph, "A", "C")

    assert result == 2