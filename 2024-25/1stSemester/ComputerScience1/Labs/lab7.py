# CS1210: Lab7 [3 functions to complete]
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
# Specification: afford(amount, purse) takes an integer amount and a
# list of the coins you currently have in your coin purse, and returns
# True if there is a combination of your coins that equals amount, or
# False if no such combination exists.
#
# Your solution should be recursive.
#
# Hint: The recursive step basically notes that a solution will either
# require using a given coin from your purse (and concomitantly
# reducing the remaining amount) or not using that given coin (#
# leaving the remaining amount unchanged).
#
# Example:
#   >>> afford(0, [1, 10, 5, 10, 25, 1])
#   True
#   >>> afford(23, [1, 10, 5, 10, 25, 1])
#   False
#   >>> afford(26, [1, 10, 5, 10, 25, 1])
#   True
#
def afford(amount, purse):
    if amount == 0:
        return True
    elif len(purse) == 0:
        return False
    return afford(amount-purse[0], purse[1:]) or afford(amount, purse[1:])
    

######################################################################
# Specification: spend(amount, purse) takes an integer amount and a
# list of the coins you currently have in your coin purse, and returns
# a list of coins from your purse that equal amount, or False if no
# such combination exists. Your solution should be recursive.
#
# Hint: start with afford() and modify it to construct the solution as
# you descend the recursive calls.
#
# Example:
#   >>> spend(0, [1, 10, 5, 10, 25, 1])
#   []
#   >>> spend(23, [1, 10, 5, 10, 25, 1])
#   False
#   >>> spend(22, [1, 10, 5, 10, 25, 1])
#   [1, 10, 10, 1]
#
# Note that there may be more than one coin combination that equals
# amount; return any legal combination.
#
def spend(amount, purse, spent=[]):
    if amount == 0:
        return spent
    elif len(purse) == 0:
        return False
    return spend(amount-purse[0], purse[1:], spent+[purse[0]]) or spend(amount, purse[1:], spent)

######################################################################
# Specification: change(amount, coins) takes an integer amount and a
# list containing the value of the coins in a given country's coinage
# system and returns the minimum number of coins needed to sum to
# amount, or False in the event that there is no "reasonable"
# combination of coins that works.
#
# What is a "reasonable" combination? Well this gets pretty technical,
# but what you should know is that the algorithm will work for any
# "superincreasing" coinage system, meaning that each successive
# denomination is greater or equal to twice the previous denomination.
# The US coinage system is designed in just this way: [100, 50, 25,
# 10, 5, 1], for dollar, half dollar, quarter, dime, nickel and penny.
# We'll make the US coinage system the default value in our function
# signature.
#
# Example:
#    >>> change(17, [100, 50, 25, 10, 5, 1])
#    [10, 5, 1, 1]
#    >>> change(58, [100, 50, 25, 10, 5, 1])
#    [50, 5, 1, 1, 1]
#    >>> change(0, [100, 50, 25, 10, 5, 1])
#    []
#    >>> change(9, [6,  3])
#    [6, 3]
#    >>> change(9, [7, 6, 3])
#    False           # Not a superincreasing coinage set!
#    >>> change(9, [6,  2])
#    False           # Superincreasing, but no solution.
#    >>> change(9, [6, 2, 1])
#    [6, 2, 1]       # Adding 1 ensures a solution.
#
# Here, we will assume the coinage set is alway superincreasing, so
# False means there isn't a solution.  Also note that we assume there
# are infinitely many coins of each value available; so if you need 17
# quarters for your solution, you can safely assume that there are 17
# quarters available.
#
# The cool thing about the change function is that it always returns
# the smallest number of coins required when used with an appropriate
# coinage set. So, for example, it would never return:
#    >>> change(58, [100, 50, 25, 10, 5, 1])
#    [25, 25, 5, 1, 1, 1]
# even though this is a legal solution, because using a half dollar
# requires one fewer coin that using two quarters.
#
def change(amount, coins=[100, 50, 25, 10, 5, 1]):
    L = []

    while amount > 0 and coins:
        print(L)
        if amount >= coins[0]:
            amount -= coins[0]
            L.append(coins[0])
        else:
            coins = coins[1:]

    if amount == 0:
        return L
    
    return False
