import ast
import _ast
import argparse

fct = """
def iteration():
    l = list(range(100))
    k = len(l)
    i = 0
    e = list()
    while i < k:
        e.append(l[i])
        i += 1
"""

class WhileCheck (ast.NodeVisitor):

    def __init__(self):
        self._op = None
        self._var_name = None
        self._cpt = 0


    def visit_While(self, node):
        print("|trace : visit_While, l.", node.lineno)
        self._show_fields(node)
        if isinstance(node.test, ast.Compare):
            self._op = node.test.ops[0]
            print("| trace : op ->", self._op)
            if isinstance(self._op, _ast.Lt) or isinstance(self._op, _ast.LtE):
                # var {< | <=} var'
                self._var_name = node.test.left.id
            else:
                # var' {> | >=} var
                self._var_name = node.test.comparators[0].id
            print("| trace : var ->", self._var_name)
            self.generic_visit(node)

            
    def visit_AugAssign(self, node):
        print("| trace : visit_AugAssign, l.", node.lineno)
        self._show_fields(node)
        print("| trace : cpt ->", self._cpt)
        if isinstance(node.target, ast.Name):
            if node.target.id == self._var_name:
                self._cpt += 1
                print("| trace : incr(cpt)")
            print("| trace : cpt ->", self._cpt)

        
    def _show_fields(self, node):
        for fields in ast.iter_fields(node):
            print("|\t", fields[0], ':', fields[1:], end='\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="File to check",
                        type=str)
    args = parser.parse_args()
    tree = None
    with open(args.filename, "r") as stream:
        tree = ast.parse(stream.read())
    print(tree)
    # tree = ast.parse(fct)
    check = WhileCheck()
    check.visit(tree)
        
if __name__ == '__main__':
    main()
