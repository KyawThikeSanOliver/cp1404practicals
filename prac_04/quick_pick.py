import random

MIN_NUMBER_PICKS = 1
MAX_NUMBER_IN_LINE = 6
MAX = 45
MIN = 0


def main():
    quick_picks = get_quick_picks()

    for i in range(quick_picks):
        the_picks = []
        for j in range(MAX_NUMBER_IN_LINE):
            number = random.randint(MIN, MAX)
            while number in the_picks:
                number = random.randint(MIN, MAX)
            the_picks.append(number)
        the_picks.sort()
        print(" ".join(f"{number:2}" for number in the_picks))


def get_quick_picks():
    """Getting quick pick and validating input """
    quick_picks = int(input("How many quick picks?:"))
    while quick_picks < MIN_NUMBER_PICKS:
        print("The quick picks should be at least 1")
        quick_picks = int(input("How many quick picks?:"))
    return quick_picks


if __name__ == "__main__":
    main()

main()
