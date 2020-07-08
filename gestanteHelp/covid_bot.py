"""Install the following requirements:
    dialogflow        0.5.1
    google-api-core   1.4.1
"""
import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToJson
from data import *
from app import *

# reply templates

DIALOGFLOW_PROJECT_ID = 'tese-lyhmix'
DIALOGFLOW_LANGUAGE_CODE = 'pt-BR'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'googlekey.json'
SESSION_ID = 'FB_BOT'  # this can be anything

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)


def get_response(user_query):
    text_to_be_analyzed = user_query
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    answer = response.query_result.fulfillment_text
    intent = response.query_result.intent.display_name
    print(intent)
    action = response.query_result.action
    print(action)

    # print('debug answer -> ', answer)
    # print('debug params -> ', parameters)
    return answer, intent, action




def nome_gestante(answer, action, sender):


        if action == 'input.welcome':

            nome = manda_user(sender_id)
            
            answer = ("ola {usna}".format(usna=nome), sender_id)
        else:
            print('nao e isso')

        return answer

    #         type_of_data = parameters['Info-type']

    #         if len(state) == 1 and len(state) < 3:
    #             try:
    #                 req_data = get_state_cases(state[0], type_of_data)
    #             except:
    #                 req_data = answer
    #         if len(state) > 1:
    #             r = list()
    #             dt = ''
    #             ti = ''
    #             st = ''
    #             for s in state:
    #                 try:
    #                     r = get_state_cases(s, type_of_data)
    #                     dt = dt + ',' + r[0]
    #                     ti = ti + ',' + r[1]
    #                     st = st + ',' + s
    #                 except:
    #                     req_data = answer
    #         if type(req_data) == tuple:
    #             d = req_data[0]
    #             t = req_data[1]
    #             reply = reply_temp_1.format(type_of_data, state[0], d, t)
    #         elif len(ti) > 0:
    #             reply = reply_temp_1.format(type_of_data, state, req_data, ti)
    #         else:
    #             d = req_data
    #             reply = reply_temp.format(type_of_data, state[0], d)
    #     else:
    #         reply = answer
    # else:
    #     reply = answer

    # return reply


def main(user_query):
    # user_query = input('Input -> ')
    answer, intent, action = get_response(user_query)
    sender = respond(sender_id)
    if intent == 'Welcome_Intent':
        reply = nome_gestante(answer,action)
    else:
        print('erro')
        
    return reply

# print('Press "/stop" to exit..')
# while True:
#    q = main()
#    if q == '/stop':
#        break

# user_query = 'total confirmed cases in india'
# user_query = 'Hi'
