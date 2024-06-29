from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string to the console
    return Response(parameter, mimetype='text/plain')  # Return plain text

@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate a list of numbers from 0 to the parameter, exclusive
    numbers = '\n'.join(str(i) for i in range(parameter))
    return Response(numbers, mimetype='text/plain')  # Return plain text

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    # Define the operations dictionary
    operations = {
        'add': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'div': lambda x, y: x / y if y != 0 else 'Infinity',
        'mod': lambda x, y: x % y,
    }
    if operation in operations:
        result = operations[operation](num1, num2)
        return Response(f'{num1} {operation} {num2} = {result}', mimetype='text/plain')  # Return plain text
    else:
        return Response('Invalid operation. Please use add, sub, mul, div, or mod.', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
