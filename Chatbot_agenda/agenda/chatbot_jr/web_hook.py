#!/usr/bin/env python

import urllib
import json
import os
import firebase

from flask import Flask
from flask import request
from flask import make_response
from db import nome_cliente, validate_params

# Flask app should start in global layout
app = Flask(__name__)
    

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    print("Request:")
    print(json.dumps(req, indent=4))

    
    if action == 'consulta.nome':
        res = consultar_nome(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def consultar_nome(req):

    parameters = req['queryResult']['parameters']['nome'] 
    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    error, clientes_params = validate_params(parameters)
    if error:
        return error

    try:
        db = nome_cliente(clientes_params)
    # return an error if there is an error getting the forecast
    except (ValueError, IOError) as error:
        return error
    
    if db.nome:
        response = db.busca_dados()

        return response
   
    

    #try:
      #  res = busca_dados(req)
   # except: 
       # return ("diga seu nome")
    
   # firebase = firebase.FirebaseApplication(ID_PROJETO,', None)
  #  docs = firebase.get("/usuario","/usuarios/nomes",nome_usuario)
     
     
        #speech = ("olá senhor" + nome_usuario + "e um prazer atendê-lo")

    #else:

        #speech = ("nao achamos o seu cadastro")

        #res = str(speech)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 2000))

    print ("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
