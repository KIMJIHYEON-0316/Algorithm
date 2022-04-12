from collections import defaultdict

list_dict = defaultdict(list)

print(list_dict['key1'])

list_dict['key1'] = 'A'

print(list_dict['key1'])
print(list_dict.keys())
print(list_dict.values())