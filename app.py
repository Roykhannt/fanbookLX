from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://roykhananto:learningx@cluster0.vge15c4.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc= {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.btsfans.insert_one(doc)
    return jsonify({'msg':'POST request!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.btsfans.find({},{'_id': False}))
    return jsonify({'messages':message_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)