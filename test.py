# Python2Aquila
import ast
import instruction_handler

s = '''a = 5
print(a)
a += 5 / (1 - a)

def func(x : int, y = 5):
	for i in range(int(x)):
		x /= i
	if 1 > x > 0:
		return 1
	elif x == 2:
		return 0
	else:
		return -1

l = [1, 2, 3]
i = 0

while True:
	l[i] += l[i + 1]
	i += i
	i %= 2
	print(len(l))
	print(l.__len__())
'''

tree = ast.parse(s)

source = map(instruction_handler.handle_instruction, tree.body)

for line in source:
    print(line)

#
