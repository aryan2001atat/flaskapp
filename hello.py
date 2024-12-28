from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Update 3: The Jenkins CICD pipeline is working!!!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True)

