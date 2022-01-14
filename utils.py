import requests
from models import Gene

class Request:
    def __init__(self):
        self.headers = {'Authorization': '7e90948a-4418-4f2b-99cb-8386e1b1d57f'}
        self.baseUrl = 'https://api2.disgenetplus.com/api/v1';

    def requestDisease(self, diseaseId):
        queryParams = {'disease': f'UMLS_{diseaseId}'}
        diseaseReq = requests.get(f'{self.baseUrl}/gda/summary', params=queryParams, headers=self.headers)

        return diseaseReq

    def requestGene(self, geneHGNCsymbol):
        queryParams = {'gene_symbol': geneHGNCsymbol}
        geneReq = requests.get(f'{self.baseUrl}/entity/gene', params=queryParams, headers=self.headers)

        return geneReq

class Response:
    def __init__(self, reqResponse):
        self.data = reqResponse['payload']

    def getDiseaseData(self):
        genesAssociatedData = map(self.createGeneData, self.data)
        return list(genesAssociatedData)[0:10]

    def createGeneData(self, data):
        return Gene(data).generateGeneTableInfo()

    def getGeneData(self):
        return self.data[0]['geneToVariants']