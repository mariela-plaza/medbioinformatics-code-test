import requests
import json
from models import Gene

class Request:
    def __init__(self):
        self._headers = {'Authorization': self.getApiKey()}
        self.base_url = 'https://api2.disgenetplus.com/api/v1'

    def getApiKey(self):
        apiKeyJSONFile = open('apiKey.json')
        apiKey = json.load(apiKeyJSONFile)['apiKey']
        apiKeyJSONFile.close()
        return apiKey

    def print_waiting_message(self):
        print('Request is being made, please hold...')

    def request_disease(self, disease_id):
        self.print_waiting_message()
        query_params = {'disease': f'UMLS_{disease_id}'}
        disease_req = requests.get(f'{self.base_url}/gda/summary', params=query_params, headers=self._headers)
        return disease_req

    def request_gene(self, gene_HGNC_symbol):
        self.print_waiting_message()
        query_params = {'gene_symbol': gene_HGNC_symbol}
        gene_req = requests.get(f'{self.base_url}/entity/gene', params=query_params, headers=self._headers)
        return gene_req

class Response:
    def __init__(self, req_response):
        self.status = req_response['status']
        if self.status == 'OK':
            self.data = req_response['payload']
        
    def get_disease(self):
        if self.status == 'OK':
            if self.check_returned_data():
                genes_associated_data = map(self.create_gene_data, self.data)
                return list(genes_associated_data)[0:10]
            else:
                return []

    def create_gene_data(self, data):
        return Gene(data).create_table_info()

    def get_gene_variants(self):
        if self.status == 'OK':
            if self.check_returned_data():
                return self.data[0]['geneToVariants']
            else:
                return []
    
    def check_returned_data(self):
        return len(self.data) != 0
        