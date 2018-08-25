from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
	a = request.args.get('a')
	b = request.args.get('b')
	return a + b

if __name__ == '__main__':
    app.run(debug = True)