from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "This code has been changed to check the working of kubernetes! and we are now working on Jenkins too."

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True)

