from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True




page_header = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
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
    """
form = """
        <form action="/" method="POST">
            <label for="rot">Rotate By:</label>
            <input type="text" name="rot" id="rot" value="0">
            <textarea name="text" id="" cols="30" rows="10">{0}</textarea>
            <input type="submit">
        </form>
        """
      
page_footer= """
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot_val = request.form['rot']
    text_str = request.form['text']
    answer = rotate_string(text_str, int(rot_val))
    return page_header + form.format(answer) + page_footer


@app.route("/")
def index():
    text = ""
    return page_header + form.format(text) + page_footer

app.run()