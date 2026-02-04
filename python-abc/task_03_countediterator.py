class CountedIterator:
    """
    A custom iterator that wraps any iterable and counts
    the number of items retrieved during iteration.

    Attributes:
        iterator (iterator): The underlying iterator object.
        count (int): Number of items that have been fetched.

    Methods:
        __next__(): Returns the next item and increments the counter.
        get_count(): Returns the current count of fetched items.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable (iterable): The object to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: self
        """
        return self

    def __next__(self):
        """
        Retrieve the next item from the underlying iterator.

        Increments the counter for each item fetched. Raises StopIteration
        when there are no more items.

        Returns:
            Any: The next item from the iterator.

        Raises:
            StopIteration: When the underlying iterator is exhausted.
        """
        item = next(self.iterator)  # will raise StopIteration if exhausted
        self.count += 1
        return item

    def get_count(self):
        """
        Get the number of items that have been retrieved so far.

        Returns:
            int: The count of items retrieved.
        """
        return self.count
