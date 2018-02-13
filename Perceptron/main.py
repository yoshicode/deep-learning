
import numpy as np

# No bias
def ANDWithNoBias(x1, x2):
    # w1 and w2 are weight
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


# With bias
def ANDWithBias(x1, x2):
    # w1 and w2 are weight
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return print(0)
    else:
        return print(1)
