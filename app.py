import json
import mariadb
import dbcreds
import dbhelper
import uuid
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)


@app.post('/api/client')
def new_client():
    # try to check req endpoint data in dbhelper and calls procedure to create a new client
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","password"])
        # if it has req info username and password then returns none
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure('call new_client(?,?)',[request.json.get("username"),request.json.get("password")])
        # if results come back as a list jsonify results
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response('sorry something went wrong',500)
    # some except blocks with possible errors
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')

@app.post('/api/login')
def login():
    # try to check req endpoint data in dbhelper and calls procedure to log client in and create token
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","password"])
        # if it has req info username and password then returns none
        if(error != None):
            return make_response(jsonify(error),400)
        # generating token with uuid
        token = uuid.uuid4().hex
        results = dbhelper.run_procedure('call login(?,?,?)',[request.json.get("username"),request.json.get("password"),token])
         # if results come back as a list jsonify results
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return 'something went wrong'
    # some except blocks with possible errors
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')


@app.post('/api/post')
def new_post():
    # try to check req endpoint data in dbhelper and calls procedure to post
    try:
        # checks data for required content and token
        error = dbhelper.check_endpoint_info(request.json,["content","token"])
        # if req info is recieved then returns None if anything other than none this if block returns an error
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure('call new_post(?,?)',[request.json.get("content"),request.json.get("token")])
        # if results are returned as list then jsonify results
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response('sorry something went wrong',500)
    # some except blocks with possible errors
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')



app.run(debug=True)
