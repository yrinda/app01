from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
def multiplie():
	a = int(request.args.get('a'))
	b = int(request.args.get('b'))
	op = request.args.get('op')
	
	if op == '+':
		return str(a + b)
	elif op == '-':
		return str(a - b)
	elif op == '*':
		return str(a * b)
	else:
		return str(a / b) 


if __name__ == '__main__':
	app.run(debug = True)