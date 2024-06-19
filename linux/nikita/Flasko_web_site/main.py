from website import create_app
from flask import Flask, render_template

app = create_app()

@app.route('/')
def home():
    return render_template('welcome.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")