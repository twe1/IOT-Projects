from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	return render_template('home.html',title="IOT !!")


if __name__ == '__main__':
	app.run('0.0.0.0',debug=True)