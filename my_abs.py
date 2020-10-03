import math

def my_abs(x):
    try:
        if x < 0:
            return -x
        else:
            return x
    except TypeError:
        return math.nan

def my_almost_eq(x, y, tol):
    if (my_abs(x -y) < tol):
        return True
    else:
        return False
