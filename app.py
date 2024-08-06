from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

if __name__ == '__main__':
    app.config.update(
        TEMPLATES_AUTO_RELOAD = True
    )
    app.run(host='0.0.0.0', port=5000, debug=True)
