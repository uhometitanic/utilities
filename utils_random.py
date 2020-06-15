# this module contains some functions that generate random objects
import random


def randstr(length, k):
    """Generate k random strings consisting of word characters of
    the given length.
    """
    import string

    word_chars = string.ascii_letters + string.digits
    for _ in range(k):
        rand_chars = random.choices(word_chars, k=length)
        yield ''.join(rand_chars)


def randate_from(last_date, day_range, k):
    """Generate k random dates within the given day_range from
    the given fixed last_date.
    """
    import datetime

    for _ in range(k):
        days = random.randrange(day_range)
        yield last_date - datetime.timedelta(days)


def farey_sequence(m):
    """Return the Forey's sequence with denominator <= m."""
    seq = []
    a, b, c, d = 0, 1, 1, m
    while c <= m:
        k = (m + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        seq.append((a, b))
    return seq


def randfrac(m, k):
    """Generate k random fractions within the range of (0, 1]
    with denominator <= m.
    """
    import fractions

    seq = farey_sequence(m)
    for _ in range(k):
        numer, denom = random.choice(seq)
        yield fractions.Fraction(numer, denom)
