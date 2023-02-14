from quart import Quart, request

# instantiate quart object
app = Quart(__name__)

@app.route('/')
def auth():
    print("Quart's Authorization Information")
    print(request.authorization)
    return ""


if __name__ == "__main__":
    app.run()