from app import app

@app.route("/hello")
def hello():
    return "Hello world !!! in Flask !!!"

