# CS1210: Lab1 [5 functions to complete]
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
# In this lab, you'll be working on 5 functions inspired by the first
# few weeks of lecture. This is a fairly easy but not entirely trivial
# lab, and one meant to get you into the swing of things.
#
# Assuming you are working in pairs, compile a single solution file
# that includes both (all three in some cases) of your hawkids in the
# signed() function above. Upload your solution to Gradescope, being
# careful to specify your partner(s) as your "group members" at
# submission time.
#
# MAKE SURE YOU IDENTIFY YOUR LAB PARTNERS IN GRADESCOPE.
#
# Ideally, each of you will take turns on the machine, with the second
# partner watching and helping. Switch roles frequently (perhaps for
# each problem).  This paired approach is often described as an
# integral part of the agile software development paradigm; it is
# commonly used in industry, and you can expect to encounter it
# professionally. Be patient, listen to each other, and resist
# temptation to solve the problem unilaterally. Your solutions should
# be jointly derived.
#
# For full credit, meet the spec in its entirety, and use only
# concepts introduced in class and in your assigned readings. Pay
# attention to types; return exactly what is being asked for. You will
# not need conditional statements or iteration to solve these
# problems. Each problem pretty much has just a simple one line
# solution that captures the essence of the calculation!

######################################################################
# Specification: m2ft takes an number, m, representing a distance in
# meters, and returns the corresponding distance measured in feet.
#
# There are 3.28084 feet in a meter.
#
# Example:
#   >>> m2ft(2.1)
#   6.889764
#
# Note: this is a simple function. It takes a value as input and
# returns another value. Be concise.
#
def m2ft(m):
    return m*3.28084

######################################################################
# Specification: runway(S) takes a string representing the large
# block numbers painted on an airport runway and returns an integer
# corresponding to the compass heading of that runway. 
#
# Example:
#   >>> runway('32')
#   320
#   >>> runway('7')
#   70
#   
# Note: The input to runway() is a string, not an integer, and is
# guaranteed to correspond to an integer between 1 and 36, inclusive,
# as these are the legal runway markings. 
#
# Note: The numbers painted on runways (e.g., 9R) are shorthand for
# the compass heading of that runway. They are meant to facilitate
# communication between air traffic control and pilots, hence "cleared
# to land runway two-two" makes sense to both and conveys important
# directional information (heading 220) to the pilot. The numbers
# measured from North (the optional R/L denote 'left' or 'right' when
# dealing with a pair of parallel runways -- we won't worry about that
# here).  Here, runway numbers will always be between 1 and 36
# (inclusive), but compass headings range from 0-360, where 0 and 360
# both correspond to North (and such a runway would be labeled 36, not
# 0).
#
# Note: Your solution should consist of a single statement; there is
# no need to use assignment (i.e., '='): be concise.
#
def runway(S):
    return int(S + '0')

######################################################################
# Specification: opposite(S) takes a string representing the large
# block numbers painted on an airport runway and returns an integer
# corresponding to the large block number painted on the other end of
# the same runway. The value returned must be in the range from 1-360;
# 0 is not a legal runway label!
#
# Example:
#    >>> opposite('12')
#    300
#    >>> opposite('34')
#    160
#
# Note: The runway labeled with a 9 corresponds to a compass heading
# of 90 degrees (clockwise) from North (i.e., heading East). The same
# runway, approached from the other side (i.e., coming from East
# heading West), would be labeled 27, or 270 degrees on the
# compass. Here's a crude picture (the numbers would be rotated in
# real life so as to be read by a plane approaching that end of the
# runway):
#
#           ---------------------------------------------
#           9                                          27
#           ---------------------------------------------
#
# Hint: Feel free to invoke your runway() function within opposite()
# if that's useful.
#
# Hint: You will have to do some modular arithmetic, and pay careful
# attention to the case marked 180, which should return 360, as 0 is
# not a legal runway label.
#
# Note: Your solution should consist of a single statement; there is
# no need to use assignment (i.e., '='): be concise.
#
def opposite(S):
    return ((runway(S) + 180) % 360)

######################################################################
# Specification: countTables(n, s) takes two integers, n and s, where
# n represents the number of people invited to a wedding, and s
# represents the number of seats at each rented table, both which are
# known to be positive integers (you needn't check). The function
# returns an integer, indicating the minimum number of tables required
# to seat all of your guests.
#
# So, for example, countTables(100, 17) returns 6, which means you'll
# need 6 tables each with 17 seats (102 seat capacity) to seat 100
# guests.
#
# ToDo: Remove the line that says "pass" and replace it with your own
# code. Do not alter the function signature.
#
# Hints: This is a real puzzler! The intended solution requires only
# some integer arithmetic. Other less elegant solutions may involve
# type conversions (e.g., int to float, Boolean to int, float to
# Boolean or something similar), but your solution should not use
# if/else.
#
def countTables(n, s):
    return((n + (s-1))// s)

######################################################################
# Specification: zulu(h, m, tz) takes a three integers, representing
# the time (using a 24 hour clock) and the timezone (tz, a number
# between -12 and 12), denoting the difference between Zulu time (also
# known as Coordinated Universal Time, or UTC, or the time at the
# Greenwich Meridian) and your local time in timezone tz, returning a
# representation of local time as a string.
#
# So, for example, Central Time (our time zone) is UTC -6, meaning
# that Greenwich is 6 hours ahead of us, so:
#
# Example:
#   >>> zulu(11, 23, -6)
#   '5:23'
#   >>> zulu(21, 14, -6)
#   '15:14'
#   >>> zulu(3, 59, -9)
#   '18:59'
#
# Note that we are not worrying about standard/daylight time
# differences, whether (as in the last example shown above) there is
# also a date differential, or whether the time returned is always in
# the format hh:mm (see next to last example above).
#
# As for the other problems in this lab, your solution must be
# concise, and should not rely on constructs we have not yet covered
# in class.
#
def zulu(h, m, tz):
    return str((h + tz) % 24) + ':' + str(m)
