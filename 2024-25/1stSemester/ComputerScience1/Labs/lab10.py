# CS1210: Lab10 [4 method to complete]
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
    return(["masnorris","cmcano"])

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
from math import sqrt
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
        list.__init__(self, list(args))

    # Specification: __repr__(self) produces a string representation
    # of this instance of Vector. Given that the underlying
    # representation is essentially a list, we want this Vector to
    # print out as <1, 2, 3, 4> rather than [1, 2, 3, 4] which is the
    # list's __repr__(self) method's behavior.
    #
    def __repr__(self):
        return '<' + ', '.join(map(str, self)) + '>'

          #return('<{}>'.format(super().__repr__(self)[1:-1]))

    # Specification: magnitude(self) returns the scalar magnitude of
    # Vector rounded to 10 decimal places. The scalar magnitude of a
    # vector is the square root of the sum of the squares of the
    # elements.
    #
    # Hint: you can use the round() function to force something to
    # round to the appropriate number of decimal digits.
    #
    def magnitude(self):
        return round(sqrt(sum([i*i for i in self])), 10)

    # Specification: normalize(self) turns self into a unit vector,
    # that is, a vector who's magnitude is 1.0.  Your method should
    # return True on success, False on failure (e.g., a zero-length
    # vector).
    #
    # Hint: you can use magnitude(self) to normalize.
    #'
    '''
    def normalize(self):
        if magnitude(self) == 0:
            return False
        self[:] = [(i/magnitude(self)) for i in self]
        return True
    '''
    def normalize2(self):
        mag = self.magnitude()
        if mag == 0:
            return False
        for i in range(len(self)):
            self[i] = self[i]/mag
        return True

    # Specification: dproduct(self, other) returns the dot product of
    # two Vectors: the current Vector, self, and another Vector, other.
    #
    # Your solution should raise a TypeError (with message "Vector
    # length mismatch") using a try/except form when called on two
    # vectors of different lengths. We used try/except in our
    # 2024-11-01 lecture, but you can review [P4E] C3.7 if you are
    # rusty.
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
        try:
            if len(self) != len(other):
                raise TypeError
            return sum([(i[0]*i[1]) for i in zip(self, other)])
        except:
            return "Vector length mismatch"
    def dproduct2(self, other):
         if len(self) != len(other):
             raise TypeError("vector length mismatch")
         return(sum([pair[0]*pair[1] for pair in zip(self,other)]))
         
