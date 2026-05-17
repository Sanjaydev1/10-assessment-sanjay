def summarize(numbers: list[int]) -> dict:
    avg = sum(numbers) / len(numbers)

    count_above_avg = 0

    for number in numbers:
        if number > avg:
            count_above_avg += 1

    return {
        "min": min(numbers),
        "max": max(numbers),
        "avg": avg,
        "count_above_avg": count_above_avg
    }

def normalize_names(names: list[str]) -> list[str]:
    normalized = set()

    for name in names:
        cleaned_name = name.strip().title()
        normalized.add(cleaned_name)

    return list(normalized)

print(
    normalize_names(
        [" sanjay ", "SANJAY", "john", "John"]
    )
)

print(summarize([1, 2, 3, 4, 5]))