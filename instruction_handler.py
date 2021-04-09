# Handle the instructions
import ast
import expression_handler as expr_handler
from warning import warn

def handle_instruction(instruction : ast.AST) -> str:
	T = type(instruction)
	if T is ast.Expr:
		return expr_handler.handle_expression(instruction)
	# Assignments
	if T is ast.Assign:
		return handle_assignment(instruction)
	if T is ast.AugAssign:
		return handle_aug_assignment(instruction)
	# Nested instructions
	if T is ast.For:
		return handle_for(instruction)
	if T is ast.While:
		return handle_while(instruction)
	if T is ast.If:
		return handle_if(instruction)
	# Functions
	if T is ast.FunctionDef:
		return handle_function_def(instruction)
	
	print(instruction)
	return 'unknown'

def handle_assignment(assignment : ast.Assign) -> str:
	var_name = assignment.targets[0].id
	value = expr_handler.handle_expression(assignment.value.value)
	return f'${var_name} = {value}'

def handle_aug_assignment(assignment : ast.AugAssign) -> str:
	var_name = assignment.target.id
	# get value str
	value = expr_handler.handle_expression(assignment.value)
	# operator
	op = expr_handler.match_operator(assignment.op)
	return f'${var_name} {op}= {value}'

def handle_function_def(function_def : ast.FunctionDef) -> str:
	print(function_def.name)
	args_string = ', '.join(map(lambda x: x.arg, function_def.args.args))
	func_body_str = '\n'.join(map(handle_instruction, function_def.body))
	func_str = f'function recursive auto {function_def.name}({args_string})\n' + \
			func_body_str + '\n' + \
			'end-function'
	return func_str

def handle_for(for_loop : ast.For):
	for_loop_body = '\n'.join(map(handle_instruction, for_loop.body))
	iterator = expr_handler.handle_expression(for_loop.iter)
	iterator_var = expr_handler.handle_expression(for_loop.target)
	return 'for-loop'

def handle_while(while_loop : ast.While):
	return 'while'

def handle_if(if_else : ast.If):
	return 'if'


