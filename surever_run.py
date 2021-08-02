from functools import wraps
from flask import *
import jwt
import mongodb_vap
import json

app = Flask(__name__)

def authorize(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None
        clientdata=request.json
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # print(token)
            token_apikey = token.split(' ')
            data = jwt.decode(token_apikey[1], "secret", algorithm="HS256")
            # print(data)
            current_user  = mongodb_vap.user_verified(data=data)
            print(current_user)
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        #
        return f(current_user,clientdata, *args, **kwargs)
    return decorated
@app.route('/entity/create', methods=['POST'])
def create():

    if request.method == 'POST':
        entity_data=request.json
        names = ('Organization_Name', 'Corporate_Email_Address','Entity_Status')
        re_dataset=set(names).issubset(entity_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                    res=mongodb_vap.entity_insert(data=entity_data)
                    print(res)
                    return res
            else:
                return "Something missing your entity fields"
        except:
            return "something wrong please try again"

@app.route('/entity/get', methods=['GET'])
def getdata():
    if request.method == 'GET':
        res=mongodb_vap.entity_get()
        print(res)
        res_json=json.loads(res)
        res_data={"respond":res_json}
        return res_data

@app.route('/entity/update', methods=['PUT'])
def updatedata():

    if request.method == 'PUT':
        entity_data = request.json
        names = ('Corporate_Email_Address', 'updatedata')
        re_dataset = set(names).issubset(entity_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                res = mongodb_vap.entity_update(data=entity_data)
                print(res)
                return res
            else:
                return "Something missing your entity update fields"
        except:
            return "something wrong please try again"

@app.route('/entity/active', methods=['GET'])
def active():
    if request.method == 'GET':
        res_data = {"respond": True}
        return res_data


@app.route('/entity/deactive', methods=['GET'])
def deactive():
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data

@app.route('/user/create', methods=['POST'])
def user():
    if request.method == 'POST':
        entity_data = request.json
        if entity_data:
            names = ('First_Name', 'Email_Address', 'Login_Id','Password')
            re_dataset = set(names).issubset(entity_data)
            print(re_dataset)
            try:
                if re_dataset is True:
                    res = mongodb_vap.user_insert(data=entity_data)
                    print(res)
                    return res
                else:
                    return "Something missing your user fields"
            except:
                return "something wrong please try again"
        else:
            return "Please give required data"
@app.route('/user/get', methods=['GET'])
@authorize
def userget(current_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        print(clientdata)
        print(current_user)
        res=mongodb_vap.user_get()
        # print(json.dumps(res))
        # res_json=json.loads(res)
        res_data={"respond":res}
        return jsonify(res_data)
@app.route('/user/update', methods=['PUT'])
@authorize
def userupdatedata(urrent_user,clientdata, *args, **kwargs):

    if request.method == 'PUT':
        user_data = request.json
        names = ('Email_Address', 'updatedata')
        re_dataset = set(names).issubset(user_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                res = mongodb_vap.user_update(data=user_data)
                print(res)
                return res
            else:
                return "Something missing your user update fields"
        except:
            return "something wrong please try again"
@app.route('/user/delete', methods=['DELETE'])
@authorize
def userdeletedata(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'DELETE':
        entity_data=request.json
        print(entity_data)
        res=mongodb_vap.user_delete(data=entity_data)
        print(res)
        return res
@app.route('/user/active', methods=['GET'])
@authorize
def useractive(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": True}
        return res_data


@app.route('/user/deactive', methods=['GET'])
@authorize
def userdeactive(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data

if __name__ == '__main__':

    app.run(debug=True,port=50088)