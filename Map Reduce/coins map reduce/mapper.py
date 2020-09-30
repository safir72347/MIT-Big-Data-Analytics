import sys

for line in sys.stdin:
    line = line.strip()
    coins = line.split()
    for coin in coins:
        print '%s\t%s' % (coin, 1)
