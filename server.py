from flask import *
import mongodb_vap
import json

app = Flask(__name__)

@app.route('/entity/create', methods='POST')
def create():

    if request.method == 'POST':
        entity_data=request.json
        res=mongodb_vap.entity_insert(data=entity_data)
        print(res)
        return res
@app.route('/entity/get', methods='GET')
def create():
    if request.method == 'GET':
        res=mongodb_vap.entity_get()
        print(res)
        res_json=json.loads(res)
        res_data={"respond":res_json}
        return res_data

if __name__ == '__main__':

    app.run(debug=True)