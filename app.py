from flask import Flask, request

from fizzbuzz.fizzbuzz import main

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/fizzbuzz')
def fizzbuzz():
    num: int = int(request.args.get('num', None))

    return main(num)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
