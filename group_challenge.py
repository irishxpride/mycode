#!/usr/bin/python3

hard= {"key1": [1, 2], "key2": [3, 4], "key3": [5, 6]}

harder= [{"key1": [1, 2], "key2": [3, 4], "key3": [5, 6]}]

hardest= {"thisishard":[{"key1": [1, 2], "key2": [3, 4], "key3": [5, 6]}]}


print(f'hard is {hard["key3"][1]}')

print(f'harder is {harder[0]["key3"][1]}')

print(f'hardest is {hardest["thisishard"][0]["key3"][1]}')
