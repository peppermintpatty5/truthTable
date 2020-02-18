from ast import *
from tabulate import tabulate


class NameGetter(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.names = set()

    def visit_Name(self, node):
        self.names.add(node.id)

    def getNames(self):
        return self.names


def boolIter(n):
    return (list(c == "0" for c in bin(i)[2:].zfill(n)) for i in range(1 << n))


def boolExprTbl(expr):
    ng = NameGetter()
    ng.visit(parse(expr))
    names = sorted(ng.getNames())

    return {
        "thead": names + [expr],
        "tbody": [x + [eval(expr, dict(zip(names, x)))] for x in boolIter(len(names))],
    }


while True:
    try:
        tbl = boolExprTbl(input("Enter a boolean expression: "))
        print(tabulate(tbl["tbody"], tbl["thead"], "github"), "\n")
    except EOFError as e:
        print("Goodbye!")
        break
