import models
import fire

def printDisease(diseaseId):
    """
    Returns the diseaseId introduced
    :param diseaseId: identifier of the disease to search
    """
    firstGene = models.Gene({'symbolOfGene':"PRC1","score": 0.9, "yearInitial": 2008, "yearFinal": 2021})
    print("Disease data:", firstGene)

def printGene(geneHGNCsymbol):
    """
    Returns the geneHGNCsymbol introduced       
    :param geneHGNCsymbol: HGNC symbol of the gene to search
    """
    print("Gene symbol:", geneHGNCsymbol)

if __name__ == "__main__":
    fire.Fire({
        "disease": printDisease,
        "gene": printGene
    })