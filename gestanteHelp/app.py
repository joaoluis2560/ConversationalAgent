from flask import Flask, request
import requests
from covid_bot import *
import facebook

app = Flask(__name__)


FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'joao'  # <paste your verify token here>
PAGE_ACCESS_TOKEN = 'EAANqZAeREJwEBAEnjZB2zyGlHQAjn0zzFsHIkGYVsPFVvK2V8GfwxiKjrto3tcXY236lcZB6HOoZAYZBbgFWiIlcQqywoRuuQGVZAnw51SAkGmB8sopcV18crBZAwdkeDNiDU2STaxslIpiIZCYcI9vKj1DmwKDu9482QH7ZCDgcb6FuieLjnYQcJ'  # paste your page access token here>"

def get_name(user_id):
    params = {
        "access_token": PAGE_ACCESS_TOKEN,
        "fields":"first_name"
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    u = requests.get("https://graph.facebook.com/v2.6/{userPSID}".format(userPSID=user_id), params=params, headers=headers)
    if u.status_code != 200:
        logar(u.status_code)
        logar(u.text)

    user=u.json()
    logar("OOO - user name")
    logar(user["first_name"])
    return user["first_name"]


def send_message(recipient_id, text):
    """Send a response to Facebook"""
    payload = {
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload
    )

    return response.json()



def get_bot_response(message):
    """connected chatbot here"""

    reply = main(message)

    return reply
    

def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")

    else:
        return "incorrect"
    

def manda_user (sender_id):
    sender = get_name(sender_id)
    print(sender)

def respond(sender, message):
    """Formulate a response to the user and
    pass it on to a function that sends it."""
    response = get_bot_response(message)
    send_message(sender, response)


def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))


      


@app.route("/", methods=['GET', 'POST'])
    

def listen():
    """This is the main function flask uses to
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)


    elif  request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                manda_user(sender_id)
                respond(sender_id, text)



        return "ok"
    else:
        return "something wrong here"

@app.route("/apptest")
def testing():
    return "App is working"


   

if __name__ == "__main__":
    app.run(debug=True)
