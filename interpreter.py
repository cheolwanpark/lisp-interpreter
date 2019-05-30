import parse
import evaluation

filename = "input.txt"
file = open(filename)
code = file.read()
file.close()
code = parse.preprocess(code)
code = parse.parse(code)
for c in code:
    val = evaluation.evaluation(c)
    print(val)



