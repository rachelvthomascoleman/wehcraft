from flask import Flask
import json
import os
import sys

# Create Flask server instance
# __name__ is a special variable.
# Its name is set to "__main__" when the program is running.
app = Flask(__name__)

# When someone asks for '/', give them the output of hello_world()
@app.route('/')
def hello_world():
    # Make moves JSON
    retval = {
        "Hello": "World"
    }
    resp = app.make_response(json.dumps(retval))
    resp.headers["Content-Type"] = "application/json"
    return resp

@app.route('/goodbye', methods=["POST"]) #Only POST requests
def goodbye_world():
    #Compare password to header on GET request
    headers = request.headers()
    #Close application
    os._exit(2) #kill python without calling cleanup handlers - not recommended

@app.route('/password', methods=["GET"]) #Only GET requests
def get_password():
    #Get password out of environment variable
    password = os.environ.get('SECRET_PASSWORD', 'asdf')
    #Return password
    retval = {
        "password": password
    }
    resp = app.make_response(json.dumps(retval))
    resp.headers["Content-Type"] = "application/json"
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
