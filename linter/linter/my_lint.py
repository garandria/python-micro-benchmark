import ast
import _ast

def main():
    with open("prog.py", "r") as stream:
        tree = ast.parse(stream.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
             # # print('node:', node, 'at line:', node.lineno)
            #  # print(ast.dump(node.test.comparators))
            # for fieldname, value in ast.iter_fields(node):
            #     print(fieldname, ":", value)
            # comparator index < var; var  > index
            the_iter = None
            op = node.test.ops[0]
            if isinstance(op, _ast.Lt) or isinstance(op, _ast.LtE):
                  print('lt')
                  # the_iter `op` var
                  the_iter = node.test.left.id
            elif isinstance(op, _ast.Gt) or isinstance(op, _ast.GtE):
                  print('gt')
                  # var `op` the_iter
                  the_iter = node.test.comparators[0].id
            for form in node.body:
                if isinstance(form, ast.AugAssign):
                    
                 
if __name__ == '__main__':
    main()
