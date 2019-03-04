import sys


def main(x):
    """
    Reverse digits of a 32-bit signed integer.
    Example:
        Input: 123 - Output: 321
        Input: -123 - Output: -321
        Input: 120 - Output: 21
        Input: 1534236469 - Output: 0 (answer overflows)

    Parameters
    ==========
    x: 32-bit signed integer
    Returns
    =======
    32-bit signed integer
    """
    neg_number = False

    if x < 0:
        x = abs(x)
        neg_number = True

    reverse = 0
    while (x > 0):
        lastDigit = x % 10
        reverse = (reverse * 10) + lastDigit
        x = x // 10

    top_limit = 1 << 31
    bottom_limit = -1 << 31

    if reverse > top_limit or reverse < bottom_limit:
        print('0')
        return 0
    else:
        return reverse if not neg_number else (-1 * reverse)


if __name__ == '__main__':
    print(main(int(sys.argv[1])))
