import sys
lst = [list(eval(c)) for c in sys.stdin]
for x, y in lst:
    print(abs(x) <= 90 and abs(y) <= 180)



