import json
from flask import jsonify, request
from application import create_app, db

app = create_app()


@app.route("/")
def hello_devops():
    return jsonify(hello="DevOps")


@app.route('/insert', methods=['POST'])
def insert():
    from models import RawData
    data = request.get_json()
    obj = RawData(raw_data=json.dumps(data))
    db.session.add(obj)
    db.session.commit()
    return jsonify(data=data)


@app.route('/read')
def read():
    from models import RawData
    objs = RawData.query.all()
    return jsonify(data=[{'ins_datetime': o.ins_datetime, 'raw_data': o.raw_data} for o in objs])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)