from flask import Flask, jsonify, request, Response, redirect, render_template
import json
import jwt,datetime
from appConfig import *

# from flask_moment import Moment


users = [
    {
        'name': 'shashank',
        'age': 26,
        'company': 'IRIS'
    },
    {
        'name': 'Manish',
        'age': 26,
        'company': 'Apple'
    },
    {
        'name': 'Pratyush',
        'age': 26,
        'company': 'Apple'
    },
    {
        'name': 'Sandesh',
        'age': 26,
        'company': 'Adobe'
    }
]
#------------------------------ Implementing JWT Web Token------------------------------------#
@app.route("/login")
def getToken():
    expirationTime = datetime.datetime.utcnow() + datetime.timedelta(seconds = 10000)
    token = jwt.encode({'exp' : expirationTime }, "meow", algorithm='HS256')
    return token

#----------------------------------------------------------------------------------------------

def validateUserRequest(userObject):
    if("name" in userObject and "age" in userObject and "company" in userObject):
        return True
    else:
        return False


@app.route("/users/redirect")
def redirectUser():
    return redirect('http://www.google.com')


@app.route("/users/View/<string:name>")
def getHtml(name):
    return "<h1 style=\"color:blue\">I can project HTML as well..%s impressed??</h1>" % name


@app.route("/users")
def getAllUsers():
    return jsonify({'users': users})


@app.route("/users/<string:company>")
def getUsersByCompany(company):
    searchUsers = []
    i = 0
    for user in users:
        i += 1
        if(user["company"] == company):
            searchUsers.insert(i, user)

    return jsonify({'users': searchUsers})


@app.route("/users/delete/<string:name>", methods=["DELETE"])
def deleteUserByName(name):
    for user in users:
        if(name == user["name"]):
            users.remove(user)

    response = Response("", 201, mimetype="application/json")
    return response


@app.route("/users/save", methods=['POST'])
def Add_User():
    requestObject = request.get_json()
    if(validateUserRequest(requestObject)):
        new_user = {
            "name": requestObject['name'],
            "age": requestObject['age'],
            "company": requestObject['company']
        }

        users.insert(0, new_user)
        response = Response(response="", status=201,
                            mimetype='application/json')
        response.headers['Location'] = '/users/' + str(new_user['company'])
        return response
    else:
        invalidObjectErrorMsg = {
            "errorMessage": "The object is not in correct format"
        }
        response = Response(response=json.dumps(
            invalidObjectErrorMsg), status=400, mimetype='application/json')
    return response

@app.errorhandler(404)
def handle_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(501)
def handle_internal_error(e):
    return render_template("501.html"), 501

#--------------------------- using rendering engine to show presentation  (JINJA2) ----------------------------#


@app.route("/users/displayJinja/<name>")
def displayJinja(name):
    return render_template("userlists.html", Name=name, Users=users)

# ---------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)
