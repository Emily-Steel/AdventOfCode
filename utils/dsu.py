"""Disjoint-set-union data structure. Shamelessly stolen from: https://github.com/d1mav0lk0v/dsu_data_structure and edited for my own use."""


from collections.abc import Iterable, Hashable, Iterator
from copy import deepcopy


_Hashable = Hashable


class DSU:
    """Disjoint-set-union data structure."""


    # O(n)
    def __init__(self, iterable: Iterable[Hashable] | None = None) -> None:
        self.__dsu = dict()

        if iterable is not None:
            self.__assert_hashable_items(iterable)
            self.__dsu = {item: {item} for item in iterable}


    # O(m + n)
    def get_sets(self, *items: Iterable[Hashable]) -> list[set]:
        """Return a deep copy of the sets to which the items belong."""

        return deepcopy(self.__get_sets(*items))


    # O(n)
    def items(self) -> set:
        """Return a universal set of items from all sets."""

        return set(self.__dsu.keys())


    # O(m)
    def same(self, *items: Iterable[Hashable]) -> bool:
        """Check whether all items belong to the same set."""

        self.__assert_include_items(items)

        set_ = None

        for item in items:
            if set_ is None:
                set_ = self.__dsu[item]
            if set_ is not self.__dsu[item]:
                return False

        return True


    # O(m + n)
    def union(self, *items: Iterable[Hashable]) -> bool:
        """Union items and their sets into one set."""

        sets = self.__get_sets(*items)
        new_set = set().union(*sets) # O(n)

        for item in new_set:
            self.__dsu[item] = new_set

        return len(sets) > 1


    # O(m)
    def make(self, *items: Iterable[Hashable]) -> None:
        """Make new sets for each items."""

        self.__assert_hashable_items(items)

        for item in items:
            if item in self.__dsu:
                self.__dsu[item].discard(item)
            self.__dsu[item] = {item}


    # O(m)
    def remove_items(self, *items: Iterable[Hashable]) -> None:
        """Remove items from sets."""

        self.__assert_include_items(items)

        for item in items:
            self.__dsu[item].discard(item)
            del self.__dsu[item]


    # O(m + n)
    def remove_sets(self, *items: Iterable[Hashable]) -> None:
        """Remove sets by items included in them."""

        self.__assert_include_items(items)

        for item in items:
            set_ = self.__dsu.get(item, [])
            for set_item in set_:
                del self.__dsu[set_item]


    # O(n)
    def copy(self) -> "DSU":
        """Return a deep copy of DSU."""

        copy_dsu = DSU()
        copy_dsu.__dsu = deepcopy(self.__dsu)

        return copy_dsu


    # O(n)
    def clear(self) -> None:
        """Clear all sets."""

        self.__dsu.clear()


    # O(m)
    @staticmethod
    def __assert_hashable_items(iterable: Iterable[Hashable]) -> None:
        """Raise an error if the item is not hashable."""

        for item in iterable:
            if not isinstance(item, _Hashable):
                raise TypeError(f"unhashable type: '{type(item).__name__}'")


    # O(m)
    def __assert_include_items(self, iterable: Iterable[Hashable]) -> None:
        """Raise an error if the item is not in the sets."""

        self.__assert_hashable_items(iterable)

        for item in iterable:
            if item not in self.__dsu:
                raise KeyError(f"{item} not in '{type(self).__name__}'")


    # O(m)
    def __get_sets(self, *items: Iterable[Hashable]) -> list[set]:
        """Return the sets to which the items belongs."""

        self.__assert_include_items(items)

        id_sets = set()
        sets = list()

        for item in items:
            set_ = self.__dsu[item]
            id_ = id(set_)
            if id_ not in id_sets:
                id_sets.add(id_)
                sets.append(set_)

        return sets


    def __nonzero__(self) -> bool:
        """Check the sets empty."""

        return bool(self.__dsu)


    def __len__(self) -> int:
        """Return the number of items in the sets."""

        return len(self.__dsu)


    def __str__(self) -> str:
        """Return sets as a string."""

        return str(self.__get_sets(*self.__dsu))


    def __eq__(self, other: "DSU") -> bool:
        """Compare all sets of two DSU structures."""

        if not isinstance(other, type(self)):
            raise TypeError(
                f"'{type(self).__name__}' cannot be compared with other types"
            )

        return self.__dsu == other.__dsu


    def __contains__(self, item: Hashable) -> bool:
        """Check whether an item is contained in one of the sets."""

        self.__assert_hashable_items((item,))

        return item in self.__dsu


    def __iter__(self) -> Iterator:
        """Return an iterator over an items of the sets.
        Raise an error if the DSU size changes during iteration.
        Warning! The error is related to the dictionary."""

        # RuntimeError changed size during iteration with dict!
        yield from self.__dsu


del Iterable, Hashable, Iterator