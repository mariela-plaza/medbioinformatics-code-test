from tabulate import tabulate

class Gene:
    """Model class for Gene"""
    def __init__(self, geneData):
        self.geneSymbol = geneData['symbolOfGene']
        self.geneScore = geneData['score']
        self.geneInitialYear = geneData['yearInitial']
        self.geneFinalYear = geneData['yearFinal']

    def generateGeneTableInfo(self):
        geneTableInfo = [self.geneSymbol, self.geneScore, self.geneInitialYear, self.geneFinalYear];
        return geneTableInfo;
    
    # def __str__(self):
    #     geneTableInfo = [self.geneSymbol, self.geneScore, self.geneInitialYear, self.geneFinalYear]
    #     return tabulate(geneTableInfo, headers=["Gene HGNC symbol", "Score", "Initial Year", "Final Year"])