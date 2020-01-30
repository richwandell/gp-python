from flask import Flask
app = Flask(__name__)


@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1: int, num2: int) -> str:
    """
    Multiply 2 numbers
    :param num1:
    :param num2:
    :return:
    """
    return str(num1 * num2)


@app.route('/display')
def display() -> str:
    """
    Displays static text
    :return:
    """
    return """
    Lorem Ipsum
    """


@app.route('/display/<sometext>')
def display_some_text(sometext: str) -> str:
    """
    Displays the text following the path /display/
    :param sometext:
    :return:
    """
    return sometext


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=5000)
