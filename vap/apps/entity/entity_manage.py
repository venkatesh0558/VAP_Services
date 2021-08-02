from pymongo import MongoClient
import json
import bcrypt

client = MongoClient('localhost:27017')

db = client.UserEntity
# cur = db.user.find({})
# cur_list = []
# for i in cur:
#     # print(i)
#     cur_list.append(i)
# doc_data={'Organization_Name':'AP_Police',
#           'updatedata':{
#     "Organization_Name":"AP_Police",
#     "Corporate_Email_Address": "ap_police@apgov.org",
#     "StartDate": "2021-07-19 15:16:03.185502",
#     "EndDate":"2021-12-19 15:16:03.185502",
#     "Zip/Postal_Code:":"121212",
#     "Entity_Status":"active",
#     "Ph_no:":"08672_221133"
# }}
# db.entity.update_one({"Organization_Name":"AP_Police"},{"$set":doc_data['updatedata']}
password='rao123'
hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(hashpass)
res=bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user[
    'password'].encode('utf-8'):
