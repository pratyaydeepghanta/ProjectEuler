"""
"""


import math


def main():
    t = int(raw_input().strip())
    while t:
        n = int(raw_input().strip())
        print sum(map(int, str(math.factorial(n))))
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
