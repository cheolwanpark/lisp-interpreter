import math


def evaluation(expr):
    if not isinstance(expr, list):
        return float(expr)

    operator = expr[0]
    opr = list(map(evaluation, expr[1:]))
    count = len(opr)

    if "+" == operator:
        result = 0
        for i in range(count):
            result += opr[i]
        return result
    elif "-" == operator:
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
        result = opr[0]
        for i in range(1, count):
            result /= opr[i]
        return result
    elif "min" == operator:
        result = opr[0]
        for i in range(1, count):
            a = opr[i]
            if a < result:
                result = a
        return result
    elif "max" == operator:
        result = opr[0]
        for i in range(1, count):
            a = opr[i]
            if a > result:
                result = a
        return result
    elif "expt" == operator:
        if 2 != count:
            print("invalid operands for expt")
            return -1
        return math.pow(opr[0], opr[1])
    elif "log" == operator:
        if 1 == count:
            return math.log(opr[0])
        elif 2 == count:
            return math.log(opr[0], opr[1])
        else:
            print("invalid operands for log")
            return -1



