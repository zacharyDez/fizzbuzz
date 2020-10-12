from flask import Flask, request
import flask_monitoringdashboard as dashboard

from fizzbuzz.fizzbuzz import main

# useful link
# https://medium.com/flask-monitoringdashboard-turtorial/monitor-your-flask-web-application-automatically-with-flask-monitoring-dashboard-d8990676ce83

app = Flask(__name__)

dashboard.config.init_from(file='./dashboard.cfg')
dashboard.bind(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/fizzbuzz')
def fizzbuzz():
    num: int = int(request.args.get('num', None))

    return main(num)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
