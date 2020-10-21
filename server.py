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


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port,debug=True)
