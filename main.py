from flask import Flask, render_template
poss = ["easy", "medium", "hard", "impossivel"]
app = Flask(__name__)
@app.route('/')
def home():
	return render_template("home/index.html")
@app.route('/easy')
@app.route('/easy/')
def easy():
	return render_template("easy/index.html")
@app.route('/medium/')
@app.route('/medium')
def medio():
    return render_template('medium/index.html')
@app.route('/hard/')
@app.route('/hard')
def hard():
    return render_template('hard/index.html')
@app.route('/impossivel/')
@app.route('/impossivel')
def impossivel():
    return render_template('impossivel/index.html')

@app.route('/<nan>/')
@app.route('/<nan>')
def notPage(nan):
	return f"<h1>{nan} não encontrada</h1>"
if __name__ == "__main__":
	app.run(debug=True, port=8080)
