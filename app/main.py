from app import app, db
from models import *


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    create_tables()
    app.run()