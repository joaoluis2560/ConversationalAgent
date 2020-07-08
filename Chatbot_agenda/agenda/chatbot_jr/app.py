#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    result = req.get("result")
    disp_actions = {"sobre_mim.contatos":sobreMimContato(result)}
    action = result.get("action")
    if action in disp_actions:
        texto = disp_actions[action]
        return texto
    else:
        return{}
    
    

def sobreMimContato(result):
    
    parameters = result.get("parameters")
    contact = parameters.get("contatos")

    contatos = {'celular':'+55(54) 99999-0909', 'e-mail':'vendas@bortoliniimoveis.com.br', 'telefone':'+55(54) 3314-2020', 
    'whats':'+55(54) 98888-1122'}
    all_contacts = ''
    if (contact == '') and (result.get("actionIncomplete")):
        for v in contatos:
            if v == sorted(contatos.keys())[-1]:
                all_contacts += v + '.'
            else:
                all_contacts += v + ', '
        speech = 'Como que voce gostaria de entrar em contato conosco?\n' + all_contacts.upper()
    elif contact == 'todos':
        
        for i, j in contatos.items():
            all_contacts += '; ' + i + ': ' + j
        speech = "Claro! " + contact + " os meus contatos sao" + all_contacts + "."
    else:
        speech = "Claro! meu " + contact + " e " + contatos[contact] + "."

    print("Response:")
    print(speech)

    return {
        "fulfillmentText": speech
        
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
