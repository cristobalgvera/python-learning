def remove_duplicates(elements_list: list[str]) -> list[str]:
    return list(set(elements_list))


aList = ['HELLO', 'HELLO', 'HELLO', 'HELLO', 'BYE']
print(aList)

newList = remove_duplicates(aList)
print(newList)
