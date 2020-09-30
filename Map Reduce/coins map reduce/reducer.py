from operator import itemgetter
import sys

current_coin = None
current_count = 0
coin = None
total = 0

for line in sys.stdin:
    line = line.strip()
    coin, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_coin == coin:
        current_count += count
    else:
        if current_coin:
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_coin = coin
        total += int(coin) * int(count)

if current_coin == coin:
    print '%s\t%s' % (current_coin, current_count)
    print '%s' % (str(total))
