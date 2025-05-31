from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>那一天的憂鬱憂鬱起來</h1>'

@app.route('/about')
def about():
    return '<p>那一天的憂鬱憂鬱起來</p>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
