def stable_priority_sort(data):
    """
    Performs stable insertion sort based on priority (index 1).
    """
    n = len(data)

    for i in range(1, n):
        key = data[i]
        j = i - 1

        # Shift elements having higher priority value
        while j >= 0 and data[j][1] > key[1]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


def main():
    items = [
        ("TaskA", 2),
        ("TaskB", 1),
        ("TaskC", 2),
        ("TaskD", 1),
        ("TaskE", 3)
    ]

    print("Original List:")
    print(items)

    sorted_items = stable_priority_sort(items)

    print("\nSorted List (by priority, stable):")
    print(sorted_items)


if __name__ == "__main__":
    main()