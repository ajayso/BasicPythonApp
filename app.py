import os, newrelic.agent
from flask import Flask, request, session

app = Flask(__name__)
#newrelic.agent.initialize('newrelic.ini')


@app.route('/',methods=['POST'])
def hello():
    print("The arguments are ", request.args)
    payload = request.form
    print("The payload is ", payload)
    print("I am Alive high five")
    incoming_msg = request.values.get('Body', '').lower()
    print(incoming_msg)
    incoming_msg = request.data
    print(incoming_msg)
    return("Hello its working")
 
 
@app.route('/message')
def hello_message_name(name):
   return 'Hello Message %s!' % name
   
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)