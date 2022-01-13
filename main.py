import models
import fire
from tabulate import tabulate


def printDisease(diseaseId):
    """
    Returns the diseaseId introduced
    :param diseaseId: identifier of the disease to search
    """
    firstGene = models.Gene({'symbolOfGene':"PRC1","score": 0.9, "yearInitial": 2008, "yearFinal": 2021})
    print(tabulate([firstGene.generateGeneTableInfo()], headers=["Gene HGNC symbol", "Score", "Initial Year", "Final Year"]))

def printGene(geneHGNCsymbol):
    """
    Returns the geneHGNCsymbol introduced       
    :param geneHGNCsymbol: HGNC symbol of the gene to search
    """
    numberOfVariants = 5
    print(tabulate([[geneHGNCsymbol, numberOfVariants]], headers=["Gene Symbol", "Number of variants"]))

if __name__ == "__main__":
    fire.Fire({
        "disease": printDisease,
        "gene": printGene
    })