from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def age():
	age = int(request.args.get('age'))

	if age < 10:
		return '10歳未満なんですね'
	elif age < 18:
		return '18歳未満なんですね'
	elif age == 18:
		return 'ちょうど18歳なんですね'
	else:
		return '18歳以上だからって特に何もありませんよ?'

if __name__ == '__main__':
	app.run(debug = True)