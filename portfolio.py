from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@3.34.46.136', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('New_01.html')

@app.route('/contacts', methods=['POST'])
def write_mail():
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    message_receive = request.form['message_give']

    contact = {
        'name': name_receive,
        'email': email_receive,
        'message': message_receive,
    }
    db.contacts.insert_one(contact)
    return jsonify({'result':'success', 'msg': 'post!'})

@app.route('/cards', methods=['GET'])
def read_cards():
    cards = list(db.cards.find({},{'_id':0}))
    return jsonify({'result':'success', 'cards': cards})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)