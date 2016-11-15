import ast
import json

from flask import Flask, render_template, request
import phpserialize


app = Flask('unserializer')


@app.route('/unserializer', methods=['GET', 'POST'])
def index():
    serialized = request.form.get('serialized', '')
    unserialized = None
    try:
        unserialized = phpserialize.loads(serialized)
    except ValueError:
        pass

    if not unserialized:
        try:
            unserialized = json.loads(serialized)
        except ValueError:
            pass

    if not unserialized:
        try:
            unserialized = ast.literal_eval(serialized)
        except (SyntaxError, ValueError):
            pass

    formatted_unserialized = ''
    if unserialized:
        formatted_unserialized = json.dumps(unserialized, indent=2)

    return render_template('index.html',
        formatted_unserialized=formatted_unserialized,
        serialized=serialized
    )
