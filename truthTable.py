keywords = {"not", "and", "or", "True", "False"}


def boolIterator(n):
    """Generates boolean tuples from 0 to 1 << n"""
    if n > 0:
        for t in [True, False]:
            for u in boolIterator(n - 1):
                yield (t,) + u
    else:
        yield ()


def removeParens(string):
    """Removes all parentheses from the string"""
    return "".join(filter(lambda t: t not in "()", string))


def getParams(expr):
    """Extracts the parameters from a boolean expression. For example:

    getParams("(a and b) or (a and c)") would produce ['a', 'b', 'c']"""
    return sorted(set(filter(lambda t: t not in keywords, removeParens(expr).split())))


def truthDict(expr):
    params = getParams(expr)
    f = eval("lambda {}: {}".format(", ".join(params), expr))
    return {b: f(*b) for b in boolIterator(len(params))}


demo = input("Enter a boolean expression: ")
print("{} | {}".format(" ".join(getParams(demo)), "X"))
for k, v in truthDict(demo).items():
    print("{} | {}".format(" ".join(str(int(t)) for t in k), int(v)))
