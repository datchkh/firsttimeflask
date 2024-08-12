from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 style="color: red;">My first Flask App!<h1>'

@app.route('/greet/<name><last_name>')
def greet(name, last_name):
    return f"Hello {name} {last_name}"



@app.route('/add/<int:number1>/<int:number2>/<int:number3>')
def add(number1, number2, number3):
    return f"{number1} + {number2} + {number3} = {number1 + number2 + number3}"

@app.route('/handle_url_params')
def handle_url_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting.capitalize()}, {name}"
    else:
        return "Some parameters are missing"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)