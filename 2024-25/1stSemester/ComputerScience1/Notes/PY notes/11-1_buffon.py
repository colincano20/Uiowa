from random import random# notice

def buffon(n):
    inside = 0
    for i in range(n):
        x = random()
        y = random()
        if x*x + y*y < 1:
            inside += 1
    return(4*float(inside) / n)