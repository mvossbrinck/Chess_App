from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chessboard.html')

@app.route('/move/<int:depth>/<path:fen>/')
def get_move(depth, fen):
    print(depth)
    print("Calculating...")
    engine = Engine(fen)
    move = engine.iterative_deepening(depth - 1)
    print("Move found!", move)
    print()
    return move

app.config["TEMPLATES_AUTO_RELOAD"] = True


if __name__ == "__main__":
    app.run()
