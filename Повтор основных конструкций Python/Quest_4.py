import sys
from collections import Counter

cards_list = [c.rstrip() for c in sys.stdin]
result_dict = Counter(cards_list)
count_sale = 0
for k, v in result_dict.items():
    if v != 1:
        count_sale += result_dict[k] - 1

print(count_sale)
