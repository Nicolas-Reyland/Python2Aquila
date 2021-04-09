import ast
from warning import warn

def handle_expression(expression : ast.Expr) -> str:
	expr_T = type(expression)
	if expr_T is ast.Constant:
		return str(expression.value)
	elif expr_T is ast.Name:
		return str(expression.id)
	elif expr_T is ast.BinOp:
		return handle_bin_op(expression)
	elif expr_T is ast.BoolOp:
		return handle_bool_op(expression)

	return str(expression)

def handle_bin_op(bin_op : ast.BinOp):
	pass

def handle_bool_op(bool_op : ast.BoolOp):
	pass

def match_operator(operator : ast.operator):
	op_T = type(operator)
	if op_T is ast.Add:
		return '+'
	elif op_T is ast.Sub:
		return '-'
	elif op_T is ast.Mult:
		return '*'
	elif op_T is ast.Div:
		return '/'
	elif op_T is ast.Mod:
		return '%'
	else:
		warn('Unkown operator ' + str(operator))
		return '_OP_'

