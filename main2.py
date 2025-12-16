def get_min(nums):
    """Return the minimum value from the list, or None for empty list."""
    if not nums:
        return None
    return min(nums)


def sum_and_avg(nums):
    """Return tuple (sum, avg) for a list of numbers. avg is None for empty list."""
    if not nums:
        return 0, None
    total = sum(nums)
    avg = total / len(nums)
    return total, avg


def square_list(numbers):
    """Return a new list with each number squared."""
    return [n * n for n in numbers]


def remove_spaces(sent):
    """Return string with spaces removed."""
    return sent.replace(" ", "")


def find_index(lst, val):
    """Return index of val in lst or -1 if not found."""
    try:
        return lst.index(val)
    except ValueError:
        return -1


def swap_values(a, b):
    """Return values swapped as a tuple (b, a)."""
    return b, a


def make_string(values, sep=""):
    """Create a string by concatenating items in `values`.

    - Converts each item to `str` and joins using `sep`.
    - If a single value (not iterable except str) is provided, returns its string form.
    """
    if isinstance(values, str):
        return values

    try:
        iterator = iter(values)
    except TypeError:
        return str(values)

    return sep.join(str(v) for v in iterator)


def main():
    nums = [2, 3, 5, 6, 5, 4, 4, 6, 8, 7]
    nums.sort()

    minimum = get_min(nums)
    total, avg = sum_and_avg(nums)

    print("this is the minimum of this num =", minimum)
    print("this is the sum of this num =", total)
    print("this is the average =", avg)

    # Example: square a list
    numbers = [1, 2, 3, 4, 5]
    squares = square_list(numbers)
    print("squares:", squares)

    # Example: remove spaces from a sentence
    sent = "ram and sham is a good brothers, and also the best friends also."
    sent_no_spaces = remove_spaces(sent)
    print("no-spaces sentence:", sent_no_spaces)

    # Example: find index
    charr = ["a", "b", "c"]
    print("index of 'a' in charr:", find_index(charr, "a"))

    # Example: swap values
    a = 5
    b = 10
    a, b = swap_values(a, b)
    print(a, b)

    # Example: make_string
    print("make_string from chars:", make_string(charr))
    print("make_string from numbers with comma:", make_string(numbers, sep=","))


if __name__ == "__main__":
    main()


