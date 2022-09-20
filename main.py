from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
	return render_template("home/index.html")

@app.route('/<diff>/')
@app.route('/<diff>')
def easy(diff):
	return render_template(f'{diff}/index.html')
if __name__ == "__main__":
	app.run(debug=True, port=8080)
