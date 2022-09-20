from flask import Flask, render_template
poss = ["easy", "medium", "hard", "impossivel"]
app = Flask(__name__)
@app.route('/')
def home():
	return render_template("home/index.html")

@app.route('/<diff>/')
@app.route('/<diff>')
def easy(diff):
	for possi in poss:
		if possi == diff:
			return render_template(f'{diff}/index.html')
		else:
			pass
if __name__ == "__main__":
	app.run(debug=True, port=8080)
