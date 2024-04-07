from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client=MongoClient("mongodb://localhost:27017")
db = client.pirateslv2

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/list", methods=["GET"])
def list_todo():
    contents = list(db.todos.find({}, {'_id':False}))
    return jsonify({"result": contents})

@app.route('/post', methods=["POST"])
def post_todo():
    content_receive = request.form["content_give"]
    doc = {
        'content': content_receive
    }
    db.todos.insert_one(doc)
    return jsonify({"msg": "등록 완료!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)