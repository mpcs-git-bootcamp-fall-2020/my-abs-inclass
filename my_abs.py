import math
from numeric.abc import Real, Complex

def my_abs(x):
    if isinstance(x, Real):
        if x < 0:
            return -x
        else:
            return x
    else if isinstance(x, Complex):
        do that math i forget
    else:
        return math.nan

def my_almost_eq(x, y, tol):
    if (my_abs(x -y) < tol):
        return True
    else:
        return False
