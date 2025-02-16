from flask import Flask, render_template, request

app = Flask(__name__)

# 1. HOME ROUTE
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
