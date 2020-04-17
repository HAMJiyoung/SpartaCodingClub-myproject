from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

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
    return jsonify({'result':'success', 'msg': '전송 완료!'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)