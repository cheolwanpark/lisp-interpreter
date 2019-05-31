import math


class function:
    def __init__(self, variables, body):
        self.variables = variables
        self.body = body



def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


g_namespace = dict()
l_namespace = []


def add_val_in_global_namespace(name, val):
    if name in g_namespace:
        return False
    g_namespace[name] = val
    return True


def set_val_in_global_namespace(name, val):
    if name in g_namespace:
        g_namespace[name] = val
        return True
    else:
        return False


def find_val_in_global_namespace(name):
    if name in g_namespace:
        return g_namespace[name]
    return None


def find_val_in_local_namespace(name):
    for i in reversed(range(len(l_namespace))):
        if name in l_namespace[i]:
            return l_namespace[i][name]
    return None



# http://rigaux.org/language-study/syntax-across-languages-per-language/Scheme.html
# based on upper web page
# not implemented functions about string ( not handle string )
# some functions not implemented too ( acos, asin, ..., case, ... )


def evaluation(expr):
    if not isinstance(expr, list):
        try:
            return float(expr)
        except ValueError:
            return evaluation([expr])

    # process funcs which have exceptional expression
    val = evaluation_except(expr)
    if val is not False:
        return val

    operator = expr[0]
    # evaluate opr values first
    opr = list(map(lambda x: evaluation(x), expr[1:]))
    count = len(opr)

    # math functions
    if "+" == operator:
        result = 0
        for i in range(count):
            result += opr[i]
        return result
    elif "-" == operator:
        if 0 == count:
            print("- : invalid number of operands")
            exit(-1)
        elif 1 == count:
            return -opr[0]
        result = opr[0]
        for i in range(1, count):
            result -= opr[i]
        return result
    elif "*" == operator:
        result = 1
        for i in range(count):
            result *= opr[i]
        return result
    elif "/" == operator:
        if 0 == count:
            print("/ : invalid number of operands")
            exit(-1)
        result = opr[0]
        for i in range(1, count):
            result /= opr[i]
        return result
    elif "min" == operator:
        if 0 == count:
            print("min : invalid number of operands")
            exit(-1)
        result = opr[0]
        for i in range(1, count):
            a = opr[i]
            if a < result:
                result = a
        return result
    elif "max" == operator:
        if 0 == count:
            print("max : invalid number of operands")
            exit(-1)
        result = opr[0]
        for i in range(1, count):
            a = opr[i]
            if a > result:
                result = a
        return result
    elif "expt" == operator:
        if 2 != count:
            print("expt : invalid number of operands")
            exit(-1)
        return math.pow(opr[0], opr[1])
    elif "log" == operator:
        if 1 == count:
            return math.log(opr[0])
        elif 2 == count:
            return math.log(opr[0], opr[1])
        else:
            print("log : invalid number of operands")
            exit(-1)
    elif "remainder" == operator:
        if 2 != count:
            print("remainder : invalid number of operands")
            exit(-1)
        return float(int(opr[0]) % int(opr[1]))
    elif "exp" == operator:
        if 1 != count:
            print("exp : invalid number of operands")
            exit(-1)
        return math.exp(opr[0])
    elif "abs" == operator:
        if 1 != count:
            print("abs : invalid number of operands")
            exit(-1)
        return math.fabs(opr[0])
    elif "cos" == operator:
        if 1 != count:
            print("cos : invalid number of operands")
            exit(-1)
        return math.cos(opr[0])
    elif "sin" == operator:
        if 1 != count:
            print("sin : invalid number of operands")
            exit(-1)
        return math.sin(opr[0])
    elif "tan" == operator:
        if 1 != count:
            print("tan : invalid number of operands")
            exit(-1)
        return math.tan(opr[0])
    elif "truncate" == operator:
        if 1 != count:
            print("truncate : invalid number of operands")
            exit(-1)
        return math.trunc(opr[0])
    elif "round" == operator:
        if 1 != count:
            print("round : invalid number of operands")
            exit(-1)
        return round(opr[0])
    elif "floor" == operator:
        if 1 != count:
            print("floor : invalid number of operands")
            exit(-1)
        return math.floor(opr[0])
    elif "ceiling" == operator:
        if 1 != count:
            print("ceiling : invalid number of operands")
            exit(-1)
        return math.ceil(opr[0])

    # control flow
    elif "if" == operator:
        if 2 > count or count > 3:
            print("if : invalid number of operands %d")
            exit(-1)
        if opr[0]:
            return opr[1]
        elif count != 3:
            print("if : missing an else expression")
            exit(-1)
        else:
            return opr[2]
    elif "begin" == operator:
        return opr[-1]

    # general
    elif "=" == operator:
        if 1 > count:
            print("= : invalid number of operands")
            exit(-1)
        val = opr[0]
        for i in range(1, count):
            if val != opr[i]:
                return False
        return True
    elif "<" == operator:
        if 1 > count:
            print("< : invalid number of operands")
            exit(-1)
        for i in range(1, count):
            if opr[i-1] >= opr[i]:
                return False
        return True
    elif ">" == operator:
        if 1 > count:
            print("> : invalid number of operands")
            exit(-1)
        for i in range(1, count):
            if opr[i-1] <= opr[i]:
                return False
        return True
    elif ">=" == operator:
        if 1 > count:
            print(">= : invalid number of operands")
            exit(-1)
        for i in range(1, count):
            if opr[i-1] < opr[i]:
                return False
        return True
    elif "<=" == operator:
        if 1 > count:
            print("<= : invalid number of operands")
            exit(-1)
        for i in range(1, count):
            if opr[i-1] > opr[i]:
                return False
        return True
    elif "zero?" == operator:
        if 1 != count:
            print("zero? : invalid number of operands")
            exit(-1)
        if 0 == opr[0]:
            return True
        else:
            return False
    elif "write" == operator:
        if 1 != count:
            print("write : invalid number of operands")
            exit(-1)
        print(opr[0], end='')
        return None
    elif "writeln" == operator:
        if 1 != count:
            print("writeln : invalid number of operands")
            exit(-1)
        print(opr[0])
        return None

    else:
        # find in namespaces
        val = find_val_in_local_namespace(operator)
        if val is None:
            val = find_val_in_global_namespace(operator)
        if val is None:
            print("'%s' is not defined" % operator)
            exit(-1)
        else:
            return val


# evaluation operators which have exceptional expressions
def evaluation_except(expr):
    operator = expr[0]
    opr = expr[1:]
    count = len(opr)
    if "cond" == operator:
        for c in opr:
            count = len(c)
            if 2 > count:
                print("cond : invalid number of operands")
                exit(-1)
            if evaluation(c[0]):
                result = None
                for i in range(1, count):
                    result = evaluation(c[i])
                return result
    elif "let" == operator:
        # adding local variables
        l_namespace.append(dict())
        adding_list = []
        for v in opr[0]:
            if 2 != len(v):
                print("let : val-expr bad syntax")
                exit(-1)
            if isinstance(v[1], list):
                adding_list.append((v[0], evaluation(v[1])))
            elif isfloat(v[1]):
                adding_list.append((v[0], float(v[1])))
            else:
                val = evaluation([v[1]])
                adding_list.append((v[0], val))
        for e in adding_list:
            l_namespace[-1][e[0]] = e[1]
        val = evaluation(opr[1])
        l_namespace.pop()
        return val
    elif "define" == operator:
        if 2 != count:
            print("define : invalid number of operands")
            exit(-1)
        if not isinstance(opr[0], str) or isfloat(opr[0]):
            print("define : name must be string word")
            exit(-1)
        if not add_val_in_global_namespace(opr[0], evaluation(opr[1])):
            print("define : '%s' is already defined" % opr[0])
            exit(-1)
        return None
    elif "set!" == operator:
        if 2 != count:
            print("set! : invalid number of operands")
            exit(-1)
        if not isinstance(opr[0], str) or isfloat(opr[0]):
            print("set! : name must be string word")
            exit(-1)
        if not set_val_in_global_namespace(opr[0], evaluation(opr[1])):
            print("set : '%s' is not defined" % opr[0])
            exit(-1)
        return None
    elif "lambda" == operator:
        if 2 != count:
            print("lambda : invalid number of operands")
            exit(-1)
        # TODO: Implement lambda
    else:
        return False




















