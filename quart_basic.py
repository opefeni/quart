# import library
from quart import Quart

# instantiate the quart object
app = Quart(__name__)

@app.route("/api")
def my_microservice():
    return {"Hello" :  "World"}

@app.route("/person/<int:person_id>")
def person(person_id):
    return {"Hello": person_id}

if __name__ == "__main__":
    app.run()