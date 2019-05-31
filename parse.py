import re

def preprocess(code):
    code = re.sub(r';.*\n', '', code)
    code = code.replace("\n", "")
    code = code.replace("\t", "")
    code = code.rstrip()
    return code


def parse_parentheses_and_spaces(s):
    result = []
    start = 0
    count = 0
    processed = 0
    for i in range(len(s)):
        # print("(%c %d)"%(s[i], count))
        if '(' == s[i]:
            if 0 == count:
                start = i+1
            count += 1
        elif ')' == s[i]:
            count -= 1
            if 0 == count:
                others = s[processed:start-1].split()
                for o in others:
                    result.append(o)
                result.append(s[start:i])
                processed = i+1
                start = 0
            elif count < 0:
                print("invalid parentheses")
                exit(-1)
    if count != 0:
        print("invalid parentheses")
        exit(-1)
    others = s[processed:].split()
    count = len(others)
    if 0 != len(result):
        for i in range(count):
            result.append(others[i])
    return result


def parse(s):
    parsed = parse_parentheses_and_spaces(s)
    if 0 == len(parsed):
        result = s.split()
        if 1 == len(result):
            return result[0]
        else:
            return result
    else:
        result = []
        for s in parsed:
            a = parse(s)
            result.append(a)
        return result
