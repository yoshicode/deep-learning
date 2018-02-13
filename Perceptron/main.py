
def AND(x1, x2):
    # w1 and w2 are weight
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        print(0)
        return
    elif tmp > theta:
        print(1)
        return

AND(0, 0)
AND(0, 1)
AND(1, 0)
AND(1, 1)
