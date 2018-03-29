from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['Debug'] = True 

form = """
<!doctype html>
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
        </style>
    </head>
    <body>
        <form action="/" method='post'>
        <label>Rotate by:
            <input type="text" name="rot" value='0'/>
        </label>

        <textarea type="text" name="text" value='[0]'>{0}</textarea>
        <input type="Submit" value="Submit" /> 
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    encrypt_text = rotate_string(text, int(rot))
    return form.format(encrypt_text)
    
app.run()
