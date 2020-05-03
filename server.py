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

@app.route('/goodbye',methods=["POST"]) #Only POST requests
def goodbye_world():
    #Close application
    #sys.exit(2) #exit python - only works from main thread
    os._exit(2) #kill python without calling cleanup handlers - not recommended

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
