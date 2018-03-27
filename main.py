from flask import Flask
from caesar import rotate_string

app = Flask(__name__)
app.config['Debug'] = True 

form = """
<!doctype html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method='post'>
        <label>Rotate by:
            <input type="text" name="rot" value='0'/>
        </label>

        <input type="textarea" name="text" />
        <input type="submit" /> 
    </body>
</html>
"""

@app.route("/")
def index():
    return form 


app.run()
