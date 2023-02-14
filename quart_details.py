# import the required libraries
from quart import Quart, request, jsonify

#instantiate the quart object
app = Quart(__name__)

# call the app route decorator
@app.route("/api", provide_automatic_options=False)
# make the function async
async def my_microservice():
    # examine the request object
    print(dir(request))
    response = jsonify({"Hello":"World"})
    print(response)
    print(await response.get_data())
    return response


if __name__ == "__main__":
    print(app.url_map)
    app.run()