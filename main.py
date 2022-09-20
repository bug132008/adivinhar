from flask import Flask, render_template
poss = ["easy", "medium", "hard", "impossivel"]
app = Flask(__name__)
@app.route('/')
def home():
	return render_template("home/index.html")

@app.route('/<nan>/')
@app.route('/<nan>')
def easy(nan):
	return f"<h1>{nan] não encontrada</h1>"
if __name__ == "__main__":
	app.run(debug=True, port=8080)
