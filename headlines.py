from flask import Flask 

app = Flask(__name__)

@app.route("/")

def get_news():
	return "no news is good news"

if __name__ == '__name__':
	app.run(port=5000, debug=True)