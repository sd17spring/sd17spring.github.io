"""
SoftDes Spring 2017 day 10 in-class exercise: Geometry classes
"""


class Line(object):
    """A instance of this class represents a geometric line segment: a line between two points."""

    def __init__(self, x0, y0, x1, y1):
        """Initialize the instance.

        Examples:
        >>> line = Line(10, 20, 100, 200)
        >>> line.x0
        10
        >>> line.y0
        20
        """
        pass

    def __repr__(self):
        """Return a string representation. Python's `print` statement calls this method.

        Examples:
        >>> line = Line(10, 20, 100, 200)
        >>> print(line)
        Line(10, 20, 100, 200)
        """
        pass

    def top(self):
        """Return the smallest y value.

        This is the *opposite* of the convention in math. It's the standard convention in many computer window
        systems and 2D computer graphics systems -- probably because Western writing systems, except boustrophedon
        Greek and Irish runes, are written from left to right (x increases to the right) and top to bottom (y
        increases towards the ground).

        Examples:
        >>> Line(10, 20, 100, 200).top()
        20
        >>> Line(100, 200, 10, 20).top()
        20
        """
        pass

    def left(self):
        """Return the smallest x value.

        Whew.

        Examples:
        >>> Line(10, 20, 100, 200).left()
        10
        >>> Line(100, 200, 10, 20).left()
        10
        """
        pass

    def bottom(self):
        """Return the y coordinate of the bottom of the shape.

        Examples:
        >>> Line(10, 20, 100, 200).bottom()
        200
        >>> Line(100, 200, 10, 20).bottom()
        200
        """
        pass

    def right(self):
        """Return the x coordinate of the rightmost point.

        Examples:
        >>> Line(10, 20, 100, 200).right()
        100
        >>> Line(100, 200, 10, 20).right()
        100
        """
        pass

    def length(self):
        """Return the length of the line.

        Examples:
        >>> Line(10, 20, 10 + 30, 20 + 40).length()
        50.0
        """
        pass

    def is_horizontal(self):
        """Return true iff the line is horizontal.

        Examples:
        >>> Line(10, 20, 100, 20).is_horizontal()
        True
        >>> Line(10, 20, 10, 200).is_horizontal()
        False
        """
        pass

    def is_vertical(self):
        """Return true iff the line is vertical.

        Examples:
        >>> Line(10, 20, 10, 200).is_vertical()
        True
        >>> Line(10, 20, 100, 20).is_vertical()
        False
        """
        pass

    def intersection(self, other):
        """Going Beyond: Return the intersection of two lines.

        For this assignment, this only need work if `self` and `other` are
        both horizontal. This is already surprisingly difficult.

        Examples:
        # >>> Line(10, 20, 100, 20).intersection(Line(5, 20, 105, 20))
        # Line(10, 20, 100, 20)
        # >>> Line(10, 20, 100, 20).intersection(Line(5, 20, 15, 20))
        # Line(10, 20, 15, 20)
        # >>> Line(10, 20, 100, 20).intersection(Line(15, 20, 105, 20))
        # Line(15, 20, 100, 20)
        # >>> Line(10, 20, 100, 20).intersection(Line(15, 20, 95, 20))
        # Line(15, 20, 95, 20)
        # >>> Line(15, 20, 95, 20).intersection(Line(10, 20, 100, 20))
        # Line(15, 20, 95, 20)
        """
        pass


class Rect(object):
    """An instance of this class represents a geometric rectangle."""

    def __init__(self, x0, y0, x1, y1):
        """Initialize the instance."""
        pass

    def __str__(self):
        """Return a human-readable string that describes the instance.

        Examples:
        >>> rect = Rect(10, 20, 100, 200)
        >>> print(rect)
        Rect(10, 20, 100, 200)
        """
        pass

    def width(self):
        """Return the shape's width.

        Examples:
        >>> Rect(10, 20, 100, 200).width()
        90
        >>> Rect(100, 200, 10, 20).width()
        90
        """
        pass

    def height(self):
        """Return the shape's height.

        Examples:
        >>> Rect(10, 20, 100, 200).height()
        180
        >>> Rect(100, 200, 10, 20).height()
        180
        """
        pass

    def area(self):
        """Return the shape's area.

        Examples:
        >>> Rect(10, 20, 100, 200).area()
        16200
        """
        pass

    def bbox(self):
        """Return this shape's bounding box.

        The bounding box is the smallest practically-computable rectangle that contains all
        the points in this shape's interior. For a rectangle, its bounding box is itself. The bounding box is a
        fundamental graphics concept. The Going Beyond exercise illustrates one way this method is helpful.
        """
        return self

    def contains_pt(self, x0, y0):
        """Return true iff this rectangle contains the point (x0, y0).

        Examples:
        >>> Rect(10, 20, 100, 200).contains_pt(5, 5)
        False
        >>> Rect(10, 20, 100, 200).contains_pt(50, 50)
        True
        >>> Rect(10, 20, 100, 200).contains_pt(5, 50)
        False
        >>> Rect(10, 20, 100, 200).contains_pt(50, 5)
        False
        >>> Rect(10, 20, 100, 200).contains_pt(50, 300)
        False
        >>> Rect(100, 200, 10, 20).contains_pt(50, 50)
        True
        """
        pass

    def intersection(self):
        """Going Beyond: intersection. `self` is another instance of `Rect`.

        Examples:
        # >>> Rect(10, 20, 100, 200).intersection(Rect(15, 25, 90, 180))
        # Rect(15, 25, 90, 180)
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # doctest.run_docstring_examples(Line.__repr__, globals())
