#!/usr/bin/env python


class NoSuchElementError(Exception):
    """Captures an exception that indicates that an element is not present.

    Here for utility and also to show custom exceptions.

    """

    def __init__(self, message):
        """Create the exception object using the superclass constructor."""
        super(NoSuchElementError, self).__init__(message)


class Node(object):
    """Encapsulates the structure of a Node for a doubly-linked list."""

    def __init__(self, contents=None):
        """Initializes a Node object.

        Creates object with fields _contents, _next, and _prev. The variable
        _contents is initialized with the value of the contents argument, or
        None if no argument is provided. The variables _next and _prev are
        set to None.

        """
        self._contents = contents
        self._next = None
        self._prev = None

    def __str__(self):
        """Returns a string representation of _contents.

        Returns a string representation of _contents; simply use str()
        on whatever _contents refers to.

        """
        return str(self._contents)


class ListIterator(object):
    """Encapsulates a forward-traversing iterator for a doubly-linked list."""

    def __init__(self, entry):
        """Initializes the iterator object.

        Creates an instance variable _current and sets its value to entry.

        """
        self._current = entry

    def __iter__(self):
        """Returns a reference to this object (self)."""
        return self

    def next(self):
        """Returns contents of _current node and changes _current to the next node.

        If _current node is None, raises a StopIteration exception.

        """
        if self._current is None:
            raise StopIteration
        else:
            contents = self._current._contents
            self._current = self._current._next
            return contents


class ReverseListIterator(object):
    """Encapsulates a reverse iterator for a doubly-linked list.

    This has the same basic protocol as our forward-reading iterator, but
    expects _current to begin at the last node in the list (tne pointer to this
    node is passed into this method by the __reversed__ method). Calls to 
    next() move _current to the previous node, in order to implement reverse
    traversal.

    """

    def __init__(self, entry):
        """Initializes the iterator object.

        Creates an instance variable _current and sets its value to the
        entry argument.

        """
        self._current = entry

    def __iter__(self):
        """Returns a reference to this object (self)."""
        return self

    def next(self):
        """Returns contents of _current node and changes _current to be the
        previous node in the list.

        If _current node is None, raises a StopIteration exception.

        """
        if self._current is None:
            raise StopIteration
        else:
            contents = self._current._contents
            self._current = self._current._prev
            return contents


class LinkedList(object):
    """Encapsulates a doubly-linked list."""

    def __init__(self):
        """Initializes a LinkedList object.

        Creates object with fields _first and _last initialized to None, and
        _count initialized to 0.

        """
        self._first = None
        self._last = None
        self._count = 0

    def __len__(self):
        """Returns the number of nodes in the list using _count."""
        while not self is None:
            self._count += 1

        if self._count == 0:
            return True
        return False

    def is_empty(self):
        """Returns True if the list contains no nodes."""
        if self._count == 0:
            return True

    def __iter__(self):
        """Returns an iterator object.

        Creates an iterator object using the ListIterator class constructor
        with _first as the argument.

        """
        return ListIterator(self._first)

    def __reversed__(self):
        """Returns a reverse-traversing iterator.

        Creates a ReverseListIterator object with _last as the argument to that
        class's constructor.

        """
        return ReverseListIterator(self._last)

    def __str__(self):
        """Returns a string representation of the list.

        The string should begin with "[", end with "]", and display the
        contents of each node using the Node class __str__ method. Each item
        should be separated by a comma.

        Examples: "[]", "[1, 2, hello]" (without the quotes, of course)

        Hint: You can use the iterator support you've already built for
        easy traversal through the list.

        """
        lst = []

        p = self._first
        while not p is None:
            lst.append(p._contents)
            p = p._next

        return str(lst)

    def rev_str(self):
        """Returns a string representation of the list, in reverse order.

        Other than the order of elements, uses the same conventions as __str__.

        Hint: You can build this string directly, or you can use the reverse
        iterator support you've already created.

        """
        lst = []
        p = self._last
        while not pointer is None:
            lst.append(p._contents)
            p = p._prev
        return str(lst)

    def __eq__(self, other):
        """Determines list equality, based on the contents of nodes.

        Returns True if and only if the two lists are of equal length and
        the contents of all their nodes are equal, and returns False otherwise.
        Make sure to use the == operator directly on the node _contents, since
        this library hasn't overriden the __eq__ method for the Node class.

        Note: This is a tricky one; take your time and carefully consider the
        various cases that need to be accounted for.

        """
        if self._count != other._count:
            return False
        else:
            #value = True
            node = self._first
            other_node = other._first
            while not node is None:
                if node._contents != other_node._contents:
                    return False
                node = node._next
                other_node = other_node._next
            return True

    def add_first(self, contents):
        """Adds a new Node containing contents in the first list position."""
        n = Node(contents)
        if self.is_empty():
            self._first = n
            self._last = n
        else:
            self._first._prev = n
            n._next = self._first
            self._first = n

        self._count += 1

    def add_last(self, contents):
        """Adds a new Node containing contents in the last list position."""
        n = Node(contents)
        if self.is_empty():
            self._first = n
            self._last = n
        else:
            self._last._next = n
            n._prev = self._last
            self._last = n
        self._count += 1

    def remove_first(self):
        """Returns the contents of the first node in the list and removes it.

        If the list is empty, raises NoSuchElementError. Otherwise, it removes
        the first node in the linked list and returns the removed node's
        contents.

        """
        if self.is_empty():
            raise NoSuchElementError()
        elif self._count == 1 and self._first is self._last:
            value = self._last._contents
            self._first = None
            self._last = None
            self._count -= 1
            return value
        else:
            value = self._first
            self._count -= 1
            self._first._prev._next = None
            temp = self._first._prev
            self._first._prev = None
            self._first = temp
            return value

    def remove_last(self):
        """Returns the contents of the last node in the list and removes it.

        If the list is empty, raises NoSuchElementError. Otherwise, it removes
        the last node in the linked list and returns the removed node's
        contents.

        """
        if self.is_empty():
            raise NoSuchElementError()
        elif self._count == 1 and self._first is self._last:
            value = self._last._contents
            self._first = None
            self._last = None
            self._count -= 1
            return value
        else:
            value = self._last
            self._count -= 1
            self._last._prev._next = None
            temp = self._last._prev
            self._last._prev = None
            self._last = temp
            return value

    def copy(self):
        """Returns a (shallow) copy of the list.

        If the list is empty, a new empty list should be returned. Otherwise,
        the copy should begin with the _first node of this list and create
        new node objects for the contents of the list being copied.

        Hint: You can reuse the add_first or add_last methods you've already
        created very easily for this method.

        Note: A shallow copy -- in this context -- means that we create new
        objects for the list and node structures of the new list being created
        for the copy, but we don't create new objects of the contents of nodes.

        """
        lst = LinkedList()
        for i in self:
            lst.add_last(i)
        return lst

    def append(self, other):
        """Appends a copy of other to this list.

        After the call to this method, the contents of this list should be
        all of its original nodes with copies of the nodes from other appended
        to the tail end. If other is empty, then this list should not be
        modified.

        If other is not a list, then a new node should be added to the end of
        the list with other as its contents.

        Hint: You can tell if something is a list by trying to treat it as one
        (attempting to access an expected field or method, for example) and
        seeing if an AttributeError exception is raised.

        Double Hint: The copy method you've already created gives you an easy
        way to create copies of all of a list's nodes.

        """
        if isinstance(other, LinkedList):
            for i in other:
                self.add_last(i)
        else:
            self.add_last(other)

    # Note:
    # The following 4 methods allow this class to support the core operations
    # expected of Python containers by implementing the protocols defined for
    # the __getitem__, __setitem__, __delitem__, and __contains__. The only
    # big thing missing is support for slicing, which would add a bit more
    # complexity we can omit for now. These methods are a really good example of
    # how overriding methods can be used to integrate your custom classes
    # into Python's overall design to match the behavior of built-in classes.

    def __getitem__(self, index):
        """Returns the contents of the node at position index.

        This method is one of those called when using the bracket notation in
        Python. For example:

        print(list_name[4])

        is really equivalent to:

        print(list_name.__getitem__(4))

        This method will let us access a specific index in our list in the same
        way that we do with Python lists, though at worse complexity.

        For the sake of consistency with the standard Python interaction
        protocol and indexing, the _first node's index is 0. If the argument
        passed to index is not an integer value, then this method should
        raise a TypeError exception. If index is an integer outside the valid
        range for this list, then this method should raise an IndexError
        exception. This method should not support negative indexes, and should
        raise an IndexError if index is a negative number.

        Hint: There are a variety of ways to check whether a value is an integer
        or not, such as what you have to do here for index. The most Pythonic
        way is to try and use the value in an operation that demands an integer,
        such as the built-in range() function, and catching the resulting
        exceptions. For example, see what happens when executing:

        range("hello") or range(4.5877)

        If that code, for example, throws an exception, then you can
        catch that exception in this method and that's your indication that you
        need to raise the TypeError expected of this method with a linked list
        specific error message.

        You can also look into using the built-in isinstance function, but
        that's a little less Pythonic. For example:

        isinstance(index, (int, long))

        will return True if and only if index is an arbitrarily large integer
        value.

        For the IndexError, just check to see if index is within the valid range
        for this linked list before continuing with your algorithm for finding
        the node that corresponds to index -- raise an IndexError exception with
        a useful message if index is not within this valid range.

        """
        if not isinstance(index, int):
            raise TypeError
        if index < 0 or index >= self._count:
            raise IndexError
        ind = 0
        curr = self._first
        while ind < index:
            curr = self._next
            ind += 1
        return curr._contents

    def __setitem__(self, index, value):
        """Sets the contents of the node at position index to value.

        Follows the same indexing and exception conventions as __getitem__.

        Hint: The code for __setitem__ should be remarkably similar to that of
        __getitem__.

        """
        if not isinstance(index, int):
            raise TypeError
        if index < 0:
            raise IndexError
        ind = 0
        curr = self._last
        while ind > index:
            curr = self._prev
            ind += 1
        return curr._contents

    def __delitem__(self, index):
        """Deletes the node at position index.

        This method is what is called when using the del keyword with the
        bracket notation for lists. For example:

        del list_name[3]

        is really equivalent to:

        list_name.__delitem__(3)

        The method follows the same indexing and exception conventions as
        __getitem__. Carefully consider the different cases for the position of
        the node being removed, and I suggest that you reuse existing methods
        for at least some of these cases -- that way, your well-tested existing
        methods cover cases that you don't need to test for again.

        Note: This might very well be the trickiest of all the methods in this
        assignment. Take your time and think it through carefully.

        """
        if not isinstance(index, int):
            raise TypeError
        if index < 0 or self._count <= index:
            raise IndexError
        if index == 0:
            self.remove_first()
        elif index == self._count - 1:
            self.remove_last()
        else:
            num = 1
            current = self._first._next
            while current < index:
                current = current._next
                num += 1
            current._next._prev = current._prev
            current._prev._next = current._next
            current._next = None
            current._prev = None
            current._contents = None
            self._count -= 1

    def __contains__(self, item):
        """Returns True if item is in the linked list.

        This method is called when using the in keyword to examine a container.
        For example:

        "hello" in list_name

        is equivalent to:

        list_name.__contains__("hello")

        This method returns True if and only if the item argument is equal to
        the contents of one of the linked list's nodes, and returns False
        otherwise. An empty list, of course, will always return False.

        """
        point = self._first
        while not point is None:
            if point._contents == item:
                return True
            point = point._next
        return False
