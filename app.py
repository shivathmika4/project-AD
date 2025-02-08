from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")  # Get user input
        print(f"User Input: {msg}")  # Print to Visual Studio command shell
        return render_template("result.html", message=msg)  # Redirect to result page

    return render_template("predict.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
