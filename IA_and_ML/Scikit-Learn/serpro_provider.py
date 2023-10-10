import base64
import requests


class ConsultaNFe:

    def __init__(self, consumer_key, consumer_secret) -> None:
        self.url_base = 'https://gateway.apiserpro.serpro.gov.br'
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = 'Bearer ' + self.__auth()

    # Autenticação (método privado -> chamada apenas no construtor)
    # Key e Secret são convertidos para base64 e enviados no header da requisição
    def __auth(self):
        url = self.url_base + '/token'
        key_base64 = base64.b64encode(
            (self.consumer_key + ':' + self.consumer_secret).encode('ascii')).decode('ascii')
        data = {
            'grant_type': 'client_credentials'
        }
        headers = {
            'Authorization': 'Basic ' + key_base64
        }
        response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            return response.json()['access_token']
        else:
            print('Erro na autenticação')
            return None

    # Consulta de NFe
    def consulta(self, chave):
        url = self.url_base + '/consulta-nfe-df/api/v1/nfe/' + chave
        response = requests.get(
            url, headers={'Authorization': self.access_token})

        if response.status_code == 200:
            return response.json()
        else:
            # print('Erro na consulta: ' + str(response.json()))
            if response.reason == 'Unauthorized':
                self.access_token = 'Bearer ' + self.__auth()
                return self.consulta(chave)
            return None
