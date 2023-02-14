# objective: creating custom url converter unlike using int, float or any
# import libraries
from quart import Quart
from werkzeug.routing import BaseConverter, ValidationError

# initial simple dummy data for testing
_USER = {"1": "Alice", "2": "Bob"}
_IDS = { id: name for id, name in _USER.items()}

# create a custome class to handle the conversion
class RegisteredUser(BaseConverter):
    def to_python(self, value: str)->str:
        if value in _USER:
            return _USER[value]

        raise ValidationError()

    def to_url(self, value: int):
        return _IDS[value]

# instantiate the quart object
app = Quart(__name__)
# add the class to the list of existing conversion
app.url_map.converters["registered"] = RegisteredUser

# map the url to the registered converter
@app.route("/api/person/<registered:name>")
def person(name):
    return {"Hello" : name}

if __name__ == "__main__":
    app.run()