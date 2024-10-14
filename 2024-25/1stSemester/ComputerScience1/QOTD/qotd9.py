# CS1210: QotD9
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) you have not shared it with anyone else.
#
# ToDo: Change the word "hawkid" between the two double quote marks to
# match your own hawkid. Your hawkid is the "login identifier" (not
# your email address) that you use to login to all University
# services.
#
def signed():
    return(["cmcano"])

######################################################################
# Specification: smooshInts(n) takes a nonnegative integer, n, and
# returns a new integer consisting only of the even digits in n.
#
# Example:
#   >>> smooshEvens(19054249)
#   424                # Note flushed leading 0!
#   >>>smooshEvens(452350194)
#   4204
#   >>> smooshEvens(77713319)
#   0                  # Edge casem, no even ints!
#
# Your solution must employ a comprehension. You will also need to
# review your string methods and brush up on how to change types.
#
# Note that the obvious, simple, solution has an unfortunate edge case
# when there are no even integers! You can fix this with a conditional
# -- which I've asked you not to use -- or you can use a different,
# somewhat clever, solution to handle the edge case. Let's plan on the
# latter.
#
def smooshEvens(n):
    return (int(''.join(i for i in str(n) if int(i) % 2 == 0) or 0))

