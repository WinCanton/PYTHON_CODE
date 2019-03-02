import sys


def main(x):

"""
returns bool status

Program checks an integer input for palindrome property.
Input is given as an argument to the program during invocation.
Result printed to the screen.
"""
    for i in range(divmod(len(x), 2)[0]):
        j = -(i + 1)
        if x[i] == x[j]:
            continue
        else:
            print("number is not palindrome")
            return False
    print("number is palindrome")
    return True


if __name__ == '__main__':
    main(sys.argv[1])
