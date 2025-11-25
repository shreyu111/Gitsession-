import __main__
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "data":{
            "regno":24122003,
            "name":"Abhinav",
            "email":"abhinav.tiwari@msds.christuniversity.in"

        }
    }
# TODO: create CRUD apis for this app

if __name__ == "__main__":
    app.run(debug=True)