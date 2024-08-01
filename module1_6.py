my_dict = {'Данил': 2004, 'Никита': 2003, 'Серёга': 2005}
print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict['Данил']}")
print(f"Not existing value: {my_dict.get("Аркадий")}")
my_dict.update([('Саша',2005),('Тимур', 2004)])
print(f"Deleted value: {my_dict.pop('Саша')}")
print(f"Modified dictionary: {my_dict}")
print()
my_set = {1,(1,2),4,13,13,"hello",(1,2,3)}
print(f"Set: {my_set}")
my_set.update((6,7))
my_set.discard((1,2))
print(f"Modified set: {my_set}")