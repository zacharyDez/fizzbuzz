import time

import statsd
from flask import Flask, request

from fizzbuzz.fizzbuzz import main

c = statsd.StatsClient('localhost', 8125)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/fizzbuzz')
def fizzbuzz():
    start = time.time()
    num: int = int(request.args.get('num', None))

    dur = (time.time() - start) * 1000
    c.timing("tasktime", dur)
    c.incr("taskcount")

    return main(num)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
