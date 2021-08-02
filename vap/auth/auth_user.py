from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps
from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.UserEntity
cur = db.entity.find({})
Users=list(cur)
app = Flask(__name__)
app.config['SECRET_KEY']='Th1s1ss3cr3t'
def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):

      token = None

      if 'x-access-tokens' in request.headers:
         token = request.headers['x-access-tokens']

      if not token:
         return jsonify({'message': 'a valid token is missing'})

      try:
         data = jwt.decode(token, app.config[SECRET_KEY])
         current_user = Users.query.filter_by(public_id=data['public_id']).first()
      except:

            return jsonify({'message': 'token is invalid'})
      else:

        return f(current_user, *args, **kwargs)
   return decorator
def login_user():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'SECRET_KEY: "login required"'})

    user = Users.query.filter_by(name=auth.username).first()

    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('could not verify', 401, {'Done Reg: "login required"'})