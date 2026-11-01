
from flask import Flask, render_template, request
from checker import check_password
from generator import generate_password

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    strength = None
    feedback = []

    if request.method == "POST":

        password = request.form.get("password", "")

        if password:
            strength, feedback = check_password(password)

    return render_template(
        "index.html",
        strength=strength,
        feedback=feedback
    )


@app.route("/generate", methods=["POST"])
def generate():

    try:
        length = int(request.form.get("length", 16))
        password = generate_password(length)

        return render_template(
            "index.html",
            generated_password=password,
            generated_length=length
        )

    except ValueError:
        return render_template(
            "index.html",
            generator_error="Choose a length between 12 and 64."
        )


if __name__ == "__main__":
    app.run(debug=True)
