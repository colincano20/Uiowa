# CS1210: QotD2
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
# Specification: mpg2lpk(mpg) takes an integer, mpg, as input
# (representing miles per gallon) and returns a number representing
# the corresponding performance expressed as liters per 100
# kilometers.
#
# Backstory: Some of you may be surprised that what we express as
# miles per gallon in the US (essentially, distance per volume of
# fuel) is typically expressed as liters per 100 kilometers in Europe
# (essentially, volume of fuel per distance).
#
# So, in Europe, a smaller number corresponds to higher efficiency!
#
# Example:
#   >>> mpg2lpk(52)	    # 2023 Toyota Prius
#   4.523357629902905
#   >>> mpg2lpk(19)         # 1963 Pontiac Tempest 389 V8
#   12.379715618681635      # (see "My Cousin Vinnie")
#
# Hints:
#   There are 1.609344 kilometers in a mile.
#   There are 3.785412 liters in a gallon.
#
# ToDo: Remove the line that says "pass" and replace it with your own
# code. Do not alter the function signature.
#
def mpg2lpk(mpg):
    if mpg > 0:
         miles = 1
         gallons = 1
         liters = gallons * 3.785412
         kilometers = miles * 1.609344
         liter_100km = (100 * liters)/ kilometers
         volume = liter_100km / mpg
         return(volume)
    else:
        return('Please insert number above 0')



    
    
