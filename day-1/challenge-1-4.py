def collatzConjecture(n: int, tries=0) -> int:
    if n < 1:
        return tries
    elif n == 1:
        return tries

    tries += 1

    if n % 2 == 0:
        return collatzConjecture(int(n / 2), tries)

    return collatzConjecture((n * 3) + 1, tries)


print(collatzConjecture(671))
