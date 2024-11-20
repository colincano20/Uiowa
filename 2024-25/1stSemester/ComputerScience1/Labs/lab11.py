# CS1210: Lab11 [4 methods to complete]
######################################################################
# READ ALL INSTRUCTIONS CAREFULLY.
#
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partner(s), and
#  2) you have not shared it nor will share it with anyone else.
#
# ToDo: Change the two "hawkid" strings to match the hawkids of you
# and your partner(s). Your hawkid is the "login identifier" that you
# use to login to all University services: it is not your email
# address or your student id number.
#
# Note: we are not asking for your passwords, just the login
# identifiers: for example, mine is "segre". 
#
# Note: if there are 3 of you, add a third string to the list returned
# by signed() below (e.g., change ["hawkid1","hawkid2"] to
# ["hawkid1","hawkid2","hawkid3"], using your own three UI login
# identifiers as the hawkid values).
#
def signed():
    return(["cbliss1","cmcano"])

######################################################################
# For this lab, we'll be writing an OO implementation of
# one-dimensional vectors based on specializing an existing class,
# list.
#
# We represent vectors as lists of numbers; defining the vector class
# as a specialization of list allows us to add extra functionality to
# list (such as normalization and dotproduct) while retaining a lot of
# useful methods already provided.
#
# I am providing the basic structure of the class, including the
# constructor, and you will provide a number of additional methods.
#
from math import sqrt, cos, acos, degrees
class Vector(list):
    # Specification: __init__(self, *args) is the initializor invoked
    # each time we create an object of type Vector. It relies on
    # manually invoking the parent class' __init__() method with a
    # little additional work.
    #
    # My implementation shows off an argument handling trick: unlike
    # list's __init__(), Vector's __init__() groups all of its
    # arguments into a new vector. This means Vector(1,2,3,4) will
    # return a 4-element vector <1,2,3,4>, even though list(1,2,3,4)
    # yields an error -- recall the list constructor requires a
    # seqence as its only argument, so list([1, 2, 3, 4]) or
    # list(range(1,5)) would be more typical.
    #
    # This isn't necessarily a good idea, but grouping multiple
    # remaining arguments with the *args construct is a good trick to
    # know about, and one we covered on 2024-09-20.
    def __init__(self, *args):
        '''Constructor invokes list constructor on the collection of args given.'''
        super().__init__(list(args))

    # Specification: __repr__(self) produces a string representation
    # of this instance of Vector. Given that the underlying
    # representation is essentially a list, we want this Vector to
    # print out as <1, 2, 3, 4> rather than [1, 2, 3, 4] which is the
    # list's __repr__(self) method's behavior.
    #
    def __repr__(self):
        '''Replace standard list brackets with angle brackets.'''
        return('<{}>'.format(super().__repr__()[1:-1]))

    # Specification: magnitude(self) returns the scalar magnitude of
    # Vector rounded to 10 decimal places. The scalar magnitude of a
    # vector is the square root of the sum of the squares of the
    # elements.
    #
    # Hint: you can use the round() function to force something to
    # round to the appropriate number of decimal digits.
    #
    def magnitude(self):
        '''Returns scalar magnitude of self rounded to 10 decimal places.'''
        return(round(sqrt(sum( [ val*val for val in self ])), 10))

    # Specification: normalize(self) turns self into a unit vector,
    # that is, a vector who's magnitude is 1.0.  Your method should
    # return True on success, False on failure (e.g., a zero-length
    # vector).
    #
    # Hint: you can use magnitude(self) to normalize.
    #
    def normalize(self):
        '''Normalize self to unit magnitude. Returns True on success, False
           otherwise.'''
        mag = self.magnitude()
        if mag == 0:
            return(False)
        for i in range(len(self)):
            self[i] = self[i]/mag
        return(True)

    # Specification: dproduct(self, other) returns the dot product of
    # two Vectors: the current Vector, self, and another Vector,
    # other, rounded to 10 decimal places.
    #
    # Your solution should raise a TypeError (with message "Vector
    # length mismatch") that can be trapped using a try/except form
    # when called on two vectors of different lengths. We used
    # try/except in our 2024-11-01 lecture, but you can review [P4E]
    # C3.7 if you are rusty.
    #
    # Also, although not strictly necessary, consider the use of zip()
    # to "sew" two like-sized lists together, element by element.
    #    >>> zip([1,2,3],[4,5,6])
    #    <zip object at 0x7f2e52fa8700>
    # where the zip object "looks" internally like:
    #    >>> list(zip([1,2,3],[4,5,6]))
    #    [(1, 4), (2, 5), (3, 6)]
    # This can be quite handy as the sequence part of a comprehension,
    # for example.
    #
    # To unzip a zip object (although you won't need to here):
    #    >>> zip(*zip([1,2,3],[4,5,6]))
    #
    def dproduct(self, other):
        '''Dot product of self and another vector.'''
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return(round(sum([ pair[0]*pair[1] for pair in zip(self,other) ]), 10))

    # Specification: edistance(self, other) returns the Euclidean
    # distance between two Vectors: the current Vector, self, and
    # another Vector, other, rounded to 10 decimal places.
    #
    # Your solution should raise a TypeError (with message "Vector
    # length mismatch") that can be trapped by a try/except form when
    # called on two vectors of different lengths.
    #
    #our solution
    def edistance(self, other):
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return round(sqrt(sum([(a - b)**2 for a, b in zip(self, other)])), 10)

    #teacher solution
    def edistance2(self,other):
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return(round(sqrt(sum([pow(pair[0] - pair[1], 2) for pair in zip(self.other)])), 10))

    

    # Specification: add(self, other) returns a new Vector instance
    # elements that are element-by-element sums of self and other. 
    #
    # Your solution should raise a TypeError (with message "Vector
    # length mismatch") that can be trapped by a try/except form when
    # called on two vectors of different lengths.
    #our solution
    def add(self, other):
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")

        return Vector(*(a+b for a, b in zip(self, other)))
    #teacher solution
    def add(self, other):
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return(Vector(*[pair[0] + pair[1] for pair in zip(self.other)]))

    # Specification: sub(self, other) returns a new Vector instance
    # elements that are element-by-element differences of self and
    # other.
    #
    # Your solution should raise a TypeError (with message "Vector
    # length mismatch") that can be trapped by a try/except form when
    # called on two vectors of different lengths.
    # our solution
    def sub(self, other):
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")

        return Vector(*(a-b for a, b in zip(self, other)))
    
    #teacher solution does not  exist
    def sub(self,other):
        pass


    # Specification: theta(self, other) returns the angle between two
    # unit vectors, self and other, expressed in degrees using the
    # cosine rule, which relates the cosine of theta (the angle
    # between the two vectors) to the dot product of the two vectors
    # divided by the product of the scalar magnitudes of both
    # vectors. The result should again be rounded to 10 decimal places.
    #
    # As with many numerical calculations, the effects of rounding can
    # wreak havoc, throwing unexpected errors. Here, you will need to
    # take the inverse cosine (see acos() in the Python docs), which
    # expects its argument to be between -1 and 1. But rounding can
    # cause your value to exceed these limits, even if only just by a
    # little bit. Make sure you take steps to avoid the issue.
    #
    # To test your code, try finding the angle between a vector and
    # its unit vector equivalent. Technically, this should be 0, but
    # because we've limited the precision to 10 decimal places, it
    # will likely be off by a few thousandths of a degree.
    #our solution
    def theta(self, other):
        if len(self) != len(other):
            raise TypeError("Vector length mismatch")
        return round( degrees( acos( min(1, max(-1, self.dproduct(other) / (self.magnitude() * other.magnitude()))))), 10)
    #teacher solution
    def theta(self,other):
        if self.magnitude() == 0 or other.magnitude() ==0:
            raise ZeroDivisionError("Zero Magnitude vector")
        return(round(degrees(acos(max(-1, min(1, self.dproduct(other) / (self.magnitude() * other.magnitude()))))),10))
    