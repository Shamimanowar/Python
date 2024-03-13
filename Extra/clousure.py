from collections import namedtuple

def init_count():

    count: int = 0
    
    def add(amount):
        nonlocal count
        count += amount

    def get_count():
        return count
    Count = namedtuple("Count", ['add', 'now_count'])
    # namedtuple(typename, field_names)
    
    return Count(add, get_count)