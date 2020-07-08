import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./service_account.json')
firebase_admin.initialize_app(cred)

banco = firestore.client() 

class nome_cliente(object):
     def __init__(self, params):
        """Initializes the Forecast object
        gets the forecast for the provided dates
        """

        self.nome = params['nome']
        self.db = self.busca_dados

     def busca_dados(self):
    
        nome_do_cliente = self.nome
        paciente_ref = banco.collection(u'paciente')

    ## ver nome paciente
        query = paciente_ref.where(u'nome', u'==', nome_do_cliente)
    
        if (query == nome_do_cliente): 
            speech = "voce ja e cadastrado"
        return speech

def validate_params(parameters):
    #validar ou nao lista de parametros

    # Inicializa parametros ou erros
    error_response = ''
    params = {}

    # 
    if (parameters.get('nome')): #and
            #isinstance(parameters.get('address'), dict)):
        params['nome'] = parameters.get('nome')
    else:
        params['nome'] = None
        error_response += 'por favor diga seu nome '

    return error_response.strip(), params


    

