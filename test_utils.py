from utils import summarize, normalize_names


def test_summarize():
    result = summarize([1, 2, 3, 4, 5])

    assert result["min"] == 1
    assert result["max"] == 5
    assert result["avg"] == 3.0
    assert result["count_above_avg"] == 2


def test_normalize_names():
    result = normalize_names(
        [" sanjay ", "SANJAY", "john", "John"]
    )

    assert set(result) == {"Sanjay", "John"}