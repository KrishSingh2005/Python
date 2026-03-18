from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret123"


# 🎯 Generate number based on difficulty
def generate_number(level):
    if level == "easy":
        return random.randint(1, 50)
    elif level == "medium":
        return random.randint(1, 100)
    else:
        return random.randint(1, 200)


# 🔥 Set max attempts
def get_max_attempts(level):
    if level == "easy":
        return 5
    elif level == "medium":
        return 4
    else:
        return 3


@app.route("/", methods=["GET", "POST"])
def index():
    # Default level
    if "level" not in session:
        session["level"] = "medium"

    # Generate number if not exists
    if "number" not in session:
        session["number"] = generate_number(session["level"])
        session["attempts"] = 0

    message = ""
    alert = ""

    max_attempts = get_max_attempts(session["level"])

    if request.method == "POST":

        # 🎚 Change difficulty
        if "level" in request.form:
            session["level"] = request.form["level"]
            session["number"] = generate_number(session["level"])
            session["attempts"] = 0
            message = "🔄 Level changed! New game started."

        # 🎯 Guess logic
        elif "guess" in request.form:
            try:
                guess = int(request.form["guess"])

                # ❌ Range check
                if guess < 1 or guess > 200:
                    alert = "⚠️ Enter a valid number!"
                else:
                    session["attempts"] += 1

                    if guess < session["number"]:
                        message = "📉 Too Low!"
                    elif guess > session["number"]:
                        message = "📈 Too High!"
                    else:
                        # 🎉 WIN
                        alert = f"🎉 Correct! Attempts: {session['attempts']}"
                        message = "🏆 You Won!"
                        session.clear()

                        return render_template(
                            "index.html",
                            message=message,
                            alert=alert,
                            level="medium",
                            attempts=0,
                            max_attempts=4
                        )

                    # 💀 LOSE
                    if session["attempts"] >= max_attempts:
                        correct_number = session["number"]
                        message = f"💀 You Lost! Correct number was {correct_number}"
                        alert = "Game Over!"

                        session.clear()

                        return render_template(
                            "index.html",
                            message=message,
                            alert=alert,
                            level="medium",
                            attempts=0,
                            max_attempts=4
                        )

            except:
                alert = "❌ Invalid input!"

    return render_template(
        "index.html",
        message=message,
        alert=alert,
        level=session.get("level"),
        attempts=session.get("attempts", 0),
        max_attempts=max_attempts
    )


if __name__ == "__main__":
    app.run(debug=True)