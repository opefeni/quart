# import libraries
from quart import Quart

# instantiate quart object
app = Quart(__name__)

# declare default error message for HTTP error 404
text_404 = (
 "The requested URL was not found on the server. "
 "If you entered the URL manually please check your "
 "spelling and try again."
)

# declare error handler decorator
# for 500 error
@app.errorhandler(500)
def error_handling_500(error):
    return {"Error": str(error)}, 500

# for 404 error
@app.errorhandler(404)
def error_handling_404(error):
    return {"Error" : str(error), "Description" : text_404}, 404

@app.route('/api')
def my_microservice():
    raise TypeError("This is a testing exception")

if __name__ == '__main__':
    app.run()