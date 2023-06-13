import json
import mariadb
import dbcreds
import dbhelper
import uuid
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)

@app.post('/api/client')
def new_client():
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure('call new_client(?,?)',[request.json.get("username"),request.json.get("password")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response('sorry something went wrong',500)
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')

@app.post('/api/login')
def login():
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        token = uuid.uuid4().hex
        results = dbhelper.run_procedure('call login(?,?,?)',[request.json.get("username"),request.json.get("password"),token])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return 'something went wron'
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')


@app.post('/api/post')
def new_post():
    try:
        error = dbhelper.check_endpoint_info([request.json.get("content")],["content","token"])
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure('call new_post(?,?)',[request.json.get("content"),request.json.get("token")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response('sorry something went wrong',500)
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')



app.run(debug=True)
