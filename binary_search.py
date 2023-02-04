def binary_search(lst: list, goal: int) -> int:
    start = 0
    end = len(lst) - 1

    while start <= end:
        half = int((start + end) / 2)
        guess = lst[half]

        if guess == goal:
            return half
        elif guess < goal:
            start = half + 1
        else:
            end = half - 1

    return None
