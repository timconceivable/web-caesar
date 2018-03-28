from flask import Flask, request
from caesar import caesar_encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <form method='post'>
            <div>
                <label for='rot'>Rotate by:</label>
                <input name='rot' type='text' value='0'>
                <p class='error'>
                </p>
            </div>
            <textarea name='text' type='text'>{text}</textarea>
            <input type='submit' value='Encrypt'>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(text="The cat was playing the saxophone in the garden at night.")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    return form.format(text=caesar_encrypt(text,rot))

app.run()   