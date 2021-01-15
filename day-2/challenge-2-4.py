class Friend:
    def __init__(self, name: str, best_friend: bool, vegan: bool, angry: bool, woman: bool):
        self.name = name
        self.best_friend = best_friend
        self.vegan = vegan
        self.angry = angry
        self.woman = woman


friends = {
    "John": Friend("John", False, True, True, False),
    "Peter": Friend("Peter", True, False, False, False),
    "Maria": Friend("Maria", False, True, False, True),
    "Helena": Friend("Helena", True, True, False, True),
    "Douglas": Friend("Douglas", False, False, False, False)
}


def filter_friends(attribute: str, state: bool) -> {}:
    for i, friend in friends.items():
        if friend.__getattribute__(attribute) == state:
            condition = ("is " if state else "isn't ") + attribute
            print(i, condition)


filter_friends('angry', False)
