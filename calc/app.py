from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def do_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<p>{add(a, b)}</p>"

@app.route('/sub')
def do_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<p>{sub(a, b)}</p>"

@app.route('/mult')
def do_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<p>{mult(a, b)}</p>"

@app.route('/div')
def do_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<p>{div(a, b)}</p>"


operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<p>{operations[operation](a, b)}</p>"