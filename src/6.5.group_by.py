def group_by(func, iterable):
    return {func(i): [ii for ii in iterable if func(ii) == func(i)] for i in iterable}
