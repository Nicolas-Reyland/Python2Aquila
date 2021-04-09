# Python2Aquila
import ast
import instruction_handler

s = '''a = 5
print(a)
a += 1 - a
def func(x : int, y = 5):
	for i in range(x):
		x /= i
	if x == 0:
		return 1
	else:
		return -1
'''

tree = ast.parse(s)

source = []
for instruction in tree.body:
    source.append(instruction_handler.handle_instruction(instruction))

for line in source:
    print(line)

#
