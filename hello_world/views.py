from flask import request

from hello_world import app
from hello_world.formater import PLAIN, SUPPORTED, get_formatted

moje_imie = "Bartas"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie, output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
