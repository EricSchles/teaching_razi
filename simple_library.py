def add(x: int, y: int):
    """
    This adds two integers together
    >>> add(5,6)
    11
    """
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("woah, this should not print")
