import random
import os

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    try:
        if request.method == 'GET':
            roll_dice_no = random.randint(1, 6)
            dice_image = os.path.join(
                '/static/images/', f'dice{roll_dice_no}.png')
            return render_template("index.html", dice_image=dice_image)
    except Exception as e:
        raise e


if __name__ == '__main__':
    app.run(debug=True)
