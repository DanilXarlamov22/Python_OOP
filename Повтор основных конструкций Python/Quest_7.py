def quantify(iterable, predicate):
    if predicate is None:
        predicate = bool
    return len(list(filter(lambda x: predicate(x), iterable)))