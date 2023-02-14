# import library
from quart import Quart
import yaml

# instantiate quart object
app = Quart(__name__)

# declare yamlify function
def yamlify(data, status=200, headers=None):
    _headers = {"Content-Type": "application/x-yaml"}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data), status, _headers

# create route endpoint
@app.route('/api')
def my_microservice():
    return yamlify(["Hello", "YAML", "World"])

if __name__ == '__main__':
    app.run()
