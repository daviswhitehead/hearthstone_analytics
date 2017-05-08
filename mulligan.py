""" Calculates mulligan
"""


def choice_probability(total, target, trials):
    """ Calculates the probability of NOT choosing at least
        one target from a total.
    """
    # logging
    print total, target, trials

    p = 1.0
    for t in range(0, trials):
        remaining = (total - t)
        p = p * float(remaining - target) / float(remaining)

    return p


def mulligan(target, coin):
    # handle coin
    trials = 4 if coin else 3
    total = 30

    # first round
    p1 = choice_probability(total, target, trials)

    # second round
    p2 = choice_probability(total - trials, target, trials)

    print p1 * p2
    return p1 * p2


def main():
    m1 = mulligan(6, True)
    m2 = mulligan(6, False)
    m = (m1 * 0.5) + (m2 * 0.5)
    print 1 - m

if __name__ == '__main__':
    main()
