# Gabriel Luo, Erica Liu
# Mar. 2020, University of Michigan.
# Math 389 Knot Research Project amidst a pandemic.
from __future__ import annotations
from typing import List

''' Every point in the graph (Erica Ver.) is denoted by a pair (m, n).
    The first value m denotes the id of the square,
    the second value n denotes which corner of the square (0, 1, 2 or 3)
'''


class UnorderedPair:
    def __init__(self, elt1, elt2):
        self.elt1 = elt1
        self.elt2 = elt2

    def __eq__(self, other: UnorderedPair):
        """Represent unordered-ness"""
        return (self.elt1 == other.elt1 and self.elt2 == other.elt2) or \
               (self.elt2 == other.elt1 and self.elt1 == other.elt2)

    def __ne__(self, other):
        return not self == other

    def __contains__(self, item):
        return item == self.elt1 or item == self.elt2

    def items(self):
        return {self.elt1, self.elt2}


class Square:
    """One Square represents a crossing: 1 and 3 makes the under-crossing, 2 and 0 makes the over-crossing"""
    """  3   0 
           /
         2   1 """
    def __init__(self, _id: int):
        self.id = _id
        self.zero = (self.id, 0)
        self.one = (self.id, 1)
        self.two = (self.id, 2)
        self.three = (self.id, 3)

    def __str__(self):
        return f"Square {self.id}"

    def __repr__(self):
        return self.__str__()


class Edge:
    """Unordered Inter-Square Edge"""
    def __init__(self, corner1: tuple, corner2: tuple):
        self.endpoints = UnorderedPair(corner1, corner2)

    def __eq__(self, other: Edge):
        return self.endpoints == other.endpoints


class Projection:
    square_list: List[Square]
    inter_square_edges: List[Edge]

    def __init__(self, squares, edges):
        self.square_list = squares
        self.inter_square_edges = edges


def is_valid_projection(proj: Projection):
    """check the necessary condition for the projection to be valid"""
    """every square corner must appear in the edge list exactly once"""
    for square in proj.square_list:
        for corner in [square.zero, square.one, square.two, square.three]:
            contained_in_edge_list = False
            for edge in proj.inter_square_edges:
                if corner in edge:
                    if contained_in_edge_list:
                        raise ValueError(f"corner: {corner} connects to more than one edge.")
                    else:
                        contained_in_edge_list = True

            if not contained_in_edge_list:
                raise ValueError(f"corner: {corner} does not connect to any other corners.")
    print(f"The projection with {proj.square_list} is checked. It does not violate obvious restrictions.")


def main():
    s1 = Square(1)
    s2 = Square(2)
    s3 = Square(3)
    trefoil_left = Projection(
        [s1, s2, s3],
        [
            (s1.zero, s3.one),
            (s1.one, s2.zero),
            (s1.two, s2.three),
            (s1.three, s3.two),
            (s2.one, s3.zero),
            (s2.two, s3.three)
        ]
    )
    is_valid_projection(trefoil_left)


if __name__ == '__main__':
    main()

