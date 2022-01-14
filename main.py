import models
from utils import Request, Response

import fire
from tabulate import tabulate

request = Request();

def printDiseaseInformation(diseaseId):
    """
    Returns the first 10 genes associated with the disease identified by the diseaseId provided.
    The results are organized by descending score. The information provided fo each gene is:
        * Gene HGNC symbol
        * Score
        * Initial Year
        * Final Year
    :param diseaseId: identifier of the disease to search
    """

    diseaseRequest = request.requestDisease(diseaseId)
    diseaseResponse = Response(diseaseRequest.json())
    associatedGenes = diseaseResponse.getDiseaseData()
    print(tabulate(associatedGenes, headers=["Gene HGNC symbol", "Score", "Initial Year", "Final Year"]))

def printGeneInformation(geneHGNCsymbol):
    """
    Returns the Gene HGNC symbol introduced and the number of variants associated with said gene. 
    :param geneHGNCsymbol: HGNC symbol of the gene to search
    """

    geneRequest = request.requestGene(geneHGNCsymbol);
    geneResponse = Response(geneRequest.json())
    numberOfVariants = len(geneResponse.getGeneData())
    print(tabulate([[geneHGNCsymbol, numberOfVariants]], headers=["Gene Symbol", "Number of variants"]))

if __name__ == "__main__":
    fire.Fire({
        "disease": printDiseaseInformation,
        "gene": printGeneInformation
    })