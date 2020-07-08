from flask import Flask, request, make_response, jsonify
import json
import regex
import re

# initialize the flask app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])

def webhook():
     
    return make_response(jsonify(results()))

# function for responses
def results():
    req = request.get_json(silent=True, force=True)
    try:
        #action = req.get('queryResult').get('action')
        parameters = req.get('queryResult').get('parameters')
        #print('Dialogflow Parameters:')
        #print(json.dumps(parameters['any'], indent=4))
        query_sentence = parameters('any')
        print(query_sentence)
        print(parameters)

    except AttributeError:
        return 'json error'

def parse(entity, code):
    regex = r"\b(?:" + "|".join(re.escape(entity) for ent in entity) + r")\b"
    reobj = re.compile(regex, re.I)
    return reobj.sub(lambda x:code[x.group(0)], entity)
       
    #return {'fulfillmentText':'is a response'}

#def dataPre(req):  
   # action = req.get('queryResult').get('action')
   # params= req.get('parameters')
    ##return response

# run the app
if __name__ == '__main__':
   app.run()