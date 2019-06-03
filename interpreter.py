import parse
import evaluation
import sys
import time

filename = "input.txt"
file = open(filename)
code = file.read()
file.close()
start_t = time.time()
code = parse.preprocess(code)
code = parse.parse(code)
print("parsing time : %s seconds" % (time.time() - start_t))
sys.setrecursionlimit(10000)
print("recursion limit %d" % sys.getrecursionlimit())
print("============================= results =============================")
start_t = time.time()
for c in code:
    val = evaluation.evaluation(c)
    if None is not val:
        if isinstance(val, float) and val.is_integer():
            val = int(val)
        print(val)
print("============================= results =============================")
print("evaluating time : %s seconds" % (time.time() - start_t))
