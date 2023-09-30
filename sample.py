from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and a function to handle the request


@app.route('/')
def hello_world():
    return 'Hello, World!!'


@app.route("/<string:name>")
def index3(name):
    return f"<h1>hello,{name}</h1>"


# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(port=3032, debug=True)
