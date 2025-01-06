from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from lst and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains:
            - a sequence from lst,
            - the length of the sequence.
    """
    return [(i, len(i)) for i in lst]
