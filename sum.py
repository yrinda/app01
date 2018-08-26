from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def sum():
	a = int(request.args.get('a'))
	b = int(request.args.get('b'))
	return str(a + b)

'''
another pattern

a = request.args.get('a', type = int)
b = request.args.get('b', type = int)
'''
	

if __name__ == '__main__':
    app.run(debug = True)