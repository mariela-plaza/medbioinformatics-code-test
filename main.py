import fire

def printDisease(diseaseId):
    """
    Returns the diseaseId introduced
    :param diseaseId: identifier of the disease to search
    """
    print("Disease:", diseaseId)

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