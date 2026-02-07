from itertools import permutations
from wordfreq import zipf_frequency
from tabulate import tabulate

chars = ['s', 'e', 'a', 'i', 'p', 'o']
special_char = 'd'
result = []

chars += special_char
for i in range(1, len(chars) + 1):
    for p in permutations(chars, i):
        result.append(''.join(p))

final_val = {}
for local in result:
    if ((special_char in local) and (len(local) >= 4) and (zipf_frequency(local, 'en') > 2) and (local not in final_val.keys())):
        final_val[local] = zipf_frequency(local, 'en')


table = []
sorted_dict = dict(sorted(final_val.items(), key=lambda x: x[1], reverse=True))
for keys in sorted_dict.keys():
    table.append([keys, sorted_dict[keys]])

headers = ["Word", "Relevence"]
print(tabulate(table, headers=headers, tablefmt="plain"))
