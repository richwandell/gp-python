import os
from flask import Flask, jsonify
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
    print("hi")
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


@app.route('/getjson')
def get_json() -> str:
    """
    Returns a JSONAPI response using jsonify function from flask.
    This function will set application/json content type header as well as translate the dict into json string.
    :return:
    """
    return jsonify({
      "type": "articles",
      "id": "1",
      "attributes": {
        "title": "Rails is Omakase"
      },
      "relationships": {
        "author": {
          "links": {
            "self": "/articles/1/relationships/author",
            "related": "/articles/1/author"
          },
          "data": {"type": "people", "id": "9" }
        }
      }
    })


if __name__ == "__main__":
    import argparse  # for parsing passed parameters through terminal

    parser = argparse.ArgumentParser()
    parser.add_argument("--environment", help="Hostname", default="development")
    args = parser.parse_args()

    environment = args.environment
    if environment == 'development':
        os.environ['FLASK_ENV'] = environment
        app.run('localhost', debug=True, port=5000)
    else:
        import os, bjoern
        bjoern.run(app, '0.0.0.0', 80)
